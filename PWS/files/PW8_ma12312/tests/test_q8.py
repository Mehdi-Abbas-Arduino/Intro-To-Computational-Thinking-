import hashlib
import os
import sys

import pytest

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from q8 import *


q8_testcases = [
    ('Japan',
     'Aaj apa narangi laayi hain.',
     [2, 9],
     True),
    ('Mozambique',
     'Aaj apa musambi laayi hain.',
     [],
     True),
    ('Canada',
     'Can a day of extreme self-care really reset your mood and nervous system?',
     [0, 8],
     True),
    ('Peru',
     'Give hope. Run!',
     [7, 13],
     True),
    ('China',
     'HU cafeteria may open a branch in all major food districts--God help us!',
     [28, 35],
     True),
    ('Melon',
     "He found his home lonely after his dog's death.",
     '81aa6838408424e42729990f10cc1dbbb27ccd60d07c1a1c3e364b036354b13d',
     False),
    ('Pineapple',
     'There is only one fidget-spin app left in her phone.',
     '4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945',
     False),
    ('Peach',
     'The adventurers brought one map each.',
     '6e1db180aeb9a5737079e2f300b7b0e1b70b02d680c3d957e2fb01ece25cfe4b',
     False),
    ('Cherry',
     'The English teacher, Ryan, teaches French too.',
     '8c895ec8e97aba4b4216b9ce61eb774dbc9471c51ee92de48311c314ee122aa3',
     False),
    ('Banana',
     'One dare not rob an anaconda of its prey.',
     '8c895ec8e97aba4b4216b9ce61eb774dbc9471c51ee92de48311c314ee122aa3',
     False),
    ('Sweden',
     'The pleasures we deny ourselves are often the most tempting',
     'dd9d7d5bd872a651b19a16b8ff5777bc5080f2cb1b765f207e92c8d04a5ed8cd',
     False),
    ('Iran',
     'I1r2a3n',
     '9256b3c60b4c2079ce02d8b72d585797f60e6f1f80d4297bd39d7e5c36036012',
     False),
    ('Italy',
     'xx I-t A!l,y zz',
     '4d805ac8eb68b4ef9e51f39fc2e478eaa43f20be3e7a005efe57c320263a5410',
     False),
    ('Nepal',
     'nE p-A_l',
     '13f7576bb16f52aaff5b9ca6cd95b4302dded9a05af6abef7b89a13e502bda24',
     False),
    ('India',
     'In-dia and then I n d i a again',
     '8d0e00ef451bb2f75a9caac5227f428db2e333f4c9b227ddbffa0b395f68cb6d',
     False),
]


def hashcode(value):
    return hashlib.sha256(str(value).encode("utf-8")).hexdigest()


@pytest.mark.parametrize(
    "word, sentence, expected, visible",
    q8_testcases
)
def test_q8(word, sentence, expected, visible):
    result = word_search(word, sentence)

    assert isinstance(result, list), (
        f"Bad return type. Expected list but got {type(result)}."
    )

    assert len(result) in (0, 2), (
        "The function should return either an empty list or "
        "a list containing exactly two positions."
    )

    if len(result) == 2:
        assert all(isinstance(value, int) for value in result), (
            "The beginning and ending positions should be integers."
        )

    if visible:
        assert result == expected
    else:
        assert hashcode(result) == expected
