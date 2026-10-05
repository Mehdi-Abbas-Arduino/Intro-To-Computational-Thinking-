import pytest
import hashlib
import inspect
import ast
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from q4 import print_scoreboard_alignment


def normalize_output(output):
    return "\n".join(line.rstrip() for line in output.rstrip("\n").splitlines())


def hashcode(value):
    return hashlib.sha256(str(value).encode("utf-8")).hexdigest()


def _has_nested_iteration(function):
    tree = ast.parse(inspect.getsource(function))
    loops = (ast.For, ast.While)
    return any(
        isinstance(node, loops)
        and any(
            isinstance(child, loops)
            for child in ast.walk(node)
            if child is not node
        )
        for node in ast.walk(tree)
    )


def _assert_no_string_multiplication(source):
    tree = ast.parse(source)
    string_names = set()

    changed = True
    while changed:
        changed = False
        for node in ast.walk(tree):
            if isinstance(node, (ast.Assign, ast.AnnAssign)):
                value = node.value
                targets = node.targets if isinstance(node, ast.Assign) else [node.target]
                is_string_value = (
                    isinstance(value, ast.Constant) and isinstance(value.value, str)
                ) or (
                    isinstance(value, ast.Name) and value.id in string_names
                )
                if is_string_value:
                    for target in targets:
                        if isinstance(target, ast.Name) and target.id not in string_names:
                            string_names.add(target.id)
                            changed = True

    def is_string_operand(node):
        return (
            isinstance(node, ast.Constant) and isinstance(node.value, str)
        ) or (
            isinstance(node, ast.Name) and node.id in string_names
        )

    for node in ast.walk(tree):
        if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Mult):
            if is_string_operand(node.left) or is_string_operand(node.right):
                pytest.fail("Do not use string multiplication to generate repeated output.")


q4_testcases = [
    (5, '0 1 2 3 4 5\n  0 1 2 3 4\n    0 1 2 3\n      0 1 2\n        0 1', True),
    (1, '0 1', True),
    (2, '0 1 2\n  0 1', True),
    (3, '615a5d9a11b70556e642708d6fc564ad84d736112fa0d213c7283fc94b093f9f', False),
    (4, '9562a8473ab58b14482e72e18a626283109fc4f0016a35007c68116011ec53c1', False),
    (6, 'b75b1eaa478c4b9333a1281749fc7cebee949c370fd385a9c4e2a476482e346e', False),
    (7, '7bcc51022731adec14bc4fab16dc323fca846fa143e431051b8d8ee6ec5554b4', False),
    (8, '5fa45ca5ab15f429fdbb2c07d39c74f69ce5967221cbca69a000099e048194c5', False),
    (9, '3aedcde9dfbda8cf8ce72c91e34b0ca115262448ba0dc2d5f269ddabf560f1bc', False),
]


@pytest.mark.parametrize("max_number, result, visible", q4_testcases)
def test_q4(capsys, max_number, result, visible):
    print_scoreboard_alignment(max_number)
    actual = normalize_output(capsys.readouterr().out)
    if visible:
        assert actual == result
    else:
        assert hashcode(actual) == result


def test_q4_uses_nested_iteration():
    assert _has_nested_iteration(print_scoreboard_alignment), \
        "print_scoreboard_alignment must use nested iteration."


def test_q4_no_string_multiplication():
    _assert_no_string_multiplication(inspect.getsource(print_scoreboard_alignment))
