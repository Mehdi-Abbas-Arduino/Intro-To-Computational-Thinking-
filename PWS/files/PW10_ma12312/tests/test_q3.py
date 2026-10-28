import ast
import hashlib
import inspect
import os
import sys

import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import q3


q3_testcases = [
    # Visible testcases
    (3, '1, 2, 3', True),
    (13, '1, 2, 3, 4, Buzz, 6, 7, 8, 9, Buzz, 11, 12, 13', True),
    (20, '1, 2, 3, 4, Buzz, 6, 7, 8, 9, Buzz, 11, 12, 13, 14, Buzz, 16, 17, 18, 19, Buzz', True),
    (-13, 'Error: last_number must be a positive integer.', True),
    ('thirteen', 'Error: last_number must be a positive integer.', True),
    (5, '1, 2, 3, 4, Buzz', True),
    (1, '1', True),
    (0, 'Error: last_number must be a positive integer.', True),
    (-3, 'Error: last_number must be a positive integer.', True),

    # Hidden testcases
    (10, '9fbabf8783b4da4c00a939df6e5086203fd28a451a441614e10db2dd22ba534c', False),
    (23, 'abdd7a717563c5059c362373e19cfe96856d884e1fd5bb1381cbdb8d33ccd985', False),
    ((lambda x: x), '17234883c75d6167f06594e6f743011266cee675e4ff1d59f9bb85c947ec17ff', False),
    (100, '501e53714e6eff35aacfbb6691fdced4e469703c883bdd194aa78e586ec406bf', False),
    (6, '7168ec165a6e1c450239931b5c92ad3f31d06a471bce36786eaf50a4ec769af8', False),
    (True, '17234883c75d6167f06594e6f743011266cee675e4ff1d59f9bb85c947ec17ff', False),
]


def hashcode(value):
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def check_recursion_rules():
    tree = ast.parse(inspect.getsource(q3))
    functions = [node for node in ast.walk(tree) if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))]
    public = [node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name == "count_buzz"]
    assert len(public) == 1, "Define the required count_buzz function."
    starter = public[0]
    parameters = starter.args
    assert len(parameters.posonlyargs) == 0 and [arg.arg for arg in parameters.args] == ["last_number"], (
        "count_buzz must take the one parameter named last_number."
    )
    assert not (parameters.defaults or parameters.kwonlyargs or parameters.vararg or parameters.kwarg), (
        "count_buzz must take exactly the one required parameter."
    )
    forbidden = (ast.Global, ast.For, ast.AsyncFor, ast.While,
                 ast.ListComp, ast.SetComp, ast.DictComp, ast.GeneratorExp)
    assert not any(isinstance(node, forbidden) for node in ast.walk(tree)), (
        "Loops, comprehensions, and global variables are not allowed."
    )

    names = {node.name for node in functions}

    class CalledNames(ast.NodeVisitor):
        def __init__(self):
            self.names = set()
        def visit_FunctionDef(self, node):
            return  # Analyse nested definitions separately.
        def visit_AsyncFunctionDef(self, node):
            return
        def visit_Call(self, node):
            if isinstance(node.func, ast.Name):
                self.names.add(node.func.id)
            self.generic_visit(node)

    graph = {}
    for func in functions:
        visitor = CalledNames()
        for statement in func.body:
            visitor.visit(statement)
        graph.setdefault(func.name, set()).update(visitor.names & names)

    # A call cycle reachable from count_buzz supports both direct recursion
    # and recursive helpers, including helpers defined inside count_buzz.
    visited, on_path = set(), set()

    def has_recursive_cycle(name):
        if name in on_path:
            return True
        if name in visited:
            return False
        on_path.add(name)
        for target in graph.get(name, ()):
            if has_recursive_cycle(target):
                return True
        on_path.remove(name)
        visited.add(name)
        return False

    assert has_recursive_cycle("count_buzz"), (
        "Use recursion in count_buzz or in a recursive helper called by count_buzz."
    )


@pytest.mark.parametrize("last_number, expected, visible", q3_testcases)
def test_q3(last_number, expected, visible, capsys):
    check_recursion_rules()
    result = q3.count_buzz(last_number)
    output = capsys.readouterr().out
    assert result is None, "count_buzz must print its output and return nothing."
    if output.endswith("\n"):
        output = output[:-1]  # A single final newline is optional.
    assert "\n" not in output, "Print the entire result on one line."
    if visible:
        assert output == expected, "Printed output or formatting does not match the worksheet."
    else:
        assert hashcode(output) == expected, "Printed output or formatting does not match the worksheet."
