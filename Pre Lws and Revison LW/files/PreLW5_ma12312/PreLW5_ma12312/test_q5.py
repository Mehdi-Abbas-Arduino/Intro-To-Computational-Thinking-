import pytest
import hashlib
import inspect
import ast
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

import q5


def hashcode(value):
    return hashlib.sha256(str(value).encode("utf-8")).hexdigest()


def normalized_output(output):
    body = output.rstrip("\n")
    if not body:
        return ""
    return "\n".join(line.rstrip() for line in body.splitlines())


q5_testcases = [
    # Visible Testcases
    ((5,), '*****\n*   *\n*   *\n*   *\n*****', True),
    ((1,), '*', True),
    ((3,), '***\n* *\n***', True),

    # Hidden Testcases
    ((2,), '93cf69f87ae3ce87b757a82e5edcf1049b8cba1acea2c2e58c243080d6f25356', False),
    ((4,), '6fd33657d833e48f9e53b44903510ea8cec0aa73544a0f8eda317fdc252e57f3', False),
    ((6,), '9f6edeb3c8d4aff486b326d2404a1227c17ceff7180e3e229c3a5048b8993e6c', False),
    ((7,), '6adb1ef2129c34d799700ab53348f896c95dd0f07b8448e328dbf4a2cfd76e22', False),
    ((8,), '0671f421362f69837a05340940f4a65ee939ef7235b0d67b90ec98082956f896', False),
    ((9,), 'f03a61b0d84670ff073107c716a8146e318eaa30b8d1ae3789240352f807b1a2', False),
    ((10,), '6360f74bafd7938c56ef301defd34900e19c959fb5fe4a01e5b3e41485aa024d', False),
    ((11,), '9370d1d78bcf73ef6419f708a9425785061be9d75995fd262272ce82ece3ff4e', False),
    ((12,), '222328bab80642a42a70456ac68a665c9c0231362d205847ce31fc81fc42f05a', False),
    ((13,), 'ae176ecb77886099e720c79bc606a0f806b9cd0558f36db67c61d3e00f9eb0d8', False),
    ((14,), '75db9ebb495db61962f481fd72ec7c0ec0c550298d942a4337d5b5a65fbd04a5', False),
    ((15,), 'e62512d236eb8fd7951c4ae83283a5d10f6129ed9e40a9eb5cf7ba718d355587', False),
]


@pytest.mark.parametrize("arguments, result, testcase", q5_testcases)
def test_q5(capsys, arguments, result, testcase):
    q5.hollow_square(*arguments)
    actual = normalized_output(capsys.readouterr().out)

    if testcase:
        assert actual == result
    else:
        assert hashcode(actual) == result


def test_q5_uses_nested_iteration():
    tree = ast.parse(inspect.getsource(q5.hollow_square))
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

    assert has_nested_loop, "hollow_square must use nested iteration."


def test_q5_no_row_generation_shortcuts():
    source = inspect.getsource(q5.hollow_square)
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
