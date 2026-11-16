import hashlib
import os
import sys

import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
sys.path.insert(0, os.path.dirname(__file__))
import q2
from _pw_runner import run_solution
from _pw_rules import validate_rules, assert_recursion_executed


q2_testcases = [
    ('ADD', 7172, 71725, True),
    ('ADD', 92011, 920113, True),
    ('VERIFY', 313370, True, True),
    ('VERIFY', 678291, False, True),

    ('ADD', 14, 'd6f0c71ef0c88e45e4b3a2118fcb83b0def392d759c901e9d755d0e879028727', False),
    ('ADD', 67890, '34f6ee350f892c89cfa2ae76f6dae8f34f423ab9fed893e01d8422aa54f7e25b', False),
    ('VERIFY', 172653, '3cbc87c7681f34db4617feaa2c8801931bc5e42d8d0f560e756dd4cd92885f18', False),
    ('VERIFY', 529197, '60a33e6cf5151f2d52eddae9685cfa270426aa89d8dbc7dfb854606f1d1a40fe', False),
    ('ADD', 0, '5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9', False),
    ('ADD', 5, '2fca346db656187102ce806ac732e06a62df0dbb2829e511a770556d398e1a6e', False),
    ('ADD', 1000000, 'dfa73f9264a72c077893423f8b32c476cc359b753af2e8934decfd7d135ec2e1', False),
    ('ADD', 99999999999, 'c9ad92e1a2a5f55f42f9227c087e66f7b1970feb9d4d1244994ce0a2a91f97f6', False),
    ('VERIFY', 70, '3cbc87c7681f34db4617feaa2c8801931bc5e42d8d0f560e756dd4cd92885f18', False),
    ('VERIFY', 1001, '3cbc87c7681f34db4617feaa2c8801931bc5e42d8d0f560e756dd4cd92885f18', False),
    ('VERIFY', 876543212, '60a33e6cf5151f2d52eddae9685cfa270426aa89d8dbc7dfb854606f1d1a40fe', False),
]



def test_q2_rules():
    validate_rules(q2, 2)


def test_q2_add_recursion_executed():
    assert_recursion_executed(q2, q2.add_check_digit, (7172,))


def test_q2_verify_recursion_executed():
    assert_recursion_executed(q2, q2.verify_check_digit, (678291,))


@pytest.mark.parametrize('operation, idnum, expected, visible', q2_testcases)
def test_q2(operation, idnum, expected, visible):
    if operation == 'ADD':
        outcome = run_solution(2, 'add_check_digit', idnum)
        result = outcome.value
        assert outcome.result_type == 'int', "add_check_digit must return an int."
    else:
        outcome = run_solution(2, 'verify_check_digit', idnum)
        result = outcome.value
        assert outcome.result_type == 'bool', "verify_check_digit must return a bool (True or False)."
    if visible:
        assert result == expected
    else:
        assert hashlib.sha256(str(result).encode("utf-8")).hexdigest() == expected
