import pytest
import hashlib
import inspect
import ast
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from q1 import *


def normalize_output(output):
    return "\n".join(line.rstrip() for line in output.rstrip("\n").splitlines())


def hashcode(value):
    return hashlib.sha256(str(value).encode("utf-8")).hexdigest()


q1_testcases = [
    # Visible Testcases
    (5, "5\n5 4\n5 4 3\n5 4 3 2\n5 4 3 2 1", True),
    (1, "1", True),
    (2, "2\n2 1", True),

    # Hidden Testcases
    (10, "cb01f696a2a1dad696a6bc137bca4bbef636a26fa92d79910bca97e341325197", False),
    (4, "3650502bf1c1f706200cfd458cb6eb18180a973a2a46f67c34f5b2bcc4583d51", False),
    (20, "7ddebc9f286b411eb53772c0b92397ff8359f2ad866c2e5346a4e354ab83a70b", False),
    (50, "bb4f501057b74e48ba9094e59825778a224aa6c77737d2855c1512ced335a45c", False),
    (80, "25f0a20f65059655c3fa7497816c09118c9fadbc5ed5aeb4595ab5f107e84528", False),
]


@pytest.mark.parametrize("start_value, result, testcase", q1_testcases)
def test_q1(capsys, start_value, result, testcase):
    number_trail(start_value)
    actual = normalize_output(capsys.readouterr().out)
    if testcase:
        assert actual == result
    else:
        assert hashcode(actual) == result


def test_q1_uses_nested_iteration():
    tree = ast.parse(inspect.getsource(number_trail))
    loops = (ast.For, ast.While)
    assert any(isinstance(n, loops) and any(isinstance(c, loops) for c in ast.walk(n) if c is not n) for n in ast.walk(tree))
