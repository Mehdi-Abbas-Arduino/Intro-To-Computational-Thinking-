import pytest
import hashlib
import inspect
import ast
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

import q3


def hashcode(value):
    return hashlib.sha256(str(value).encode("utf-8")).hexdigest()


def normalized_output(output):
    body = output.rstrip("\n")
    if not body:
        return ""
    return "\n".join(line.rstrip() for line in body.splitlines())


q3_testcases = [
    # Visible Testcases
    ((5,), '*\n**\n***\n****\n*****', True),
    ((1,), '*', True),
    ((3,), '*\n**\n***', True),

    # Hidden Testcases
    ((2,), 'd8dd2d403c280f0cb02c14eb990c56ebc31e8a87ff29ea03ccbd4bf85137eaa9', False),
    ((4,), 'b1a6b87a213c4c9efc48fc20ef99e1d04940f1ed376ff7a302c961550120ec9c', False),
    ((6,), '0fff1e6c22e4723f3a75cf9de66f829379c19e2214552f6196dd6679bec5e2cc', False),
    ((7,), '3dd95654731a00288f675c9d5811e5bcc2b419f8e9e67fa6edad0d6233c75c72', False),
    ((8,), '6bc157c63aaa30e89c6ae7db747be8c510ad716ae395e2460addcd727ef025f3', False),
    ((9,), '86b21767aed2facffeb73899ec4c254983e727582d60e2443945bea85b303c3a', False),
    ((10,), 'f99cc94dfb670477a9abe935ab538df342c41768163c36329ec1b9415a55dfbe', False),
    ((11,), 'b76bae3e302bdd4afcb97c7ce95d56b354fc73ea32509f7db369300cfd9e4171', False),
    ((12,), '6a2e2c971515fb4764a3ed6f03919c7d0e3324379722c917facd96de0d70a994', False),
    ((13,), '3b80db2759d2d1e884d93c54e21badd7a11a60b90093dc0c3411ea1dd4c98e63', False),
    ((14,), '899fa3631275f3b2b44c6d6f9071992c8cc6d0e89189e79ee2c71bfba9d26c32', False),
    ((15,), '9782018ce7a0e00b62a71ab9d18f76ef000bfb1b39b40f4615fef21325dd5321', False),
]


@pytest.mark.parametrize("arguments, result, testcase", q3_testcases)
def test_q3(capsys, arguments, result, testcase):
    q3.right_triangle(*arguments)
    actual = normalized_output(capsys.readouterr().out)

    if testcase:
        assert actual == result
    else:
        assert hashcode(actual) == result


def test_q3_uses_nested_iteration():
    tree = ast.parse(inspect.getsource(q3.right_triangle))
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

    assert has_nested_loop, "right_triangle must use nested iteration."


def test_q3_no_row_generation_shortcuts():
    source = inspect.getsource(q3.right_triangle)
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
