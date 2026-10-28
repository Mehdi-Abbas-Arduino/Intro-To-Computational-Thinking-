import ast
import hashlib
import inspect
import os
import sys

import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import q4


q4_testcases = [
    # Visible testcases
    (3, '1\n1\n2', True),
    (5, '1\n1\n2\n3\n5', True),
    (1, '1', True),
    (7, '1\n1\n2\n3\n5\n8\n13', True),

    # Hidden testcases
    (2, 'c553228271d4cf65305957e97cd75da60964776a9e615c702bd6a4c077d266c0', False),
    (4, 'ce83839cecace70b9271a6ddc6cf55a213ecb0ee4a52514816ded093e6c95bd3', False),
    (6, 'd6fe9c8d41f6e586ac68b84ec9dffe17c76313f5ffb50d762d80d3f73f96a708', False),
    (8, '7b3a56ee86509532208a1596768395dc218a1c18bf960207c281c1a54d2a71e1', False),
    (10, '8b5b408c3debcd1dc4c8a2508cc9179dfd6119ef49571b1cd3458a4672273e07', False),
    (12, '3379cf6dfceaabc8e8fcb2b2dc15a9abaa5ab423af8beb5ded1071188b6f0a4e', False),
    (15, 'd2234048d4f09aa4b88143f0d56801bfbe31012139bb83626839c465270610f5', False),
    (20, 'c0a64e4d796161b8533f96f7f23b6904a40a46b7d71e9cf947bfa341a99c6dda', False),
    (35, 'c995d804b08d15afd525755bd448e78117ad48d246ed32afe3c5e7e5577e440c', False),
    (50, 'db74c07d068dd8b2f8edff62604112e97375b4d8a4c249f33064689d888e9aeb', False),
    (100, 'a5fc6fb16e99835c2ef649611db1450bdbd7ad0c50ca95d69d6e3d0e8ed3a37f', False),
]

def hashcode(value):
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def check_recursion_rules():
    tree = ast.parse(inspect.getsource(q4))
    public = [node for node in tree.body
              if isinstance(node, ast.FunctionDef) and node.name == "print_fibb"]
    assert len(public) == 1, "Define the required print_fibb function."
    function = public[0]
    assert function.args.posonlyargs == [] and function.args.args and function.args.args[0].arg == "number_of_terms", (
        "The first parameter of print_fibb must be named number_of_terms."
    )
    # Additional parameters are permitted only if the function remains callable
    # with a single number_of_terms argument.
    sig = inspect.signature(q4.print_fibb)
    try:
        sig.bind(3)
    except TypeError:
        pytest.fail("print_fibb must be callable with only number_of_terms.")
    forbidden = (ast.Global, ast.For, ast.AsyncFor, ast.While,
                 ast.ListComp, ast.SetComp, ast.DictComp, ast.GeneratorExp)
    assert not any(isinstance(node, forbidden) for node in ast.walk(tree)), (
        "Loops, comprehensions, global variables, and other iteration are not allowed."
    )

    # Find calls between named functions, including local (nested) helpers.
    # Exclude nested function definitions from their enclosing function's own calls.
    functions = [node for node in ast.walk(tree)
                 if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))]
    names = {node.name for node in functions}

    class CallCollector(ast.NodeVisitor):
        def __init__(self):
            self.names = set()
        def visit_FunctionDef(self, node):
            return
        def visit_AsyncFunctionDef(self, node):
            return
        def visit_Call(self, node):
            if isinstance(node.func, ast.Name):
                self.names.add(node.func.id)
            self.generic_visit(node)

    graph = {}
    for definition in functions:
        visitor = CallCollector()
        for statement in definition.body:
            visitor.visit(statement)
        graph.setdefault(definition.name, set()).update(visitor.names & names)

    def reachable(root):
        seen = set()
        def visit(name):
            if name in seen:
                return
            seen.add(name)
            for target in graph.get(name, ()): visit(target)
        visit(root)
        return seen

    def has_cycle(root):
        seen, active = set(), set()
        def visit(name):
            if name in active:
                return True
            if name in seen:
                return False
            active.add(name)
            if any(visit(target) for target in graph.get(name, ())):
                return True
            active.remove(name)
            seen.add(name)
            return False
        return visit(root)

    assert has_cycle("print_fibb"), (
        "You must use recursion in print_fibb or in a helper called by it."
    )


@pytest.mark.parametrize("number_of_terms, expected, visible", q4_testcases)
def test_q4(number_of_terms, expected, visible, capsys):
    check_recursion_rules()
    result = q4.print_fibb(number_of_terms)
    output = capsys.readouterr().out
    assert result is None, "The function must print the result and return nothing."
    if output.endswith("\n"):
        output = output[:-1]  # Allow a final newline, but not blank extra lines.
    if visible:
        assert output == expected, "Printed output does not match the worksheet."
    else:
        assert hashcode(output) == expected, "Printed output does not match the worksheet."
