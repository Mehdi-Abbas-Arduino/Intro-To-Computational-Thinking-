import pytest
import hashlib
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from q2 import *

q2_testcases = [
    # Visible Testcases
    ([8, 6, 6, 7, 5, 3, 7, 0, 7, 7, 9, 7], 2, 0, [8, 6, 6, 7, 5, 3, 7, 0, 7, 7, 9, 7], True),
    ([8, 6, 6, 7, 5, 3, 7, 0, 7, 7, 9, 7], 5, 1, [8, 6, 6, 7, 3, 7, 0, 7, 7, 9, 7], True),
    ([8, 6, 6, 7, 3, 7, 0, 7, 7, 9, 7], 7, 5, [8, 6, 6, 3, 0, 9], True),
    ([2, 2, 2, 2], 2, 4, [], True),
    ([], 2, 0, [], True),

    # Hidden Testcases
    (['gerbil', 'cat', 'dog', 'grey parrot', 'horse', 'goldfish', 'rabbit', 'hamster', 'otter', 'manatee', 'peacock', 'snake', 'gerbil', 'lion', 'elephant', 'gerbil', 'gerbil', 'rhinoceros', 'gerbil', 'hippopotamus', 'koala', 'gerbil'], 'deer', '5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9', '4ada2e9c756a61d7a9fe71bafaecd2cccd5668fa79c96964ba37b12dec674b9a', False),
    (['gerbil', 'cat', 'dog', 'grey parrot', 'horse', 'goldfish', 'rabbit', 'hamster', 'otter', 'manatee', 'peacock', 'snake', 'gerbil', 'lion', 'elephant', 'gerbil', 'gerbil', 'rhinoceros', 'gerbil', 'hippopotamus', 'koala', 'gerbil'], 'elephant', '6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b', '4423956f8f33e3dd15247731ec93a2008c4b00f0d336ed5014ef6469bd236a05', False),
    (['gerbil', 'cat', 'dog', 'grey parrot', 'horse', 'goldfish', 'rabbit', 'hamster', 'otter', 'manatee', 'peacock', 'snake', 'gerbil', 'lion', 'gerbil', 'gerbil', 'rhinoceros', 'gerbil', 'hippopotamus', 'koala', 'gerbil'], 'gerbil', 'e7f6c011776e8db7cd330b54174fd76f7d0216b612387a5ffcfb81e6f0919683', 'c831ec4216c1b5230a43381c717ffa7416f8eaab3ae902b8e19114439933f71b', False),
    ([1, 2, 1, 3, 1], 1, '4e07408562bedb8b60ce05c1decfe3ad16b72230967de01f640b7e4729b49fce', '5bf775530e2e5fcd9c6ae577c52cd57a20d13ebb5f7bc3e8a8a7920d3a7ce41e', False),
    (['a', 'b', 'a', 'c'], 'a', 'd4735e3a265e16eee03f59718b9b5d03019c07d8b6c51f90da3a666eec13ab35', '886121b70d7c6fdb24990641c9fcecdd01152eef64f2a3caa3f6cffa40b5f728', False),
    ([5], 5, '6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b', '4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945', False),
    ([5], 7, '5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9', '1ae3592f8248c3f879b56afe3f2ce6aad45ba898434796d35c565684397fb3e6', False),
    ([0, 0, 1, 0, 2, 0], 0, '4b227777d4dd1fc61c6f884f48641d02b4d121d3fd328cb08b5531fcacdabf8a', '3a316d6d3226f84c1e46e4447fa8d5fd800bff4a1bc6498152523cd4a602b69b', False),
    ([1.5, 2.5, 1.5], 1.5, 'd4735e3a265e16eee03f59718b9b5d03019c07d8b6c51f90da3a666eec13ab35', 'd12b59f6f760de2712eb596685a87451ec1839398000e9da7c10fe942dd110a6', False),
    ([('a', 1), ('b', 2), ('a', 1)], ('a', 1), 'd4735e3a265e16eee03f59718b9b5d03019c07d8b6c51f90da3a666eec13ab35', '999ae44dab4e6143f9c3b42cef6ec0528e05f800036d21672fd48afa1c8a9c43', False),
]

def hashcode(value):
    return hashlib.sha256(str(value).encode("utf-8")).hexdigest()

@pytest.mark.parametrize("t, v, funcresult, tresult, visible", q2_testcases)
def test_q2(t, v, funcresult, tresult, visible):
    import inspect
    import re

    list_methods = ['__delitem', '__getitem__', '__setitem__']
    verboten_methods = [
        '\\.[ \\t]*' + method + '[ \\t]*\\('
        for method in list_methods
    ]
    verboten = ['eval', 'getattr', '\\[', '\\]']
    verboten.extend(verboten_methods)
    verboten = [re.compile(pattern) for pattern in verboten]

    if any(pattern.search(inspect.getsource(remove_all)) for pattern in verboten):
        raise Exception(
            'eval function, getattr function, indexing, slicing, '
            'or internal list methods may not be used.'
        )

    if visible:
        assert remove_all(t, v) == funcresult
        assert t == tresult
    else:
        assert hashcode(remove_all(t, v)) == funcresult
        assert hashcode(t) == tresult
