import pytest
import hashlib
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from q5 import *


def hashcode(value):
    return hashlib.sha256(str(value).encode("utf-8")).hexdigest()


q5_testcases = [
    (['how', 'much', 'wood', 'would', 'a', 'woodchuck', 'chuck', 'if', 'a', 'woodchuck', 'could', 'chuck', 'wood'], [], True),
    (['how', 'much', 'wood', 'would', 'a', 'woodchuck', 'chuck', 'if', 'a', 'woodchuck', 'COULD', 'chuck', 'wood'], ['woodchuck', 'chuck'], True),
    (['how', 'much', 'wood', 'would', 'a', 'WOODCHUCK', 'CHUCK', 'if', 'a', 'woodchuck', 'could', 'CHUCK', 'WOOD'], ['a', 'WOODCHUCK', 'CHUCK', 'if', 'could', 'CHUCK', 'WOOD'], True),
    (['HOW', 'much', 'WOOD', 'would', 'a', 'woodchuck', 'chuck', 'if', 'a', 'woodchuck', 'could', 'chuck', 'wood'], ['much', 'would'], True),
    (['HOW', 'much', 'wood', 'WOULD', 'A', 'woodchuck', 'CHUCK', 'if', 'a', 'woodchuck', 'COULD', 'chuck', 'wood'], ['much', 'wood', 'WOULD', 'A', 'woodchuck', 'if', 'woodchuck', 'chuck'], True),
    (['in', 'life', 'misery', 'is', 'INEVITABLE', 'it', 'is', 'what', 'it', 'is'], '3d42796ecdb0ea32b62044df15c514b24246be4d43f9e804c4269cb9c9342ac1', False),
    (['IN', 'life', 'misery', 'is', 'inevitable', 'it', 'is', 'what', 'it', 'is'], '438df5ac4619dcbd659fde9cdbbad30d11e7322cc2eb88e2586e853c49af8a72', False),
    (['in', 'LIFE', 'MISERY', 'IS', 'INEVITABLE', 'IT', 'is', 'what', 'it', 'is'], 'c6acd028ddf1a19ec630abb3d89f2abf73111fdff830fe064caddacf57359b33', False),
    (['in', 'life', 'misery', 'is', 'INEVITABLE', 'it', 'is', 'WHAT', 'it', 'IS'], '523dc337e49ccb78b4a5d44007cb8c75c3182c4249e76d8ec68dd144b567d8fb', False),
    (['IN', 'life', 'misery', 'is', 'inevitable', 'it', 'is', 'what', 'it', 'IS'], 'c63ee73a047e6e9c6f60f893b08816a8a64c1e3f3ca8cd132265bb2b4297cb34', False),
    ([], '4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945', False),
    (['HELLO'], '4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945', False),
    (['HELLO', 'there', 'WORLD'], 'ac05ef14c1aa40f02157e93e5df61390ebbb1c4ae257a906acf4217622087723', False),
    (['a1', 'B2', 'c3', 'D4', 'e5'], '9d057e1602d5c99eb110a065ae9e1ab4533aec4e046bad08f71d9227d3797176', False),
    (['SAME', 'same', 'SAME', 'same', 'SAME'], 'ec23453f13905ba76102cae3f380dbbda39df4a610c1cb66f65635a920ffd988', False),
]


@pytest.mark.parametrize("words, expected, visible", q5_testcases)
def test_q5(words, expected, visible):
    result = noisy_neighbors(words)

    assert isinstance(result, list), (
        f"Bad return type. Expected list but got {type(result)}."
    )

    if visible:
        assert result == expected
    else:
        assert hashcode(result) == expected