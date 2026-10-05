import pytest
import hashlib
import inspect
import ast
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

import q2


def hashcode(value):
    return hashlib.sha256(str(value).encode("utf-8")).hexdigest()


def normalized_output(output):
    body = output.rstrip("\n")
    if not body:
        return ""
    return "\n".join(line.rstrip() for line in body.splitlines())


q2_testcases = [
    # Visible Testcases
    ((3, 5), '*****\n*****\n*****', True),
    ((1, 4), '****', True),
    ((4, 1), '*\n*\n*\n*', True),

    # Hidden Testcases
    ((1, 1), '684888c0ebb17f374298b65ee2807526c066094c701bcc7ebbe1c1095f494fc1', False),
    ((2, 2), '93cf69f87ae3ce87b757a82e5edcf1049b8cba1acea2c2e58c243080d6f25356', False),
    ((2, 5), 'bc201daa7ff7cd260edc23965fc86743b1d4be649d5a57250fc3304b751238e1', False),
    ((5, 2), '70b9da103f8d9ce92e3562ca3858a2f9c639c53dff3d6cfff7f6bedd27e23047', False),
    ((4, 6), '978afe1b1b309e2408150070e1728fc28e3049caa86d43fa6e193b2e0c69e790', False),
    ((6, 4), '8766a9603c51ff267a19bbb107bec95bca8bcb674b516e5190aa1fc100249dfb', False),
    ((3, 1), 'a81d52fdc419cf6fdd8cfc3f22b2912795b678e137285091d806a3e8cadb3b3a', False),
    ((1, 7), 'eb0f08df4490a936686900f130b51868a6f7a9ae73ac4fd4386660b2c3003a48', False),
    ((7, 1), '5f1a2a8d8a5278f6717f395d1c52d9c8890f42c19aaf33dd8fc04009d1647611', False),
    ((5, 5), 'e2fc551a99b3a6a1c450da8bd97eeda6db06a7cad11f607a3ed8305ee1e32fa5', False),
    ((2, 8), 'dccaec1de03af8299877b9db88329dc73da7590c0ae925fe71f5cc0ab636fe06', False),
    ((8, 2), '592d810da542582525b8c1dc940176a02d1f2eb974ae0fd2c8a55b77e47953d0', False),
]


@pytest.mark.parametrize("arguments, result, testcase", q2_testcases)
def test_q2(capsys, arguments, result, testcase):
    q2.rectangle_pattern(*arguments)
    actual = normalized_output(capsys.readouterr().out)

    if testcase:
        assert actual == result
    else:
        assert hashcode(actual) == result


def test_q2_uses_nested_iteration():
    tree = ast.parse(inspect.getsource(q2.rectangle_pattern))
    loops = (ast.For, ast.While)

    has_nested_loop = any(
        isinstance(node, loops)
        and any(
            isinstance(child, loops)
            for child in ast.walk(node)
            if child is not node
        )
        for node in ast.walk(tree)
    )

    assert has_nested_loop, "rectangle_pattern must use nested iteration."


def test_q2_no_row_generation_shortcuts():
    source = inspect.getsource(q2.rectangle_pattern)
    tree = ast.parse(source)

    string_names = set()

    changed = True
    while changed:
        changed = False
        for node in ast.walk(tree):
            value = None
            targets = []

            if isinstance(node, ast.Assign):
                value = node.value
                targets = node.targets
            elif isinstance(node, ast.AnnAssign):
                value = node.value
                targets = [node.target]

            if value is None:
                continue

            is_string = (
                isinstance(value, ast.Constant) and isinstance(value.value, str)
            ) or (
                isinstance(value, ast.Name) and value.id in string_names
            )

            if is_string:
                for target in targets:
                    if isinstance(target, ast.Name) and target.id not in string_names:
                        string_names.add(target.id)
                        changed = True

    def is_string_expression(node):
        return (
            isinstance(node, ast.Constant) and isinstance(node.value, str)
        ) or (
            isinstance(node, ast.Name) and node.id in string_names
        )

    for node in ast.walk(tree):
        if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Mult):
            if is_string_expression(node.left) or is_string_expression(node.right):
                pytest.fail(
                    "Do not use string multiplication to generate repeated pattern characters. "
                    "Use nested iteration."
                )

        if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
            if node.func.attr == "join":
                pytest.fail(
                    "Do not use join() to generate a complete pattern row. "
                    "Use nested iteration."
                )

        if isinstance(node, (ast.ListComp, ast.SetComp, ast.DictComp, ast.GeneratorExp)):
            pytest.fail(
                "Do not use comprehensions or generator expressions to generate pattern rows. "
                "Use explicit nested iteration."
            )
