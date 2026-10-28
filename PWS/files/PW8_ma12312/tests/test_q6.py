import ast
import hashlib
import inspect
import os
import sys
import pytest

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
import q6
from q6 import *

def hashcode(value):
    return hashlib.sha256(str(value).encode("utf-8")).hexdigest()

q6_testcases = [
    # Visible Testcases
    ([1, 3, 3, 3, 2, 2, 1], 3, [1, 2, 2, 1], True),
    ([1, 2, 2, 2, 1, 1], 3, [], True),
    ([6, 1, 1, 6, 6, 1, 1, 1, 6, 6, 6], 3, [6, 1, 1], True),
    ([1, 2, 2, 1], 2, [], True),
    ([7, 7, 7, 7], 3, [], True),

    # Hidden Testcases
    ([1, 2, 3, 4, 5], 3, '0c049903ce2330190375d4c1f2e489888c9ebe39daf75b2564e591e8bc1afe72', False),
    ([4, 4, 4, 4, 4, 2, 3], 3, '5bf775530e2e5fcd9c6ae577c52cd57a20d13ebb5f7bc3e8a8a7920d3a7ce41e', False),
    ([0, 0, 0, 1, 1, 1, 0], 3, 'd0bca111f8628137adc4c16f123496dcdd1d590d06cb5d9acd68b39fe656fb97', False),
    ([1, 1, 2, 2, 2, 1, 1, 3, 3, 3], 3, '4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945', False),
    ([0, 0, 0, 9, 1, 1, 1, 9, 9], 3, '4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945', False),
    ([1, 1, 2, 2, 2, 2, 2, 1, 3, 3, 3, 3, 1, 1, 1], 3, '4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945', False),
    ([1, 2, 3], 2, 'a36b1f2c3f84522dd1005145646617d7054c0851e97c72a039c0bdfac9fa07f3', False),
    ([5, 5, 5, 5, 5, 1, 1], 4, 'e718fe8edf8a7c2917cd7444286b7048042a74abf5208f1d70933c08dbd6b7e9', False),
    ([2, 2, 3, 3, 3, 2, 2], 3, '4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945', False),
    ([8, 8, 9, 9, 9, 8, 8, 8], 3, '4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945', False),
]

def test_no_modules_or_set():
    tree = ast.parse(inspect.getsource(q6))
    for node in ast.walk(tree):
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            raise AssertionError("You may not import modules in q6.py.")
        if isinstance(node, (ast.Set, ast.SetComp)):
            raise AssertionError("You may not use set in q6.py.")
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == "set":
            raise AssertionError("You may not use set in q6.py.")

@pytest.mark.parametrize("bubbles, k, expected, visible", q6_testcases)
def test_q6(bubbles, k, expected, visible):
    result=pop_bubbles(bubbles,k)
    assert isinstance(result,list)
    if visible:
        assert result == expected
    else:
        assert hashcode(result) == expected
