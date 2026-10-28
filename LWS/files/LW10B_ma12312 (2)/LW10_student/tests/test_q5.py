import ast
import hashlib
import inspect
import os
import sys

import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import q5


CASES = [
    # Visible Testcases
    (1, '1', True),
    (5, '1\n2\nChai\n4\nBiscuit', True),
    (16, '1\n2\nChai\n4\nBiscuit\nChai\n7\n8\nChai\nBiscuit\n11\nChai\n13\n14\nChaiBiscuit\n16', True),
    (7, '1\n2\nChai\n4\nBiscuit\nChai\n7', True),
    (34, '1\n2\nChai\n4\nBiscuit\nChai\n7\n8\nChai\nBiscuit\n11\nChai\n13\n14\nChaiBiscuit\n16\n17\nChai\n19\nBiscuit\nChai\n22\n23\nChai\nBiscuit\n26\nChai\n28\n29\nChaiBiscuit\n31\n32\nChai\n34', True),

    # Hidden Testcases
    (2, 'b598b3a62a3f7cedb17e66d1cb31d53dffeebaf5c07e2c60d5e31971936fd35e', False),
    (3, 'dd1622344e409d1a8c2b24a24626f67c9912c0e11838129dcd422c996a73f151', False),
    (4, '682296dac1a26db83b88baf879967773a7f5d5dd441665e680f7d339cd8b1b19', False),
    (6, '26fbe234f722624d7f3be5aecbb6051eb0f2956eeb7e10ca3481a6af91c39c2e', False),
    (10, '5ea449cbb327a52dcfc9bdac5d68eb4f7a9b1d7ae163ac1a67814bab0f57289d', False),
    (15, 'dabe339ab4676d83308a41e9071733626ce6d7aa22f9c360b95c2a9de38f489e', False),
    (23, 'cb68ffeb56ad8ac3f4585a07420bfaf2420d4d2d36eba19e5b934446057df628', False),
    (48, '6ae37f3ab3c553ae7affba974a7b8db6e942aa0de037000366c6d02f6e813306', False),
    (90, '01432bfc3acd1cd5b6b1af7058233ca3ceac82282917b507fcf47d0408c63eb3', False),
    (500, '4c7e787566ea74b19daee259fab0e4b6dd95c7ae36b52b2de7faec85b51d68d9', False),
]


def check_constraints():
    tree = ast.parse(inspect.getsource(q5))
    functions = [
        node for node in ast.walk(tree)
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
    ]
    assert len(functions) == 1 and functions[0].name == "print_rewards", (
        "Define only print_rewards(); helper functions are not allowed."
    )

    function = functions[0]
    assert [arg.arg for arg in function.args.args] == ["last_order"], (
        "Use the specified last_order parameter."
    )
    assert not function.args.defaults and not function.args.kw_defaults, (
        "Do not define default parameters."
    )
    assert not function.args.vararg and not function.args.kwarg, (
        "print_rewards() must take exactly one parameter."
    )
    assert not function.args.kwonlyargs and not function.args.posonlyargs, (
        "print_rewards() must take one ordinary parameter."
    )

    forbidden = (
        ast.For, ast.AsyncFor, ast.While,
        ast.ListComp, ast.SetComp, ast.DictComp, ast.GeneratorExp,
        ast.Global, ast.Nonlocal,
    )
    assert not any(isinstance(node, forbidden) for node in ast.walk(function)), (
        "Use recursion without loops, comprehensions, or global variables."
    )
    assert any(
        isinstance(node, ast.Call)
        and isinstance(node.func, ast.Name)
        and node.func.id == "print_rewards"
        for node in ast.walk(function)
    ), "print_rewards() must call itself recursively."


@pytest.mark.parametrize(
    "last_order, expected, visible",
    CASES,
    ids=[f"{'visible' if c[2] else 'hidden'}-{i:02d}" for i, c in enumerate(CASES, 1)],
)
def test_q5(capsys, last_order, expected, visible):
    check_constraints()
    result = q5.print_rewards(last_order)
    assert result is None, "print_rewards() must print and return None."

    printed = capsys.readouterr().out
    if printed.endswith("\n"):
        printed = printed[:-1]

    if visible:
        assert printed == expected, f"Expected {expected!r}; printed {printed!r}."
    else:
        digest = hashlib.sha256(printed.encode("utf-8")).hexdigest()
        assert digest == expected, "Incorrect output for this hidden test case."
