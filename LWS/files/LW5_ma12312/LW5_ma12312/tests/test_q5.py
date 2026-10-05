import pytest
import hashlib
import inspect
import ast
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

import q5


def normalize_output(output):
    return "\n".join(line.rstrip() for line in output.rstrip("\n").splitlines())


def hashcode(value):
    return hashlib.sha256(str(value).encode("utf-8")).hexdigest()


q5_testcases = [
    # Visible Testcases
    (5, "    *\n   ***\n  *****\n *******\n*********", True),
    (4, "   *\n  ***\n *****\n*******", True),

    # Hidden Testcases
    (1, "684888c0ebb17f374298b65ee2807526c066094c701bcc7ebbe1c1095f494fc1", False),
    (2, "bbba59c9634d3aba1accb57d18c053fd141a578072e842e51aad78a9355b2e95", False),
    (3, "f27198ee59485d468c389c36d78862af018f474e23eba6c4d994989567f4952f", False),
    (6, "05562404891e78b03f0b78cf80fab7a257e92fbaef78acb386adaf5122306c7c", False),
    (8, "be84bf6a663b6ea19a92d108acffc1abcdbbc5e608efb2a7547c4f0fcf279603", False),
    (10, "c69d6b2247f7d911694f4d47e0b8a575dd6ab1721f77cbcd5368b14e9b05ce13", False),
]


@pytest.mark.parametrize("size, result, testcase", q5_testcases)
def test_q5(capsys, size, result, testcase):
    q5.stage_light_display(size)
    actual = normalize_output(capsys.readouterr().out)
    if testcase:
        assert actual == result
    else:
        assert hashcode(actual) == result


def test_q5_uses_nested_iteration():
    tree = ast.parse(inspect.getsource(q5.stage_light_display))
    loops = (ast.For, ast.While)
    assert any(isinstance(n, loops) and any(isinstance(c, loops) for c in ast.walk(n) if c is not n) for n in ast.walk(tree))


def test_q5_no_string_multiplication():
    tree = ast.parse(inspect.getsource(q5.stage_light_display))

    string_variables = set()

    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            if isinstance(node.value, ast.Constant) and isinstance(node.value.value, str):
                if node.value.value in {" ", "*"}:
                    for target in node.targets:
                        if isinstance(target, ast.Name):
                            string_variables.add(target.id)

        if isinstance(node, ast.AnnAssign):
            if (
                isinstance(node.target, ast.Name)
                and isinstance(node.value, ast.Constant)
                and isinstance(node.value.value, str)
                and node.value.value in {" ", "*"}
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

    def is_repeated_string(node):
        if isinstance(node, ast.Constant) and isinstance(node.value, str):
            return node.value in {" ", "*"}
        if isinstance(node, ast.Name):
            return node.id in string_variables
        return False

    for node in ast.walk(tree):
        if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Mult):
            if is_repeated_string(node.left) or is_repeated_string(node.right):
                pytest.fail(
                    "Do not use string multiplication to generate spaces or asterisks. "
                    "Use nested iteration instead."
                )