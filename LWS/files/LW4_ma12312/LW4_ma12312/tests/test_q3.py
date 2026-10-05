import pytest
import hashlib
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from q3 import *

q3_testcases = [
    # Visible Testcases
    (1, "1", True),
    (3, "3, 8, 4, 2, 1", True),
    (8, "8, 4, 2, 1", True),
    (14, "14, 7, 20, 10, 5", True),
    (17, "17", True),

    # Hidden Testcases
    (50, "298934e6fd8c8b041fe5243c9f32056a6ad7deae1464aa9d1148b18c98fd6cd8", False),
    (56, "db943c346f5fdaa5427e2cf6490a2f5abd8e04f07fb0be3144ce049c1e827a04", False),
    (243, "45d6007390869a808434fe54e9483d223a18b61562b7624bb56595a5c9914175", False),
    (512, "b497e5e1b44b51023a14137274871ed59653ce39b5b5107da0b67692eb08edb9", False),
    (1023, "fa44c63835f90b3ac98561895a4204aec2dd742bedde6c061e4e6e5b70b7b680", False),
    (23, "fd7e7194d2765ab672e857a9f82c17ca87cc158ff35b746620288a84bc68a5c6", False),
    (6, "d4bc46d6f08336207441668ff6305300da2d5479ff2bac6bd9662b5afb3a5661", False),
    (11, "0121e445335527ce8de9f24d73d39242b34977f7ce4c05e8cdc28c6709261ce3", False),
    (75, "5b7306d9a2f443cfa63a66ab33da0e45b418bcdfbb6c39ac5964a844fef909db", False),
    (125, "52b6ba1ef17d0719895e43d2df749ac7a6df21c954bfcab03bac3d0ceca29885", False),
]

def hashcode(n: int) -> str:
    return hashlib.sha256(str(n).encode('utf-8')).hexdigest()

@pytest.mark.parametrize("starting_number, result, testcase", q3_testcases)
def test_q3(capsys, starting_number, result, testcase):
    collatz_sequence(starting_number)
    captured, err = capsys.readouterr()
    captured=captured.strip()
    if testcase:
        assert captured == result
    else:
        assert hashcode(captured) == result