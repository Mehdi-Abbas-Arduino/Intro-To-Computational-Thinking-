import ast
import hashlib
import inspect
import os
import sys

import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import q1


CASES = [
    # Visible Testcases
    (5, -3, '5, 4, 3, 2, 1, 0, -1, -2, -3', True),
    (3, 1, '3, 2, 1', True),
    (0, 0, '0', True),
    (-2, -4, '-2, -3, -4', True),
    (7, 7, '7', True),

    # Hidden Testcases
    (72, -24, '8a54a5e4635f0fdbecf8523527bd7f5f0f9c7319b66c93612297276c1abe8825', False),
    (-24, -24, '628eee823448ed34c634b578436a53dcbb6559f18b696db721fb25ab0aa1fb4b', False),
    (72, 72, '8722616204217eddb39e7df969e0698aed8e599ba62ed2de1ce49b03ade0fede', False),
    (-20, -24, '6e3e9b4bf1c538296a8995dfabde6595bf99eda90884b76f5d11ba176bdd9a97', False),
    (1, -1, 'ee524027694af7f8dbcc38d6059af0347a46af8aa298a25ce6bfe11246d84538', False),
    (10, 7, '7d4be56a32a8b167da87202bc70d4f512a4a3f5acfe73af0524ea981b0a16bb7', False),
    (0, -3, '113fdeb9abaa4adf476b9615e9dfa55a2dbc1f349ba2280abf0dad0b9bb8885a', False),
    (36, 30, '9c6e0c9b98d0bd1cf74b3124330ac314f06738bcc5b1506fca5598ad1853426b', False),
    (4, 2, 'f476763b19fd158fc6fa294704b10489eda540c0175ff2fecd0cc07007543a88', False),
    (15, -15, '102d75608a84c7850a35632ed70a585f1b1c117d8a37ffe97d5ab79570329d06', False),
]


def check_constraints():
    source = inspect.getsource(q1)
    tree = ast.parse(source)

    functions = [
        node for node in ast.walk(tree)
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
    ]
    assert len(functions) == 1 and functions[0].name == "countdown", (
        "Define only countdown(); helper functions are not allowed."
    )

    func = functions[0]
    assert [param.arg for param in func.args.args] == ["start_hour", "end_hour"], (
        "countdown() must take start_hour and end_hour as its two parameters."
    )
    assert not func.args.defaults and not func.args.kw_defaults, (
        "countdown() must not use extra or default parameters."
    )
    assert not func.args.vararg and not func.args.kwarg and not func.args.kwonlyargs, (
        "countdown() must accept exactly two parameters."
    )

    forbidden = (
        ast.For, ast.AsyncFor, ast.While,
        ast.ListComp, ast.SetComp, ast.DictComp, ast.GeneratorExp,
        ast.Global, ast.Nonlocal,
    )
    assert not any(isinstance(node, forbidden) for node in ast.walk(func)), (
        "Use recursion without loops, comprehensions, or global variables."
    )
    assert any(
        isinstance(node, ast.Call)
        and isinstance(node.func, ast.Name)
        and node.func.id == "countdown"
        for node in ast.walk(func)
    ), "countdown() must call itself recursively."


@pytest.mark.parametrize(
    "start_hour, end_hour, expected, visible",
    CASES,
    ids=[f"{'visible' if item[3] else 'hidden'}-{i:02d}" for i, item in enumerate(CASES, 1)],
)
def test_q1(capsys, start_hour, end_hour, expected, visible):
    check_constraints()
    result = q1.countdown(start_hour, end_hour)
    assert result is None, "countdown() must print and return None."

    printed = capsys.readouterr().out
    if printed.endswith("\n"):
        printed = printed[:-1]

    assert "\n" not in printed and "\r" not in printed, (
        "Print all the numbers on a single line."
    )
    if visible:
        assert printed == expected, f"Expected {expected!r}; printed {printed!r}."
    else:
        actual_hash = hashlib.sha256(printed.encode("utf-8")).hexdigest()
        assert actual_hash == expected, "Incorrect output for this hidden test case."
