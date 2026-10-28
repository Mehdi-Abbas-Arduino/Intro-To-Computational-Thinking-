import ast
import hashlib
import inspect
import os
import sys

import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import q6


CASES = [
    # Visible Testcases
    ([2, 3, 4, 0, 1], 3, [None, None, None, None, None], True),
    ([2, 0, 1, 4, 3], 4, [2, 0, 1, None, None], True),
    ([0], 0, [None], True),
    ([2, 0, 1], 0, [None, None, None], True),
    ([2, 0, 1, 0, 1], 2, [None, None, None, 0, 1], True),

    # Hidden Testcases
    ([2, 0, 3, 6, 5, 1, 4], 0, '7948ef61f04a882affbb70be61a3778d938f4c925ef635d6ee3f7610a32f7b26', False),
    ([2, 0, 3, 6, 5, 1, 4], 6, '7948ef61f04a882affbb70be61a3778d938f4c925ef635d6ee3f7610a32f7b26', False),
    ([7, 3, 6, 2, 0, 9, 1, 8, 5, 10, 4], 3, 'ddab5fd04a28a8f32d16196fee92b84dc72fa4d07aca06a1a07bb9050faa9bb7', False),
    ([7, 3, 6, 2, 0, 9, 1, 8, 5, 10, 4], 5, 'dda9aca88fb2ced938a6dade7627e6225fcb51ea5877ef68762741b2061fd165', False),
    ([2, 0, 3, 6, 4, 1, 4], 5, '7948ef61f04a882affbb70be61a3778d938f4c925ef635d6ee3f7610a32f7b26', False),
    ([1, 1, 2, 3, 4], 4, '162335f6476d9f2deb17ac6e78c329f3bfc48a488436641f82100113349b0c33', False),
    ([1, 0, 3, 2, 5, 4], 4, 'c4f29ee72ba39fc5592fabebd198d942eaa3b27a6280184d73c15d612e49ea00', False),
    ([2, 2, 3, 4, 5, 3, 0], 0, 'ca6ebcb487d92e85431d01ec189ddfb61095d31e09608935c14de026bcc72d49', False),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 9], 0, '466b61a480a30daf1370013a8aa338b6087de6cf224ebd7636cfee204280081b', False),
    ([
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
        11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
        21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
        31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
        41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
        51, 52, 53, 54, 55, 56, 57, 58, 59, 60,
        61, 62, 63, 64, 65, 66, 67, 68, 69, 70,
        71, 72, 73, 74, 75, 76, 77, 78, 79, 80,
        81, 82, 83, 84, 85, 86, 87, 88, 89, 90,
        91, 92, 93, 94, 95, 96, 97, 98, 99, 99
    ], 0, 'b7e993a2b2ec8282da3ac30a99b7edb71f77ac28fde7f019c4fbe0501952542b', False),
]


def check_constraints():
    tree = ast.parse(inspect.getsource(q6))
    functions = [
        node for node in ast.walk(tree)
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
    ]
    assert len(functions) == 1 and functions[0].name == "visit", (
        "Define only visit(clues, position); helper functions are not allowed."
    )

    function = functions[0]
    assert [arg.arg for arg in function.args.args] == ["clues", "position"], (
        "Use the required parameters: clues and position."
    )
    assert not (
        function.args.defaults or function.args.kw_defaults or
        function.args.vararg or function.args.kwarg or
        function.args.kwonlyargs or function.args.posonlyargs
    ), "visit() must take exactly two ordinary parameters."

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
        and node.func.id == "visit"
        for node in ast.walk(function)
    ), "visit() must call itself recursively."


@pytest.mark.parametrize(
    "clues, position, expected, visible",
    CASES,
    ids=[f"{'visible' if c[3] else 'hidden'}-{i:02d}" for i, c in enumerate(CASES, 1)],
)
def test_q6(capsys, clues, position, expected, visible):
    check_constraints()
    result = q6.visit(clues, position)
    assert result is None, "visit() must return None (and modify clues in place)."
    assert capsys.readouterr().out == "", "visit() must not print anything."

    if visible:
        assert clues == expected, f"Expected modified clues {expected!r}; got {clues!r}."
    else:
        digest = hashlib.sha256(str(clues).encode("utf-8")).hexdigest()
        assert digest == expected, "Incorrect visited/unvisited clues in this hidden case."
