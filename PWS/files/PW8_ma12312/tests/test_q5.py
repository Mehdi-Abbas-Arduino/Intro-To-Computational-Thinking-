import ast
import hashlib
import inspect
import os
import sys
import pytest

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
import q5
from q5 import *

def hashcode(value):
    return hashlib.sha256(str(value).encode("utf-8")).hexdigest()

q5_testcases = [
    # Visible Testcases
    (['aardvark', 'buffalo', 'crocodile', 'dingo', 'elephant', 'fox', 'gorilla', 'hippopotamus'], ['elephant', 'aardvark', 'fox', 'buffalo', 'gorilla', 'crocodile', 'hippopotamus', 'dingo'], True),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [6, 1, 7, 2, 8, 3, 9, 4, 10, 5], True),
    ([1, 2], [2, 1], True),
    ([1, 2, 3, 4], [3, 1, 4, 2], True),
    ([10, 20, 30, 40, 50, 60], [40, 10, 50, 20, 60, 30], True),

    # Hidden Testcases
    ([1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048], 'f8a128b55a4311ccf52f66c375daacee945d8b29075d81fe4308f050a9ebe3e0', False),
    ([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584], 'e942304fe016750733412f69bd7c257926149499e3ed932466f1d2578bc5b312', False),
    ([], '4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945', False),
    ([2, 3, 5, 7, 11, 13, 17, 19, 21, 23, 29, 31, 37, 41, 43, 47], '8b9604e1681ee6a667eae5b7bf29f0311d6259663b38ddf690beed4b030932eb', False),
    (['alpha', 'bravo', 'charlie', 'delta', 'echo', 'foxtrot', 'golf', 'hotel', 'india', 'juliett', 'kilo', 'lima', 'mike', 'november', 'oscar', 'papa', 'quebec', 'romeo', 'sierra', 'tango', 'uniform', 'victor', 'whiskey', 'x-ray', 'yankee', 'zulu'], '25cb62225ff8ee5dac6b336d8e8d8fc57092209a78ecc6f2e31851658848902d', False),
    ([7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1, 4, 2, 1], 'c7fa9476c792c00cd74d392e9a1c92acbe18ed5a346a64b7e7bcf894c106bbdb', False),
    ([1, 2, 8, 3, 6, 9, 17, 4, 20, 7, 15, 10, 10, 18, 18, 5, 13, 21, 21, 8, 8, 16, 16, 11, 24, 11], '133d2d51987ee0b801fa730fe59a41b54a657b19c101e6955809b54935b36fb4', False),
    (['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'], 'b8cca231455165a4d14880aaf4c077b825a2c4d6a097b5d3ca467d383d98a7b5', False),
    ([0, 0, 1, 1], 'bae30d4cb014ded2c4578961f9b7b94a7ddf929e4b7d02fbbb9076dc212e244a', False),
    ([2, 4, 6, 8, 10, 12, 14, 16, 18, 20], '771e807a486a37362c9e2b7a9e23c28b304371a56b0d8cb1051a0b793265f51c', False),
]

def test_no_imports_or_global_variables():
    tree = ast.parse(inspect.getsource(q5))
    for node in ast.walk(tree):
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            raise AssertionError("You may not import modules in q5.py.")
        if isinstance(node, ast.Global):
            raise AssertionError("You may not use global variables in q5.py.")

@pytest.mark.parametrize("original, expected, visible", q5_testcases)
def test_q5(original, expected, visible):
    t=original.copy()
    result=riffle_shuffle(t)
    assert result is None
    if visible:
        assert t == expected
    else:
        assert hashcode(t) == expected
