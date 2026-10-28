import ast
import hashlib
import inspect
import os
import sys

import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import q9


q9_testcases = [
    # Visible testcases
    (5, 10, '5 * 1 = 5\n5 * 2 = 10\n5 * 3 = 15\n5 * 4 = 20\n5 * 5 = 25\n5 * 6 = 30\n5 * 7 = 35\n5 * 8 = 40\n5 * 9 = 45\n5 * 10 = 50', True),
    (1, 1, '1 * 1 = 1', True),
    (12, 15, '12 * 1 = 12\n12 * 2 = 24\n12 * 3 = 36\n12 * 4 = 48\n12 * 5 = 60\n12 * 6 = 72\n12 * 7 = 84\n12 * 8 = 96\n12 * 9 = 108\n12 * 10 = 120\n12 * 11 = 132\n12 * 12 = 144\n12 * 13 = 156\n12 * 14 = 168\n12 * 15 = 180', True),
    (7, 20, '7 * 1 = 7\n7 * 2 = 14\n7 * 3 = 21\n7 * 4 = 28\n7 * 5 = 35\n7 * 6 = 42\n7 * 7 = 49\n7 * 8 = 56\n7 * 9 = 63\n7 * 10 = 70\n7 * 11 = 77\n7 * 12 = 84\n7 * 13 = 91\n7 * 14 = 98\n7 * 15 = 105\n7 * 16 = 112\n7 * 17 = 119\n7 * 18 = 126\n7 * 19 = 133\n7 * 20 = 140', True),
    (3, 5, '3 * 1 = 3\n3 * 2 = 6\n3 * 3 = 9\n3 * 4 = 12\n3 * 5 = 15', True),
    (3, 4, '3 * 1 = 3\n3 * 2 = 6\n3 * 3 = 9\n3 * 4 = 12', True),
    (7, 1, '7 * 1 = 7', True),

    # Hidden testcases
    (9, 3, '31a0b201f6aa64d6a1e484b1c9ccf2dd78699c770629146e49d6dc39c04581cb', False),
    (15, 7, '90ff010e2272dec0b389d1ff84c04ac905dc445fee054b786fcdaa7f897f50e3', False),
    (2, 12, '5ec78ebf6786b0db04a1cc2a403ae9a2edc2b2e1fe5e5ed0a3098a48db1af457', False),
    (11, 4, 'eece0a8ada9d5240fbb9817828c9e53238af5deccbe96becbef19cdf88bb840e', False),
    (8, 8, 'b1ce79f54ff3b6968fc864c0f7ff538a21cc21e0907d656b00c07e83ee2de6b0', False),
    (100, 100, '703bf21d5800716c279195df7afc1f679fca935bec4c60f64ca2e372d6512faf', False),
    (1, 100, 'c9edc9e23a9afb52b6c02bc5f897ef7bde89afb9e183999b03f68c0ab023fbc7', False),
    (100, 1, '4a6fed3a19e31a73a7473d62033ca72a7f43ee47ed3ecd5e1efdac6e4066e88c', False),
]


def hashcode(value):
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def check_direct_recursion():
    tree = ast.parse(inspect.getsource(q9))
    functions = [node for node in tree.body if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))]
    assert len(functions) == 1 and functions[0].name == "multiplication_table", (
        "Define only multiplication_table; helper functions are not allowed."
    )
    func = functions[0]
    assert [arg.arg for arg in func.args.args] == ["number", "last_multiplier"], (
        "Use the two parameters specified in the worksheet."
    )
    assert not (func.args.defaults or func.args.kwonlyargs or func.args.vararg or func.args.kwarg or func.args.posonlyargs), (
        "Use exactly the two required parameters."
    )
    disallowed = (ast.Global, ast.Nonlocal, ast.For, ast.AsyncFor, ast.While,
                  ast.ListComp, ast.SetComp, ast.DictComp, ast.GeneratorExp)
    assert not any(isinstance(node, disallowed) for node in ast.walk(func)), (
        "Loops, comprehensions, and global variables are not allowed."
    )
    nested_helpers = [node for node in ast.walk(func) if node is not func and isinstance(node, (
        ast.FunctionDef, ast.AsyncFunctionDef, ast.Lambda))]
    assert not nested_helpers, "Helper functions are not allowed."
    recursive_calls = [node for node in ast.walk(func) if isinstance(node, ast.Call) and (
        (isinstance(node.func, ast.Name) and node.func.id == "multiplication_table") or
        (isinstance(node.func, ast.Attribute) and node.func.attr == "multiplication_table")
    )]
    assert recursive_calls, "Use direct recursion in multiplication_table."


@pytest.mark.parametrize("number, last_multiplier, expected, visible", q9_testcases)
def test_q9(number, last_multiplier, expected, visible, capsys):
    check_direct_recursion()
    result = q9.multiplication_table(number, last_multiplier)
    output = capsys.readouterr().out
    assert result is None, "The function must print the table and return nothing."
    if output.endswith("\n"):
        output = output[:-1]  # A single final newline is optional.
    assert len(output.splitlines()) == last_multiplier, (
        "Print one line for each multiplier from 1 to last_multiplier."
    )
    if visible:
        assert output == expected, "The printed multiplication table or formatting is incorrect."
    else:
        assert hashcode(output) == expected, "The printed multiplication table or formatting is incorrect."
