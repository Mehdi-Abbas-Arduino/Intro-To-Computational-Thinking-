import ast
import hashlib
import inspect
import os
import sys

import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import q5


q5_testcases = [
    # Visible testcases
    (4, '1\n1 2\n1 2 3\n1 2 3 4', True),
    (1, '1', True),
    (5, '1\n1 2\n1 2 3\n1 2 3 4\n1 2 3 4 5', True),

    # Hidden testcases
    (2, 'da57c7587ea165f9b854320ceeb8229dcca10a4696088a00884b72fdb3cfc218', False),
    (3, 'cd1a6799ebc43a089c1100c224c1ebcd1bf635df6a14ba6a6b2f79bb76e7258b', False),
    (6, 'b6526c75c3be3e264cc2b2cdc394dff0d0bb4b418879615a0c5649d7fbef4d7c', False),
    (7, 'd0148621172fe87d88013931ae0406b394854e23183c56b012cb30fc27ce7a5f', False),
    (8, '71cd0c3c8ab5a9e2bc647118cb5c24f0a612e563d0c03652cc501dec8db01f18', False),
    (10, '99e062b05fd3b48d4c761f702a17737652fa8fd7e7d9d2d212415cad62ef2ac8', False),
    (12, '346ce8fe63810109b17c87ac544f9e575c47749e196ed95e3491c7f2638d6875', False),
    (15, 'fa1555ec51fd55880931b1cd1a1e23fedb4f46f5857a4545a241cfc7f76bd9bb', False),
    (25, '4e60bd23d4124ac8604689fa13ad8c02fc4b7edcd38f7c5a20b699e82322d3ba', False),
    (30, 'b1cee51d70c205e4c402a8ac3d9b3d740fea0ed98c89850c5edca606a0d79c9a', False),
    (50, 'cfde470724f5b2eaef34e1ee5f307408cf502d018b2fa93a33646c9edd975cdf', False),
    (100, 'd848a37b411cc82ceb766ae87548ebc505c108cdd9a7871ad81016e4c642e308', False),
]

def hashcode(value):
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def check_recursion_rules():
    tree = ast.parse(inspect.getsource(q5))
    public = [node for node in tree.body
              if isinstance(node, ast.FunctionDef) and node.name == "print_number"]
    assert len(public) == 1, "Define the required print_number function."
    function = public[0]
    assert function.args.posonlyargs == [] and function.args.args and function.args.args[0].arg == "number_of_rows", (
        "The first parameter of print_number must be named number_of_rows."
    )
    arguments = function.args
    assert [p.arg for p in arguments.args] == ["number_of_rows"] and not (
        arguments.posonlyargs or arguments.kwonlyargs or arguments.vararg or
        arguments.kwarg or arguments.defaults or arguments.kw_defaults
    ), "print_number must take exactly one parameter: number_of_rows."
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

    assert has_cycle("print_number"), (
        "You must use recursion in print_number or in a helper called by it."
    )
    helpers = {name for name in names if name != "print_number"}
    assert helpers, "A recursive helper function is required."
    invoked = reachable("print_number") & helpers
    assert invoked, "print_number must call a helper function."
    # At least one helper called (directly or indirectly) from print_number
    # must itself recurse. Purely iterative or direct-only recursion is insufficient.
    assert any(has_cycle(name) for name in invoked), (
        "A helper function used by print_number must be recursive."
    )

@pytest.mark.parametrize("number_of_rows, expected, visible", q5_testcases)
def test_q5(number_of_rows, expected, visible, capsys):
    check_recursion_rules()
    result = q5.print_number(number_of_rows)
    output = capsys.readouterr().out
    assert result is None, "The function must print the result and return nothing."
    if output.endswith("\n"):
        output = output[:-1]  # Allow a final newline, but not blank extra lines.
    if visible:
        assert output == expected, "Printed output does not match the worksheet."
    else:
        assert hashcode(output) == expected, "Printed output does not match the worksheet."
