import pytest
import hashlib
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from q6 import *


def hashcode(value):
    return hashlib.sha256(str(value).encode("utf-8")).hexdigest()


q6_testcases = [
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3, [10, 7, 8, 9, 4, 5, 6, 1, 2, 3], True),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 12, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], True),
    (['aardvark', 'buffalo', 'crocodile', 'dingo', 'elephant', 'fox', 'gorilla', 'hippopotamus'], 4, ['elephant', 'fox', 'gorilla', 'hippopotamus', 'aardvark', 'buffalo', 'crocodile', 'dingo'], True),
    ([1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096], 1, [4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1], True),
    ([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584], 5, [987, 1597, 2584, 89, 144, 233, 377, 610, 8, 13, 21, 34, 55, 1, 1, 2, 3, 5], True),
    ([], 1, '4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945', False),
    ([2, 3, 5, 7, 11, 13, 17, 19, 21, 23, 29, 31, 37, 41, 43, 47], 20, '2850d053e7b8538d4401ec7f4cde5b48de53de1ae1735008a7d560d9faab853c', False),
    (['alpha', 'bravo', 'charlie', 'delta', 'echo', 'foxtrot', 'golf', 'hotel', 'india', 'juliett', 'kilo', 'lima', 'mike', 'november', 'oscar', 'papa', 'quebec', 'romeo', 'sierra', 'tango', 'uniform', 'victor', 'whiskey', 'x-ray', 'yankee', 'zulu'], 2, '45655c9acc6cb2706e6c9426cf35628bbcc97d7239eda48b28f1499e78731a62', False),
    ([7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1], 1, '22a398ff0c87c7752aaafe2d80286435cbdff41d10f93d1ea5530dd75c62d1f9', False),
    ([1, 2, 8, 3, 6, 9, 17, 4, 20, 7, 15, 10, 10, 18, 18, 5, 13, 21, 21, 8, 8, 16, 16, 11, 24, 11], 6, '3510544eb94cb237af016c8746e7a08874d839f90808ca4758f3c871454efd46', False),
    ([42], 1, 'b86b1ea11b28136fe5224b9d1e3017b7efb68d4fae0b90c4940e0c0f89b3907a', False),
    ([1, 2, 3, 4, 5, 6], 3, '2dbd18768e3fa1a54c2e9e69590ed16bd09a55328568e86e4b135baf53885bbf', False),
    (['a', 'b', 'c', 'd', 'e'], 2, '18b2f671a44f1d79667403f9407aed7aa9c43e84ab65ae32f44c7f2df30852d1', False),
    ([5, 5, 5, 5, 5, 5, 5], 3, '4a8c6368ef7d2582a0fed9a47c7d64ab7294e9404297e83a5ba0af1c5c2906d7', False),
    ([10, 20, 30], 3, '15d98dad2ba94449f66d415d63b1e633ed896a72c15c6b91407410b8e06f5e20', False),
]


@pytest.mark.parametrize("deck, cut_size, expected, visible", q6_testcases)
def test_q6(deck, cut_size, expected, visible):
    original_deck = deck.copy()

    result = hindu_shuffle(deck, cut_size)

    assert isinstance(result, list)

    if visible:
        assert result == expected
    else:
        assert hashcode(result) == expected