import hashlib
import os
import sys

import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
sys.path.insert(0, os.path.dirname(__file__))
import q5
from _lw11_rules import validate_rules, assert_recursion_executed


q5_testcases = [
    # Visible testcases
    (2345, True, True),
    (3245, False, True),
    (2582, False, True),
    (7, False, True),
    (2, True, True),
    (4101, True, True),
    (22, False, True),
    (23, True, True),
    (230, True, True),

    # Hidden testcases
    (42, "60a33e6cf5151f2d52eddae9685cfa270426aa89d8dbc7dfb854606f1d1a40fe", False),
    (810, "3cbc87c7681f34db4617feaa2c8801931bc5e42d8d0f560e756dd4cd92885f18", False),
    (222, "60a33e6cf5151f2d52eddae9685cfa270426aa89d8dbc7dfb854606f1d1a40fe", False),
    (270, "3cbc87c7681f34db4617feaa2c8801931bc5e42d8d0f560e756dd4cd92885f18", False),
    (896785432, "3cbc87c7681f34db4617feaa2c8801931bc5e42d8d0f560e756dd4cd92885f18", False),
    (1000000000, "60a33e6cf5151f2d52eddae9685cfa270426aa89d8dbc7dfb854606f1d1a40fe", False),
 ]



def test_q5_rules():
    validate_rules(q5, 5)


def test_q5_recursion_executed():
    assert_recursion_executed(q5, q5.is_winning_ticket, (2345,))


@pytest.mark.parametrize('ticket_number, expected, visible', q5_testcases)
def test_q5(ticket_number, expected, visible):
    result = q5.is_winning_ticket(ticket_number)
    assert type(result) is bool, "Return a bool."
    if visible:
        assert result == expected
    else:
        assert hashlib.sha256(str(result).encode("utf-8")).hexdigest() == expected
