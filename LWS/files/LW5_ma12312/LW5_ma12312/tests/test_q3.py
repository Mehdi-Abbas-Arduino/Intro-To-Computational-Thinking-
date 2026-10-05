import pytest
import hashlib
import inspect
import ast
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from q3 import *


def normalize_output(output):
    return "\n".join(line.rstrip() for line in output.rstrip("\n").splitlines())


def hashcode(value):
    return hashlib.sha256(str(value).encode("utf-8")).hexdigest()


q3_testcases = [
    # Visible Testcases
    (3, "1\n1 2 1\n1 2 4 2 1", True),
    (1, "1", True),
    (2, "1\n1 2 1", True),
    (6, "1\n1 2 1\n1 2 4 2 1\n1 2 4 8 4 2 1\n1 2 4 8 16 8 4 2 1\n1 2 4 8 16 32 16 8 4 2 1", True),

    # Hidden Testcases
    (4, "345b70da48ed7924f3a50bb817bbbc876c9f806cf893c0542b6febe7c683682a", False),
    (5, "15001877a305d4d3fee4d2da42d5fccc1bf047f026e9780722dd159d6b988a06", False),
    (10, "8627e05ad6a62a29b84cd0e146387580a3686e03e5aca6d10923a02849c99eb8", False),
    (20, "bd4a1953f3ea428ec5c698fe692fafba757c8d16808b2ff56ab3d2b5cfdc751c", False),
    (30, "b589f2614986184a9503bb57c9d56e45e914f0b78903608b5a24d310e1c2b23a", False),
]


@pytest.mark.parametrize("row_count, result, testcase", q3_testcases)
def test_q3(capsys, row_count, result, testcase):
    power_pyramid(row_count)
    actual = normalize_output(capsys.readouterr().out)
    if testcase:
        assert actual == result
    else:
        assert hashcode(actual) == result


def test_q3_uses_nested_iteration():
    tree = ast.parse(inspect.getsource(power_pyramid))
    loops = (ast.For, ast.While)
    assert any(isinstance(n, loops) and any(isinstance(c, loops) for c in ast.walk(n) if c is not n) for n in ast.walk(tree))
