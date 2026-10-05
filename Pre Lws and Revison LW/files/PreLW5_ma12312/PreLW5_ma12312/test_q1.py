import pytest
import hashlib
import inspect
import ast
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

import q1


def hashcode(value):
    return hashlib.sha256(str(value).encode("utf-8")).hexdigest()


def normalized_output(output):
    body = output.rstrip("\n")
    if not body:
        return ""
    return "\n".join(line.rstrip() for line in body.splitlines())


q1_testcases = [
    # Visible Testcases
    ((4,), '****\n****\n****\n****', True),
    ((1,), '*', True),
    ((3,), '***\n***\n***', True),

    # Hidden Testcases
    ((2,), '93cf69f87ae3ce87b757a82e5edcf1049b8cba1acea2c2e58c243080d6f25356', False),
    ((5,), 'e2fc551a99b3a6a1c450da8bd97eeda6db06a7cad11f607a3ed8305ee1e32fa5', False),
    ((6,), '071d6e914132321bd826e80c0d4e52fa4e0bb8f7fa58ee99b4f7e7569e91d439', False),
    ((7,), 'd7632d15cc5b5edcf28ccdc64281a4929037381d8cebfd72a7f14c187559b107', False),
    ((8,), 'c703ba0602014af5dde8655f95565cf56926709ad3d9b8987148274c2e14b3f5', False),
    ((9,), '3305ee291a7603a61548604af7362de8636923d1d015e9a8deb652bafa50ef95', False),
    ((10,), 'e2a5bc065bcb0147094bb299f1651862044f562d7d9c03e97f0d5b95d2cecc17', False),
    ((11,), 'f56c908f28a4f2c3ea005714a358f4fb7460e2fd397a2dc65b93fa28ed457b8a', False),
    ((12,), '6d7a1324f87a7b3d2d323f93f469aaf935a3dc04466e7eb74309304b1920319c', False),
    ((13,), '26391693db7e3f65ea60bb0ad9515f27a0724701ab9ff3dfe483d4bed42b7f5f', False),
    ((14,), 'fbb9125d870439eb339fdc2dc30a0f9b4c7d0097dfd271767a5721dbdbca6abb', False),
    ((15,), '27df5fc7ae45921a60fa7c498af02c523f991c9dbb06a2581b90fb769b3aac8a', False),
]


@pytest.mark.parametrize("arguments, result, testcase", q1_testcases)
def test_q1(capsys, arguments, result, testcase):
    q1.square_pattern(*arguments)
    actual = normalized_output(capsys.readouterr().out)

    if testcase:
        assert actual == result
    else:
        assert hashcode(actual) == result


def test_q1_uses_nested_iteration():
    tree = ast.parse(inspect.getsource(q1.square_pattern))
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

    assert has_nested_loop, "square_pattern must use nested iteration."


def test_q1_no_row_generation_shortcuts():
    source = inspect.getsource(q1.square_pattern)
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
