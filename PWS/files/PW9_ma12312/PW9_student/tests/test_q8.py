import ast
import hashlib
import io
import os
import re
import sys
from copy import deepcopy

import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import q8


CASES = [
    (2, 2, 1, 4, [[1, 2], [3, 4]], [[1, 2, 3, 4]], True),
    (2, 2, 2, 4, [[1, 2], [3, 4]], [[1, 2], [3, 4]], True),
    (2, 3, 3, 2, [[1, 2, 3], [4, 5, 6]], [[1, 2], [3, 4], [5, 6]], True),
    (2, 2, 2, 3, [[1, 2], [3, 4]], [[1, 2], [3, 4]], True),
    (1, 5, 5, 1, [[1, 2, 3, 4, 5]], [[1], [2], [3], [4], [5]], True),
    (4, 1, 1, 4, [[1], [2], [3], [4]], [[1, 2, 3, 4]], True),
    (3, 4, 2, 6, [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12]], True),
    (2, 3, 2, 3, [[1, 2, 3], [4, 5, 6]], 'b0d244a98007cfce609156c97fedc8f7107fa4679f8c86ae0f40e63eb0605f2f', False),
    (1, 1, 1, 1, [[42]], '521488a321ba20132908087a5cfa920bd098afadef61d84ea0de2f7e8783f021', False),
    (2, 4, 3, 3, [[1, 2, 3, 4], [5, 6, 7, 8]], '04f88c3784d0b5b7945232f20b3ba6581a6c339f6fe4834c3924ec127b881696', False),
    (4, 3, 2, 6, [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]], '8a4c6fcfe2e30d1e066f40ce44320e38007cf5c8ce7a0845d77ca355644cc86f', False),
    (10, 10, 5, 20, [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16, 17, 18, 19, 20], [21, 22, 23, 24, 25, 26, 27, 28, 29, 30], [31, 32, 33, 34, 35, 36, 37, 38, 39, 40], [41, 42, 43, 44, 45, 46, 47, 48, 49, 50], [51, 52, 53, 54, 55, 56, 57, 58, 59, 60], [61, 62, 63, 64, 65, 66, 67, 68, 69, 70], [71, 72, 73, 74, 75, 76, 77, 78, 79, 80], [81, 82, 83, 84, 85, 86, 87, 88, 89, 90], [91, 92, 93, 94, 95, 96, 97, 98, 99, 100]], '9e2bd386d41f3bfdd771cb958e2ca3d498ba9eb64035d62badb959c91fa0c63f', False),
    (2, 3, 1, 6, [[-1000, 0, 7], [999, -8, 0]], '56135da70f8429da22b63414ee7a0c4dcaccbdba8d5ee717a3df011724331da8', False),
    (100, 100, 40, 250, 'large-pattern', 'cf3cbaf3616f2dd39c8aaa08dfa0e76834b6a5665f8c70b6a151af70447ef42f', False),
    (1, 1, 1, 300, [[42]], '521488a321ba20132908087a5cfa920bd098afadef61d84ea0de2f7e8783f021', False),
]


def make_matrix(rows):
    if rows == "large-pattern":
        return [[((r * 100 + c) % 2001) - 1000 for c in range(100)] for r in range(100)]
    return deepcopy(rows)


def check_matrix(actual, expected, visible):
    assert isinstance(actual, list), "matrixReshape() must return a nested list."
    assert all(isinstance(row, list) for row in actual), "Each matrix row must be a list."
    assert all(type(value) is int for row in actual for value in row), (
        "Matrix entries must be integers."
    )
    if visible:
        assert actual == expected, f"Expected {expected}, got {actual}."
    else:
        actual_hash = hashlib.sha256(str(actual).encode("utf-8")).hexdigest()
        assert actual_hash == expected, "Incorrect matrix for this hidden test case."


def get_printed_matrix(stdout):
    match = re.search(r"(\[\s*\[[\[\],\d\s-]*\]\s*\])\s*$", stdout)
    assert match is not None, "main() must print the resulting nested list."
    try:
        result = ast.literal_eval(match.group(1))
    except (ValueError, SyntaxError) as error:
        pytest.fail(f"main() did not print a valid nested list: {error}")
    return result


def run_main(monkeypatch, capsys, data):
    stream = io.StringIO(data)

    def compatible_input(prompt=""):
        if prompt:
            print(prompt, end="")
        line = stream.readline()
        if not line:
            raise EOFError("main() read more input than expected.")
        return line.rstrip("\r\n")

    with monkeypatch.context() as patch:
        patch.setattr("builtins.input", compatible_input)
        patch.setattr(sys, "stdin", stream)
        q8.main()
    stdout = capsys.readouterr().out
    assert not stream.read().strip(), "main() did not consume the required matrix rows."
    return get_printed_matrix(stdout)


@pytest.mark.parametrize(
    "m, n, r, c, rows, expected, visible",
    CASES,
    ids=[f"{'visible' if case[6] else 'hidden'}-{i:02d}" for i, case in enumerate(CASES, 1)],
)
def test_q8(monkeypatch, capsys, m, n, r, c, rows, expected, visible):
    original = make_matrix(rows)
    before = deepcopy(original)

    result = q8.matrixReshape(original, r, c)
    check_matrix(result, expected, visible)
    assert original == before, "matrixReshape() must not modify the input matrix."

    lines = [f"{m} {n} {r} {c}"] + [",".join(map(str, row)) for row in before]
    input_text = "\n".join(lines) + "\n"
    printed = run_main(monkeypatch, capsys, input_text)
    check_matrix(printed, expected, visible)

    calls = []
    marker = [[314159265, -271828182]]

    def spy(actual_mat, actual_r, actual_c):
        calls.append((deepcopy(actual_mat), actual_r, actual_c))
        return marker

    with monkeypatch.context() as patch:
        patch.setattr(q8, "matrixReshape", spy)
        displayed = run_main(patch, capsys, input_text)

    assert len(calls) == 1, "main() must call matrixReshape() exactly once."
    got_mat, got_r, got_c = calls[0]
    assert got_mat == before, "main() must pass the parsed matrix to matrixReshape()."
    assert all(type(v) is int for row in got_mat for v in row), (
        "main() must convert the input entries to integers."
    )
    assert (got_r, got_c) == (r, c), "main() must pass the requested dimensions as integers."
    assert type(got_r) is int and type(got_c) is int, "r and c must be integers."
    assert displayed == marker, "main() must print the value returned by matrixReshape()."