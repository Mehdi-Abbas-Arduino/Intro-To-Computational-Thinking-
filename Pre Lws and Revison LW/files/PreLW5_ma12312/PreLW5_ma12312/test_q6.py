import pytest
import hashlib
import inspect
import ast
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

import q6


def hashcode(value):
    return hashlib.sha256(str(value).encode("utf-8")).hexdigest()


def normalized_output(output):
    body = output.rstrip("\n")
    if not body:
        return ""
    return "\n".join(line.rstrip() for line in body.splitlines())


q6_testcases = [
    # Visible Testcases
    ((5, 5), 'XOXOX\nOXOXO\nXOXOX\nOXOXO\nXOXOX', True),
    ((2, 4), 'XOXO\nOXOX', True),
    ((1, 1), 'X', True),

    # Hidden Testcases
    ((1, 5), '42fc15e989da6d0a7d6c16a8c49d80236f5fcde2dbab69c2dd06cb8f4be34374', False),
    ((5, 1), '90b457e19ed485330633622e40df63f1109fa5cdeb8645383100520b9c98452c', False),
    ((3, 3), '948bfb74c42957c9bcefe8def915e1e64b73ffed670312fd82898189594abd23', False),
    ((3, 6), 'cf571b73a8c98bb013e5da9b038138bfc92c1ecab0902cadbec59bee03e09764', False),
    ((6, 3), 'c831663bee754980c587f639b563b0255ecae5c3fcd395f7a173d599f0287b0f', False),
    ((4, 4), 'cb5669ff0555194d7dcbe529f45b28a8b6d8d3aee8c733283ab6545499721d4e', False),
    ((4, 7), 'ac61ca1350a858493241f51d9ffe77424d6c7ef29751fc2379bae4bb46188e10', False),
    ((7, 4), '04135fbd166b5b0e888cb5379569a4f4b7cb0fe464513ceea599bbd39401de24', False),
    ((2, 2), 'fbbd9b03a35e20a503eada4f0e48655e72f561ead4acc1b8acee973c12363e5f', False),
    ((6, 6), 'fe2821ff879c1f33a294a7c5a3e65dc542982444cc54bc9391a42136f872b118', False),
    ((1, 8), 'eb6810d62c9806009bfe99e2ad2e78580396f81d78152166a935a7d4ad49efc6', False),
    ((8, 1), '9d03e064cc5472f9633cc06187f371d29961d77f33eda7835ab8bb99152ce74b', False),
]


@pytest.mark.parametrize("arguments, result, testcase", q6_testcases)
def test_q6(capsys, arguments, result, testcase):
    q6.chessboard_pattern(*arguments)
    actual = normalized_output(capsys.readouterr().out)

    if testcase:
        assert actual == result
    else:
        assert hashcode(actual) == result


def test_q6_uses_nested_iteration():
    tree = ast.parse(inspect.getsource(q6.chessboard_pattern))
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

    assert has_nested_loop, "chessboard_pattern must use nested iteration."


def test_q6_no_row_generation_shortcuts():
    source = inspect.getsource(q6.chessboard_pattern)
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
