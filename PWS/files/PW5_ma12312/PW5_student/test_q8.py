import pytest
import hashlib
import inspect
import ast
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

import q8


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


def normalized_codes(output):
    body = output.rstrip()
    assert "\n" not in body, "All arrangements must be printed on one line."
    if not body:
        return ""
    parts = body.split(" ")
    assert all(parts), "Arrangements must be separated by exactly one space and must not begin with a space."
    assert len(parts) == len(set(parts)), "Every arrangement must appear exactly once."
    return " ".join(sorted(parts))


q8_testcases = [
    ('ABC', 'ABC ACB BAC BCA CAB CBA', True),
    ('XYA', 'AXY AYX XAY XYA YAX YXA', True),
    ('cat', '48d70a0431dbbc5bcc79f486c03108b36b4fecd930ff967a1f6c6640eb43add3', False),
    ('DOG', '06469fc79d0487895368fb53ec33c92f867d00e421914fe4b9a5dd8a0168865b', False),
    ('xyz', '568bc324b7121584085007c9a8023a6a93f62fe744a2bbdfc4619722267d616a', False),
    ('KLM', '4494e46dd15bd2792944aa9f47da5dfd8aea4b7ebd7a7d6dfd9f509ace775c48', False),
    ('pqr', '1414334327fd9f485f8c588f680e298709de2c7d8134de6261e6ed93b9770c6c', False),
    ('mNq', 'cf988226fcb2f63371d4636161c8b5244db88b06a5179e6a19ec251e7b5c1623', False),
    ('Zed', '18a7c2517a7d9b86db237df94e03aeadceac0bc8ba8afae45595885fe08ffce6', False),
    ('sun', '4c2c82d52a77127a173af9efdb65083c07c535810d35751c0ee34cad2c8ebaa5', False),
    ('car', '17c694a962bc6db7fd83df13ea37e2d0c49669a6ffc9d95a171b2dd6b5ff0073', False),
    ('ace', '8021c5f105911131263ea2bb5acb66bdb8d4918d704d628cb268c11833c8a316', False),
    ('QRS', 'e744206e24e23f440d4706ac8b7d7a12b8ca37300c995733d66c0a580bb8bb09', False),
    ('bed', '29cb82d7945da02292326f030b67ad468f4f3ecd87342f1ffa492670a44d9a31', False),
    ('Joy', 'bbc48081b573befe391d21e217708e60fcee8c90033f94d842326f620adf281d', False),
]


@pytest.mark.parametrize("team_code, result, visible", q8_testcases)
def test_q8(capsys, team_code, result, visible):
    q8.print_code_permutations(team_code)
    actual = normalized_codes(capsys.readouterr().out)
    if visible:
        assert actual == result
    else:
        assert hashcode(actual) == result


def test_q8_uses_nested_iteration():
    assert _has_nested_iteration(q8.print_code_permutations), \
        "print_code_permutations must use nested iteration."


def test_q8_no_permutation_shortcuts():
    module_tree = ast.parse(inspect.getsource(q8))
    for node in ast.walk(module_tree):
        if isinstance(node, ast.Import):
            if any(alias.name == "itertools" for alias in node.names):
                pytest.fail("Do not use itertools to generate permutations.")
        if isinstance(node, ast.ImportFrom) and node.module == "itertools":
            pytest.fail("Do not use itertools to generate permutations.")

    tree = ast.parse(inspect.getsource(q8.print_code_permutations))
    forbidden = {"permutations", "permutation", "product", "combinations", "combinations_with_replacement", "__import__", "eval", "exec"}
    for node in ast.walk(tree):
        if isinstance(node, (ast.ListComp, ast.SetComp, ast.DictComp, ast.GeneratorExp)):
            pytest.fail("Use explicit nested iteration rather than comprehensions or generator expressions.")
        if isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name) and node.func.id in forbidden:
                pytest.fail(f"Do not use {node.func.id}() as a shortcut.")
            if isinstance(node.func, ast.Attribute) and node.func.attr in forbidden:
                pytest.fail(f"Do not use {node.func.attr}() as a shortcut.")
