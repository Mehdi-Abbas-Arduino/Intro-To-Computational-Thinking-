import hashlib
import io
import os
import re
import sys
from copy import deepcopy

import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import q7


CASES = [
    ([
        [0, 0, 0, 0],
        [0, 0, 0, 1],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 0],
    ], 5, True),

    ([
        [1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1],
    ], 8, True),

    ([
        [0, 1],
        [0, 1],
    ], 1, True),

    ([
        [0, 0, 0, 0],
        [0, 1, 0, 1],
        [0, 0, 0, 0],
    ], 'd4735e3a265e16eee03f59718b9b5d03019c07d8b6c51f90da3a666eec13ab35', False),

    ([
        [1, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 1],
    ], 'e7f6c011776e8db7cd330b54174fd76f7d0216b612387a5ffcfb81e6f0919683', False),

    ([
        [0, 0, 1],
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        [1, 0, 0],
    ], 'e7f6c011776e8db7cd330b54174fd76f7d0216b612387a5ffcfb81e6f0919683', False),

    ([
        [1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1],
    ], '2c624232cdd221771294dfbb310aca000a0df6ac8b66b696d90ef06fdefb64a3', False),

    ([
        [0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0],
    ], '2c624232cdd221771294dfbb310aca000a0df6ac8b66b696d90ef06fdefb64a3', False),

    ([
        [1, 0],
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 1],
    ], '7902699be42c8a8e46fbbb4501726517e86b22c56a189f7625a6da49081b2451', False),

    ([
        [1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1],
    ], '2c624232cdd221771294dfbb310aca000a0df6ac8b66b696d90ef06fdefb64a3', False),

    ([
        [1, 1],
        [0, 0],
    ], '6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b', False),

    ([
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ], '19581e27de7ced00ff1ce50b2047e7a567c76b1cbaebabe5ef03f7c3017bb5b7', False),

    ([
        [0, 1],
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 1],
    ], '19581e27de7ced00ff1ce50b2047e7a567c76b1cbaebabe5ef03f7c3017bb5b7', False),

    ([
        [1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1],
    ], '7902699be42c8a8e46fbbb4501726517e86b22c56a189f7625a6da49081b2451', False),

    ([
        [0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0],
    ], '8527a891e224136950ff32ca212b45bc93f69fbb801c3b1ebedac52775f99e61', False),

]


def check_result(actual, expected, visible):
    assert type(actual) is int, "rectangular_distance() must return an integer."
    if visible:
        assert actual == expected, f"Expected distance {expected}, got {actual}."
    else:
        digest = hashlib.sha256(str(actual).encode("utf-8")).hexdigest()
        assert digest == expected, "Incorrect distance for this hidden test case."


def run_main(monkeypatch, capsys, grid):
    n, m = len(grid), len(grid[0])
    input_lines = [f"{n} {m}"] + ["".join(map(str, row)) for row in grid]
    stream = io.StringIO("\n".join(input_lines) + "\n")

    def mock_input(prompt=""):
        line = stream.readline()
        if line == "":
            raise EOFError("main() requested too many input lines.")
        return line.rstrip("\r\n")

    with monkeypatch.context() as patch:
        patch.setattr("builtins.input", mock_input)
        patch.setattr(sys, "stdin", stream)
        q7.main()

    output = capsys.readouterr().out
    assert stream.read().strip() == "", "main() did not read all input rows."
    match = re.search(r"(?<!\d)(-?\d+)\s*$", output)
    assert match is not None, "main() must print the returned integer distance."
    return int(match.group(1))


@pytest.mark.parametrize(
    "grid, expected, visible",
    CASES,
    ids=[f"{'visible' if case[2] else 'hidden'}-{i:02d}" for i, case in enumerate(CASES, 1)],
)
def test_q7(monkeypatch, capsys, grid, expected, visible):
    original = deepcopy(grid)

    result = q7.rectangular_distance(grid)
    check_result(result, expected, visible)
    assert grid == original, "rectangular_distance() must not modify grid."

    displayed = run_main(monkeypatch, capsys, original)
    check_result(displayed, expected, visible)

    calls = []
    marker = 314159265

    def spy(actual_grid):
        calls.append(deepcopy(actual_grid))
        return marker

    with monkeypatch.context() as patch:
        patch.setattr(q7, "rectangular_distance", spy)
        printed = run_main(patch, capsys, original)

    assert calls == [original], (
        "main() must call rectangular_distance() once with the parsed integer grid."
    )
    assert printed == marker, "main() must print the helper's returned distance."