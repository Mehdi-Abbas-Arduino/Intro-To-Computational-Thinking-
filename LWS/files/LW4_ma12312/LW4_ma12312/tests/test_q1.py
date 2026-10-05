import pytest
import hashlib
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from q1 import *

q1_testcases = [
    # Visible Testcases
    (5, 2, '5, 4, 3, 2', True),
    (4, -3, '4, 3, 2, 1, 0, -1, -2, -3', True),
    (-1, -5, '-1, -2, -3, -4, -5', True),
    (3.0, -4, 'Error: bad argument. countdown is defined for integers only.', True),
    (3, -4.5, 'Error: bad argument. countdown is defined for integers only.', True),

    # Hidden Testcases
    (1, 0, 'd8f283e3e4ce9177ddbbee2abe89ddd5471134599d9ce1475070d70e29dffb53', False),
    (0, -1, 'f3d04e591c3ca4420be898bdbcc658e08a98bd2dfcd29c8bf9990a6b35211a16', False),
    (10, 1, 'dde506c6c99fe8bd777af2033ba0c14cf66b3a2e0e530ba5f19861fe56f9bacd', False),
    (2, -5, '77d08c05b88787af555313685c3b9ff9cde848a5fa0fcaa0c4c58268e0d66d12', False),
    (20, 15, 'f392ce4e10b6c77eee5a28b7d510d93efe6f2b58686f636ffb133b0c9fad0d15', False),
    (7, -5, '0f459984896f3a3a6369fe20d257b2cfc25d1348d44872d0d905c7a1d9370164', False),
    (20, -5, 'c2b422558a5cbc34d448fe22fea97dea6c5985f57f90c583cbefc1cb2054017f', False),
    (8.5, 2, '3476b01a45baf28d4ba56ebdb5d4a7749eecfdfe56fd7ce301516f6b6a0badc8', False),
    (8, 2.5, '3476b01a45baf28d4ba56ebdb5d4a7749eecfdfe56fd7ce301516f6b6a0badc8', False),
    (6.0, -2.0, '3476b01a45baf28d4ba56ebdb5d4a7749eecfdfe56fd7ce301516f6b6a0badc8', False),
]

def hashcode(n: int) -> str:
    return hashlib.sha256(str(n).encode('utf-8')).hexdigest()

@pytest.mark.parametrize("starting_floor, ending_floor, result, testcase", q1_testcases)
def test_q1(capsys, starting_floor, ending_floor, result, testcase):
    countdown(starting_floor, ending_floor)
    captured,err = capsys.readouterr()
    captured=captured.strip()
    if testcase:
        assert captured == result
    else:
        assert hashcode(captured) == result