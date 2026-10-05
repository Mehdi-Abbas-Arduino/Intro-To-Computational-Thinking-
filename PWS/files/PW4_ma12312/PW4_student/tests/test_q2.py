import pytest
import hashlib
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from q2 import *

q2_testcases = [
    # Visible Testcases
    (3, True, True),
    (8, False, True),
    (36, False, True),
    (51, False, True),
    (107, True, True),

    # Hidden Testcases
    (13, "3cbc87c7681f34db4617feaa2c8801931bc5e42d8d0f560e756dd4cd92885f18", False),
    (2, "3cbc87c7681f34db4617feaa2c8801931bc5e42d8d0f560e756dd4cd92885f18", False),
    (102, "60a33e6cf5151f2d52eddae9685cfa270426aa89d8dbc7dfb854606f1d1a40fe", False),
    (17, "3cbc87c7681f34db4617feaa2c8801931bc5e42d8d0f560e756dd4cd92885f18", False),
    (111, "60a33e6cf5151f2d52eddae9685cfa270426aa89d8dbc7dfb854606f1d1a40fe", False),
    (33, "60a33e6cf5151f2d52eddae9685cfa270426aa89d8dbc7dfb854606f1d1a40fe", False),
    (59, "3cbc87c7681f34db4617feaa2c8801931bc5e42d8d0f560e756dd4cd92885f18", False),
    (99, "60a33e6cf5151f2d52eddae9685cfa270426aa89d8dbc7dfb854606f1d1a40fe", False),
    (199, "3cbc87c7681f34db4617feaa2c8801931bc5e42d8d0f560e756dd4cd92885f18", False),
    (200, "60a33e6cf5151f2d52eddae9685cfa270426aa89d8dbc7dfb854606f1d1a40fe", False)
]
def hashcode(n: int) -> str:
    return hashlib.sha256(str(n).encode('utf-8')).hexdigest()

@pytest.mark.parametrize("number, result, testcase", q2_testcases)
def test_q2(number, result, testcase):
    if testcase:
        assert is_prime(number) == result
    else:
        assert hashcode(is_prime(number)) == result