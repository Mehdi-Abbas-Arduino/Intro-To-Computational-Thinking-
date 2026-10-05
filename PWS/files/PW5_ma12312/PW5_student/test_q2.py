import pytest
import hashlib
import inspect
import ast
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from q2 import print_power_levels


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


q2_testcases = [
    (1, '1', True),
    (2, '1\n2 1', True),
    (3, '1\n2 1\n4 2 1', True),
    (6, '1\n2 1\n4 2 1\n8 4 2 1\n16 8 4 2 1\n32 16 8 4 2 1', True),
    (8, '1\n2 1\n4 2 1\n8 4 2 1\n16 8 4 2 1\n32 16 8 4 2 1\n64 32 16 8 4 2 1\n128 64 32 16 8 4 2 1', True),
    (4, 'cc3dbe63fd7667330512a0cb5f0aab829ca8c354525390093f70f4603eb8798d', False),
    (5, '3505404791b967dd61e3626366ddc17d601db430089fa2e9ebf188d51ae7863e', False),
    (7, '70d7114babe9c6ba45f8a53ef98f31ce447895831b31fdc1b1ac766260c83f0b', False),
    (9, 'd7e0135b48a6bc0f12a3383b469144df06c93ac42e9b87ca03c0ef6eda223e72', False),
    (10, '86e787b7413261a7d9b03195e9008aa524ef2525dfcd97349a4e093bf87f1362', False),
    (11, 'acfa1e76faa16dd2b5f31809bfc7507992e3bc22572f513ca0ae3661d37ea4b2', False),
    (12, '2bcdc3d9cee0d65911a12d9e35d5b8a54754a8120600657b634f23f5bb70c178', False),
    (15, 'ef8bd2e5b983d131daf39251b3d0d91a899285db0a4560c92580fd0a5e92b106', False),
    (20, '951e92324cf6f92e773ba2b6d9e06f0fb986093aa5f2e54c2092983c765c81b4', False),
    (25, '74e84255f736d667af7d1b69eaab940aa1c67afc1f5c048d0ee18a21f979d04b', False),
]


@pytest.mark.parametrize("row_count, result, visible", q2_testcases)
def test_q2(capsys, row_count, result, visible):
    print_power_levels(row_count)
    actual = normalize_output(capsys.readouterr().out)
    if visible:
        assert actual == result
    else:
        assert hashcode(actual) == result


def test_q2_uses_nested_iteration():
    assert _has_nested_iteration(print_power_levels), \
        "print_power_levels must use nested iteration."
