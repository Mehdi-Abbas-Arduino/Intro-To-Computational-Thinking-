import pytest
import hashlib
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from q1 import *

q1_testcases = [
    # Visible Testcases
    (1, 1, 1, True),
    (2, 2, 0, True),
    (1, 2, 1, True),
    (2, 3, 3, True),
    (13, 2, 48, True),
    (6.7, 10, "Error: bad argument. sum_odd is defined for integers only.", True),

    # Hidden Testcases
    (2, 1, "6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b", False),
    (-2.0, 3, "941b2c104e529bc221d98bcc01e9b9203ed345580e7e73c30c5e01816f1b1605", False),
    (2, 13, "98010bd9270f9b100b6214a21754fd33bdc8d41b2bc9f9dd16ff54d3c34ffd71", False),
    (20, 300, "481922bc82550bf541bbe9381d43ac7a22a5cadc365eddd882a8628cb4f280eb", False),
    (-5, 5, "5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9", False),
    (-10, -2, "628eee823448ed34c634b578436a53dcbb6559f18b696db721fb25ab0aa1fb4b", False),
    (0, 0, "5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9", False),
    (7, 7, "7902699be42c8a8e46fbbb4501726517e86b22c56a189f7625a6da49081b2451", False),
    (True, 5, "941b2c104e529bc221d98bcc01e9b9203ed345580e7e73c30c5e01816f1b1605", False)
]

def hashcode(n: int) -> str:
    return hashlib.sha256(str(n).encode('utf-8')).hexdigest()

@pytest.mark.parametrize("first_number, second_number, result, testcase", q1_testcases)
def test_q1(first_number, second_number, result, testcase):
    if testcase:
        assert sum_odd(first_number, second_number) == result
    else:
        assert hashcode(sum_odd(first_number, second_number)) == result