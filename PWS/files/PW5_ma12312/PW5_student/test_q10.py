import pytest
import hashlib
import inspect
import ast
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

import q10


def hashcode(value):
    return hashlib.sha256(str(value).encode("utf-8")).hexdigest()


q10_testcases = [
    (213212, 'YES', True),
    (218812, 'YES', True),
    (121212, 'NO', True),
    (123321, 'f9171164593756e56fb197327b529a4955590566560dbe62d586bff41be9d297', False),
    (111111, 'f9171164593756e56fb197327b529a4955590566560dbe62d586bff41be9d297', False),
    (123421, 'f9171164593756e56fb197327b529a4955590566560dbe62d586bff41be9d297', False),
    (123456, '23794d91c53ae875c8e247d72561e35d9d06ee07c70c9e0dbcc977a6d161504a', False),
    (100001, 'f9171164593756e56fb197327b529a4955590566560dbe62d586bff41be9d297', False),
    (100011, 'f9171164593756e56fb197327b529a4955590566560dbe62d586bff41be9d297', False),
    (999999, 'f9171164593756e56fb197327b529a4955590566560dbe62d586bff41be9d297', False),
    (654456, 'f9171164593756e56fb197327b529a4955590566560dbe62d586bff41be9d297', False),
    (654356, 'f9171164593756e56fb197327b529a4955590566560dbe62d586bff41be9d297', False),
    (120021, 'f9171164593756e56fb197327b529a4955590566560dbe62d586bff41be9d297', False),
    (120031, 'f9171164593756e56fb197327b529a4955590566560dbe62d586bff41be9d297', False),
    (908809, 'f9171164593756e56fb197327b529a4955590566560dbe62d586bff41be9d297', False),
]


@pytest.mark.parametrize("entry_code, result, visible", q10_testcases)
def test_q10(entry_code, result, visible):
    actual = q10.is_lucky_code(entry_code)
    if visible:
        assert actual == result
    else:
        assert hashcode(actual) == result


def test_q10_uses_iteration():
    tree = ast.parse(inspect.getsource(q10.is_lucky_code))
    assert any(isinstance(node, (ast.For, ast.While)) for node in ast.walk(tree)), \
        "is_lucky_code must use iteration."


def test_q10_no_sequence_shortcuts():
    tree = ast.parse(inspect.getsource(q10.is_lucky_code))
    forbidden_calls = {"str", "list", "reversed", "repr", "format"}
    for node in ast.walk(tree):
        if isinstance(node, ast.List):
            pytest.fail("Do not use lists to compare the digits as a sequence.")
        if isinstance(node, ast.ListComp):
            pytest.fail("Do not use lists or list comprehensions to compare the digits as a sequence.")
        if isinstance(node, ast.Slice):
            pytest.fail("Do not use slicing to compare the digits as a sequence.")
        if isinstance(node, ast.JoinedStr):
            pytest.fail("Do not convert the entry code to a string.")
        if isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name) and node.func.id in forbidden_calls:
                pytest.fail(f"Do not use {node.func.id}() for digit-sequence comparison.")
            if isinstance(node.func, ast.Attribute) and node.func.attr in {"format"}:
                pytest.fail("Do not use string formatting for digit-sequence comparison.")
