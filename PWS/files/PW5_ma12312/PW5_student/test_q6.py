import pytest
import hashlib
import inspect
import ast
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

import q6


def normalize_output(output):
    lines = output.rstrip("\n").split("\n")
    return "\n".join(line.rstrip() for line in lines)


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


q6_testcases = [
    (5, '    *\n   ***\n  *****\n *******\n*********\n *******\n  *****\n   ***\n    *', True),
    (4, '   *\n  ***\n *****\n*******\n *****\n  ***\n   *', True),
    (1, '684888c0ebb17f374298b65ee2807526c066094c701bcc7ebbe1c1095f494fc1', False),
    (2, 'ad80826a757d1cf74decfe31a1c05f8b15d7de898aefe7fb0c8c6e8e26d03782', False),
    (3, 'e88fb8f692ca0c78ad0389a89acd5a0b8c1c0c924d0f0576cc33158f2b1dff67', False),
    (6, '17255215212f2a39aa20120d5fddc888d9797a692c9569d1ad7374477d31718b', False),
    (7, '5093d7232a4a95317cf4af208cff041a3f84fd038dbf9f3b1df2b27c8e981bd6', False),
    (8, 'f4b653e89848a0c9c9ae49924f724caaee05a0fd1680671f32d20224baf27f45', False),
    (9, '3a98ae5a1a494b10b9c314d760826b251cafd635a61334bb279c260bc6e901b2', False),
    (10, '19a0eeec2d184edfd293d4ccd0054ea4b8957170f4d02a432db0fa6ee3297ef0', False),
]


@pytest.mark.parametrize("size, result, visible", q6_testcases)
def test_q6(capsys, size, result, visible):
    q6.print_diamond(size)
    actual = normalize_output(capsys.readouterr().out)
    if visible:
        assert actual == result
    else:
        assert hashcode(actual) == result


def test_q6_helper_outputs(capsys):
    q6.print_upper_diamond(3)
    assert normalize_output(capsys.readouterr().out) == "  *\n ***\n*****"

    q6.print_lower_diamond(3)
    assert normalize_output(capsys.readouterr().out) == " ***\n  *"


def test_q6_structure():
    assert hasattr(q6, "print_upper_diamond")
    assert hasattr(q6, "print_lower_diamond")
    assert hasattr(q6, "print_diamond")
    assert len(inspect.signature(q6.print_upper_diamond).parameters) == 1
    assert len(inspect.signature(q6.print_lower_diamond).parameters) == 1
    assert len(inspect.signature(q6.print_diamond).parameters) == 1

    source = inspect.getsource(q6.print_diamond)
    tree = ast.parse(source)
    calls = {
        node.func.id
        for node in ast.walk(tree)
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name)
    }
    assert "print_upper_diamond" in calls and "print_lower_diamond" in calls, \
        "print_diamond must call both helper functions."


def test_q6_helpers_use_nested_iteration():
    assert _has_nested_iteration(q6.print_upper_diamond), \
        "print_upper_diamond must use nested iteration."
    assert _has_nested_iteration(q6.print_lower_diamond), \
        "print_lower_diamond must use nested iteration."


def test_q6_no_string_multiplication():
    _assert_no_string_multiplication(inspect.getsource(q6))
