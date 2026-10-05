import pytest
import hashlib
import inspect
import ast
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from q5 import print_inverted_number_triangle


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


q5_testcases = [
    (5, '5 5 5 5 5\n 4 4 4 4\n  3 3 3\n   2 2\n    1', True),
    (3, '3 3 3\n 2 2\n  1', True),
    (1, '1', True),
    (2, 'a223f294f582b18e34c90eac27bfe320fc388ef4bf22ee95a9dd66a147f946c1', False),
    (4, '68754a3c81d2049f6fe3fe22f5bb383e48c501d02df6697d21b49001a67e5afc', False),
    (6, 'ad54ea9bdca03524861178806a4c7402dd01a29098da3f668e0112e8065eeb98', False),
    (7, 'e1aedc9a0f1ab6ccbc914ba34d87a61c75e3789cf9f1e31e61b329ef30e535d8', False),
    (8, '3e9f98fea7d06b746f3d6e853d172258a56d7721024364f0999ef7389a08f666', False),
    (9, '99d8918ee7447b3617f0f7dc95c236c53c01be35201f999856348a51da198347', False),
]


@pytest.mark.parametrize("row_count, result, visible", q5_testcases)
def test_q5(capsys, row_count, result, visible):
    print_inverted_number_triangle(row_count)
    actual = normalize_output(capsys.readouterr().out)
    if visible:
        assert actual == result
    else:
        assert hashcode(actual) == result


def test_q5_uses_nested_iteration():
    assert _has_nested_iteration(print_inverted_number_triangle), \
        "print_inverted_number_triangle must use nested iteration."


def test_q5_no_string_multiplication():
    _assert_no_string_multiplication(inspect.getsource(print_inverted_number_triangle))
