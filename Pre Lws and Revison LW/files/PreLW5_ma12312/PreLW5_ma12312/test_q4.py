import pytest
import hashlib
import inspect
import ast
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

import q4


def hashcode(value):
    return hashlib.sha256(str(value).encode("utf-8")).hexdigest()


def normalized_output(output):
    body = output.rstrip("\n")
    if not body:
        return ""
    return "\n".join(line.rstrip() for line in body.splitlines())


q4_testcases = [
    # Visible Testcases
    ((4,), '*\n**\n***\n****\n***\n**\n*', True),
    ((1,), '*', True),
    ((2,), '*\n**\n*', True),

    # Hidden Testcases
    ((3,), 'a913ca7820da4da13eeecf2e879a6572a062cf5001f4053eee66e83f8607460e', False),
    ((5,), '19a11ab2d5377c18729792a410a84441f0e0e27b90e141eb327b29cdb6876827', False),
    ((6,), 'b43e7aa1963974bb662220983f02485510db69cb77f68a022819b7a37e276c79', False),
    ((7,), '74deae408ac3a25e0bfc738c829f9eea9eca3a0849af27b38160af9d7d929f9f', False),
    ((8,), '39758eb2905a1d08f69b2137ddd99df6bc7502bf0e13b9e69e93730b078695e8', False),
    ((9,), 'af957a70f36d5fde080c96ef0ae4bf1890d79c9a3dd3cf8072953854d368656a', False),
    ((10,), '65e717e688366571869f1e02909c01a81305c78e1b65ac41fd1edc820a5d53de', False),
    ((11,), '25473ef34833d1d97f60222b6c95e4011b3d2cfb963baa3a31e5ed101bffec1c', False),
    ((12,), 'f4a16440231f5276e252afb1d2b66774ac1becec8c5963484f0ebd1e14a18a55', False),
    ((13,), '9416b60d31de4be26e6709dc77d8b183022a96d5e774727fb8cb4644b117d493', False),
    ((14,), '954342568a52ea8550de7ce08f00f84b91221f157a2518a9ed089329996f9ecd', False),
    ((15,), '8ff9859c0297c0eb46f1636e96bbc9a05d89b68b8e405f19d66bba0050deed26', False),
]


@pytest.mark.parametrize("arguments, result, testcase", q4_testcases)
def test_q4(capsys, arguments, result, testcase):
    q4.half_diamond(*arguments)
    actual = normalized_output(capsys.readouterr().out)

    if testcase:
        assert actual == result
    else:
        assert hashcode(actual) == result


def test_q4_uses_nested_iteration():
    tree = ast.parse(inspect.getsource(q4.half_diamond))
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

    assert has_nested_loop, "half_diamond must use nested iteration."


def test_q4_no_row_generation_shortcuts():
    source = inspect.getsource(q4.half_diamond)
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
