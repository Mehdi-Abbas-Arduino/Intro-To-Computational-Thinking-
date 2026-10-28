import hashlib
import os
import sys

import pytest

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from q1 import crossword_positions

def hashcode(value):
    return hashlib.sha256(str(value).encode("utf-8")).hexdigest()

q1_testcases = [
    ('CHAI\nQUIZ\nBUNK\nLATE',
     [['C', 0, 0], ['H', 0, 1], ['A', 0, 2], ['I', 0, 3], ['Q', 1, 0], ['U', 1, 1], ['I', 1, 2], ['Z', 1, 3], ['B', 2, 0], ['U', 2, 1], ['N', 2, 2], ['K', 2, 3], ['L', 3, 0], ['A', 3, 1], ['T', 3, 2], ['E', 3, 3]], True),

    ('DS\nAL\nGO',
     [['D', 0, 0], ['S', 0, 1], ['A', 1, 0], ['L', 1, 1], ['G', 2, 0], ['O', 2, 1]], True),

    ('CHAI',
     [['C', 0, 0], ['H', 0, 1], ['A', 0, 2], ['I', 0, 3]], True),

    ('LIKE\nODIN\nVOCE\nELKS',
     'd94c2d7545456318aa48caa4af28be9f860370c57553a98b18404ed8c6311f2e', False),

    ('LIKEODINVOCEELKS',
     '177aa2616644123457cfd30947883fcf918b1278fbd69d172ec890e2964b1b81', False),

    ('lmnopqrstuvwxyz',
     '7a91f7ec100f4209164e61f1db65c1afd2cf93f2328bf51028707fea9866471b', False),

    ('a',
     '29eb8b7d3ff7df1319a105e2fceaa682770ff3fa96efb418f80981586f1f4c62', False),

    ('Z',
     '9a42792c92be74c519d440f2c8763db2ea936d44e800e251d75631a58ada0fe6', False),

    ('A\nB\nC\nD',
     '46963b9cc600f666b7a78df8b001608d3a4cbe3c9b6cf407ad8eb36f4cee77b1', False),

    ('ab\nCD',
     'ed882cf83c8b09141360e514cd1ccae59d868f4bd91da3e5713a65ed5725315a', False),

    ('ABC\nDEF',
     '4f185ff450be7a145da453fe514f728bf4e79e25686aa1cf0cf72a814edb4e69', False),

    ('HELLO\nWORLD',
     'aef7957813d680498a4c7c0d5cbe7eae892d03bb2ed4ea6e0a8d5fb3a87ca4ec', False),

    ('AaBb\ncCdD\nEeFf',
     '61e21a1d8ad01b879f4781f6aa0c1a7c66ac74f2a6a164bc0dd798f06d946a3f', False),

    ('AAAA\nAAAA',
     '651625105a8136364f48f82baa1d17e871e9cdde50c80d70ffca6537be50a349', False),

    ('PY\nTH\nON',
     '2699e203e2626c8dbe3ce31029aa65c1dede1fa81778860c845639537f65b901', False)
]


@pytest.mark.parametrize("crossword, expected, visible", q1_testcases)
def test_q1(crossword, expected, visible):
    result = crossword_positions(crossword)

    assert isinstance(result, list), (
        f"Expected a list, but got {type(result).__name__}."
    )
    if visible:
        assert result == expected
    else:
        assert hashcode(result) == expected