import ast
import hashlib
import inspect
import os
import sys

import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import q8


q8_testcases = [
    # Visible testcases
    (0, 6, '0, 2, 4, 6', True),
    (1, 5, '2, 4', True),
    (-3, 3, '-2, 0, 2', True),
    (2, 3, '2', True),
    (3, 4, '4', True),
    (1, 1, '', True),
    (0, 0, '0', True),
    (1, 6, '2, 4, 6', True),
    (0, 5, '0, 2, 4', True),

    # Hidden testcases
    (4, 4, '4b227777d4dd1fc61c6f884f48641d02b4d121d3fd328cb08b5531fcacdabf8a', False),
    (5, 10, '3b549f0e2d99f69e2e4a4709cf6f0970c97e715be170c3da0713eb60f9467b3e', False),
    (-10, -7, 'e9839dcb054802f92105e1cef99368c06949cfd9a5145784d99fc018282b74e9', False),
    (-9, -2, 'c844a09bef1e246a635d3c79064991d81f29f8f19fc23378bcb7074b7c9b66ca', False),
    (-1, -1, 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855', False),
    (99, 100, 'ad57366865126e55649ecb23ae1d48887544976efea46a48eb5d85a6eeb4d306', False),
]


def hashcode(value):
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def check_direct_recursion():
    source = inspect.getsource(q8)
    tree = ast.parse(source)
    funcs = [node for node in tree.body if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))]
    assert len(funcs) == 1 and funcs[0].name == "print_lift_stops", (
        "Define only print_lift_stops; helper functions are not allowed."
    )
    func = funcs[0]
    assert [arg.arg for arg in func.args.args] == ["first_floor", "last_floor"], (
        "Use the two parameters specified in the worksheet."
    )
    assert not func.args.defaults and not func.args.kwonlyargs and not func.args.vararg and not func.args.kwarg, (
        "Use exactly the two required parameters."
    )
    disallowed = (ast.Global, ast.Nonlocal, ast.For, ast.AsyncFor, ast.While,
                  ast.ListComp, ast.SetComp, ast.DictComp, ast.GeneratorExp)
    assert not any(isinstance(node, disallowed) for node in ast.walk(func)), (
        "Do not use loops, comprehensions, or global variables."
    )
    nested = [node for node in ast.walk(func) if node is not func and isinstance(node, (
        ast.FunctionDef, ast.AsyncFunctionDef, ast.Lambda
    ))]
    assert not nested, "Helper functions are not allowed."
    recursive_calls = [node for node in ast.walk(func) if isinstance(node, ast.Call) and (
        (isinstance(node.func, ast.Name) and node.func.id == "print_lift_stops") or
        (isinstance(node.func, ast.Attribute) and node.func.attr == "print_lift_stops")
    )]
    assert recursive_calls, "Use direct recursion in print_lift_stops."


@pytest.mark.parametrize("first_floor, last_floor, expected, visible", q8_testcases)
def test_q8(first_floor, last_floor, expected, visible, capsys):
    check_direct_recursion()
    result = q8.print_lift_stops(first_floor, last_floor)
    output = capsys.readouterr().out
    assert result is None, "The function must print the stops and return nothing."
    if output.endswith("\n"):
        output = output[:-1]  # A single final newline is optional.
    assert "\n" not in output, "All lift stops must be on a single line."
    if visible:
        assert output == expected, "The printed lift stops or their formatting are incorrect."
    else:
        assert hashcode(output) == expected, "The printed lift stops or their formatting are incorrect."
