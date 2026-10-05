import pytest
import hashlib
import inspect
import ast
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from q4 import *


def normalize_output(output):
    return "\n".join(line.rstrip() for line in output.rstrip("\n").splitlines())


def hashcode(value):
    return hashlib.sha256(str(value).encode("utf-8")).hexdigest()


q4_testcases = [
    # Visible Testcases
    (5, "5 4 3 2 1\n  4 3 2 1\n    3 2 1\n      2 1\n        1", True),
    (1, "1", True),
    (2, "2 1\n  1", True),

    # Hidden Testcases
    (3, "071bc31d5f7bf54fc1dd3fcfef676636944c0990ce3ee27f92d825358f648c2e", False),
    (4, "63d36eced9ff34b7f81a2fe5e7d7aa5752193dbb98832923f66a9a4e3fccec70", False),
    (6, "4c37e92d14a4f598962e8e746d76488c159b3cc83cf94b8b5a5992036876ab48", False),
    (7, "c19bbddf008e6403fc1e9b64530a11e25a8a23720cc5cef23dbd5e14d02545f3", False),
    (8, "f0666ab41c2d544a2ca1b5d4b2354ee7916b632b1ac1adf902227ed6bd55bca9", False),
    (9, "23d503d25971199b28f9fd959b752e86ac35096e4b5819a9d0055eaec1ec08c3", False),
]


@pytest.mark.parametrize("start_value, result, testcase", q4_testcases)
def test_q4(capsys, start_value, result, testcase):
    countdown_pattern(start_value)
    actual = normalize_output(capsys.readouterr().out)
    if testcase:
        assert actual == result
    else:
        assert hashcode(actual) == result


def test_q4_uses_nested_iteration():
    tree = ast.parse(inspect.getsource(countdown_pattern))
    loops = (ast.For, ast.While)
    assert any(isinstance(n, loops) and any(isinstance(c, loops) for c in ast.walk(n) if c is not n) for n in ast.walk(tree))


def test_q4_no_string_multiplication():
    tree = ast.parse(inspect.getsource(countdown_pattern))

    string_variables = set()

    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            if isinstance(node.value, ast.Constant) and isinstance(node.value.value, str):
                for target in node.targets:
                    if isinstance(target, ast.Name):
                        string_variables.add(target.id)

        if isinstance(node, ast.AnnAssign):
            if (
                isinstance(node.target, ast.Name)
                and isinstance(node.value, ast.Constant)
                and isinstance(node.value.value, str)
            ):
                string_variables.add(node.target.id)

    changed = True
    while changed:
        changed = False
        for node in ast.walk(tree):
            if isinstance(node, ast.Assign) and isinstance(node.value, ast.Name):
                if node.value.id in string_variables:
                    for target in node.targets:
                        if isinstance(target, ast.Name) and target.id not in string_variables:
                            string_variables.add(target.id)
                            changed = True

    def is_string_value(node):
        if isinstance(node, ast.Constant) and isinstance(node.value, str):
            return True
        if isinstance(node, ast.Name):
            return node.id in string_variables
        return False

    for node in ast.walk(tree):
        if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Mult):
            if is_string_value(node.left) or is_string_value(node.right):
                pytest.fail(
                    "Do not use string multiplication to generate repeated spacing or output. "
                    "Use nested iteration instead."
                )

        if isinstance(node, ast.AugAssign) and isinstance(node.op, ast.Mult):
            if is_string_value(node.target):
                pytest.fail(
                    "Do not use string multiplication to generate repeated spacing or output. "
                    "Use nested iteration instead."
                )

