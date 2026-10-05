import pytest
import hashlib
import inspect
import ast
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from q2 import *


def normalize_output(output):
    return "\n".join(line.rstrip() for line in output.rstrip("\n").splitlines())


def hashcode(value):
    return hashlib.sha256(str(value).encode("utf-8")).hexdigest()


q2_testcases = [
    # Visible Testcases
    (2, "1\n3 5", True),
    (3, "1\n3 5\n7 9 11", True),
    (5, "1\n3 5\n7 9 11\n13 15 17 19\n21 23 25 27 29", True),

    # Hidden Testcases
    (1, "6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b", False),
    (4, "c4da137c2b0c70fc119b5c777ce9335587126b86db471bbfa5bb40a442b323cd", False),
    (6, "042d76fa1abf21b26133f69c64bcd968351adfbb14116d3155729366f299eaa6", False),
    (8, "0578e1529abe11f87e12d3651630074fe62a7bef5e7e88f33d150dd895275238", False),
    (10, "f6d60a036337b7c1b0ed276a82b596e39b77b6dc68adb39392620163c4d58b73", False),
]


@pytest.mark.parametrize("row_count, result, testcase", q2_testcases)
def test_q2(capsys, row_count, result, testcase):
    print_odd_staircase(row_count)
    actual = normalize_output(capsys.readouterr().out)
    if testcase:
        assert actual == result
    else:
        assert hashcode(actual) == result


def test_q2_uses_nested_iteration():
    tree = ast.parse(inspect.getsource(print_odd_staircase))
    loops = (ast.For, ast.While)
    assert any(isinstance(n, loops) and any(isinstance(c, loops) for c in ast.walk(n) if c is not n) for n in ast.walk(tree))
