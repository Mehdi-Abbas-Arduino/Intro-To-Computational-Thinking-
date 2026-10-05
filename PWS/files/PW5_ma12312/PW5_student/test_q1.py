import pytest
import hashlib
import inspect
import ast
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from q1 import print_combo_multipliers


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


q1_testcases = [
    (1, '1', True),
    (2, '2 4\n1', True),
    (3, '3381049549cfeecc7edf41c509804f106c61737be8187d0b98aba8dd2b9f10ad', False),
    (4, '5cd00c5d7b3a8d39aeee0c251534c7e72d7ade039b483adf27190609a1ad6059', False),
    (5, '6a08d50e57d7982776f0e972f2ea1de9ea038f751409d7c0a1f7c51fbc0825f8', False),
    (6, 'cded97bedc5e295161a42b00ef6877d2d14e8428829fe7a0f244a0f05921d917', False),
    (7, 'af55de0df097ce0e8fbcf28778a6191d263bd6292e66d9f4ebad568ccc0bb9cd', False),
    (8, '45e4cc4eee742d443182defa166628af5f68c4d7f5036dcb82e79323aa1c9adc', False),
    (9, '0ee0b37fcf03893a0ab27a0e3467f1db8c85b25304b622561ce020b105d84eb5', False),
    (10, '22fd2774967d9996800fdda3e99fc0c71eae82b1bcc20c4809c22c0b60a65080', False),
]


@pytest.mark.parametrize("level_count, result, visible", q1_testcases)
def test_q1(capsys, level_count, result, visible):
    print_combo_multipliers(level_count)
    actual = normalize_output(capsys.readouterr().out)
    if visible:
        assert actual == result
    else:
        assert hashcode(actual) == result


def test_q1_uses_nested_iteration():
    assert _has_nested_iteration(print_combo_multipliers), \
        "print_combo_multipliers must use nested iteration."
