import ast
import hashlib
import inspect
import os
import sys

import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import q2


CASES = [
    # Visible Testcases
    (72, 5, [50, 75, 60, 70, 65], 'Attempts remaining: 5\nToo low!\nAttempts remaining: 4\nToo high!\nAttempts remaining: 3\nToo low!\nAttempts remaining: 2\nToo low!\nAttempts remaining: 1\nYou lost!', True),
    (85, 10, [50, 75, 85], 'Attempts remaining: 10\nToo low!\nAttempts remaining: 9\nToo low!\nAttempts remaining: 8\nYou won with 7 attempts remaining.', True),
    (100, 1, [100], 'Attempts remaining: 1\nYou won with 0 attempts remaining.', True),
    (0, 1, [1], 'Attempts remaining: 1\nYou lost!', True),
    (43, 4, [43], 'Attempts remaining: 4\nYou won with 3 attempts remaining.', True),

    # Hidden Testcases
    (0, 1, [0], '18a542db4bc40bdd388e3122660439ad464be205ed581ad85f316ce529c78e5a', False),
    (100, 1, [99], '910d86e7c27444d1328f0e567575ea98497df5276eebcadd4087c580eb5d1cb8', False),
    (37, 4, [50, 20, 37], '6508b38268d8bd437997d19ed19b44b5c9efc072dd8ea481ce2f93828c592ed6', False),
    (37, 4, [50, 20, 40, 37], '863012b8df6c0d9e844a39c751133d817d9835b672d6932bf0fd682b44186187', False),
    (37, 4, [50, 20, 40, 30], '0d2569114c39f0129e6357b26c43841672892965295c313e3cb390a1f0aa3efc', False),
    (73, 7, [50, 75, 63, 69, 72, 74, 73], '4a77d4e1f8e5d8dd167000e688d38631272398172c62de6b6ba12277c1414e8a', False),
    (73, 7, [50, 75, 63, 69, 72, 74, 72], '6a3736b2b1f102128f507967fc901aa5b561852e98fdb59f81e1e10c7707424f', False),
    (49, 19, [48, 49], '2a5010c1d53efde72f56e76e130b895c432f16492766c4bcac6077717c86a07f', False),
    (25, 3, [25], 'be3930f90652ca1df2db3bc0777650ee5b9b7ed0ec22ac39399f210fa9555475', False),
    (20, 10, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], '9db10a072a1d4d7e7d77bb299afd3cbb94a194367c0f986a11536de4bbf132f3', False),
]


def check_constraints():
    tree = ast.parse(inspect.getsource(q2))
    functions = [
        node for node in ast.walk(tree)
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
    ]
    assert len(functions) == 1 and functions[0].name == "guess_midterm_score", (
        "Define only guess_midterm_score(); helper functions are not allowed."
    )

    function = functions[0]
    assert [arg.arg for arg in function.args.args] == [
        "midterm_score", "attempts_left"
    ], "Use the specified midterm_score and attempts_left parameters."
    assert not function.args.defaults and not function.args.kw_defaults, (
        "Do not define default parameters."
    )
    assert not function.args.vararg and not function.args.kwarg, (
        "guess_midterm_score() must take exactly two parameters."
    )
    assert not function.args.kwonlyargs and not function.args.posonlyargs, (
        "guess_midterm_score() must take two ordinary parameters."
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
        and node.func.id == "guess_midterm_score"
        for node in ast.walk(function)
    ), "guess_midterm_score() must call itself recursively."


@pytest.mark.parametrize(
    "midterm_score, attempts_left, guesses, expected, visible",
    CASES,
    ids=[f"{'visible' if c[4] else 'hidden'}-{i:02d}" for i, c in enumerate(CASES, 1)],
)
def test_q2(monkeypatch, capsys, midterm_score, attempts_left, guesses, expected, visible):
    check_constraints()
    calls = []

    def mock_input(prompt=""):
        if len(calls) >= len(guesses):
            pytest.fail("The game requested another guess after it should have ended.")
        result = str(guesses[len(calls)])
        calls.append(result)
        return result

    monkeypatch.setattr("builtins.input", mock_input)
    result = q2.guess_midterm_score(midterm_score, attempts_left)
    assert result is None, "guess_midterm_score() must print and return None."
    assert len(calls) == len(guesses), (
        "The game did not read the expected number of guesses."
    )

    printed = capsys.readouterr().out
    if printed.endswith("\n"):
        printed = printed[:-1]
    if visible:
        assert printed == expected, f"Expected {expected!r}, printed {printed!r}."
    else:
        digest = hashlib.sha256(printed.encode("utf-8")).hexdigest()
        assert digest == expected, "Incorrect output for this hidden test case."