import hashlib
import os
import sys

import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.insert(0, os.path.dirname(__file__))
import q9
from _pw_runner import run_solution
from _pw_rules import validate_rules, assert_recursion_executed


q9_testcases = [
    ('aab', 'cck', 'acbk', True),
    ('act', 'sat', 'ascat', True),
    ('sSsiIi', 'tttaAa', 'stia', True),
    ('bcd', 'efg', 'becfdg', True),
    ('vvvv', 'vvvv', 'v', True),
    ('mmmm', 'nnnn', 'mn', True),
    ('AvTiS', 'TIsVA', 'atvitsivsa', True),
    ('aaaaBBBcccccDDDDDeeeeeffffggggghhhhiiiii', 'ttttssssQQQqaaaaVVVVVmmmmmnnnnoooopppppp',
     'atbscqdaevfmgnhoip', True),
    ('ttttttttttaaaaaaaaaaiiiiiiiisssssssssvvvvvvvvvvbbbbbbbbbbbb',
     'ccccccccccddddddddddeeeeeeeeeeffffffffffgggggggggghhhhhhhhh', 'tcadiesfvgbh', True),
    ('AAAAAAAAAAAAAAAAAAA', 'TTTTTTTTTTTTTTTTTTT', 'at', True),

    ('aab', 'cde', 'aa1eac30ff6cdab9011355be5ac7722b78be4802fb9056fbe371160fd4b045e9', False),
    ('aAb', 'Bcc', 'ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad', False),
    ('AAAAA', 'AAAAA', 'ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb', False),
    ('abBAAA', 'bbCCDD', 'e6d97e91189aa639cb1302c863097b4e1d2daf85b6ffe97cdd40fae742c67c56', False),
    ('AbAbAbAbAbAbAbAbAbAbAbAbAbAbAbAbAbAbAbAbAbAbAbAbAbAbAbAbAbAbAbAbAbAbAbAbAbAbAbAbAbAbAbAbAbAbAbAbAbAb',
     'CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC',
     '7e47f18950ff372a8e69f5ec453ac21b829f0503913e919187ba9ceffb76e9fd', False),

]


def test_q9_rules():
    validate_rules(q9, 9)


def test_q9_recursion_executed():
    assert_recursion_executed(q9, q9.create_scroll, ('aab', 'cck'))


@pytest.mark.parametrize('first_scroll, second_scroll, expected, visible', q9_testcases)
def test_q9(first_scroll, second_scroll, expected, visible):
    outcome = run_solution(9, 'create_scroll', first_scroll, second_scroll)
    result = outcome.value
    assert outcome.result_type == 'str', 'Return a string.'
    if visible:
        assert result == expected
    else:
        assert hashlib.sha256(str(result).encode('utf-8')).hexdigest() == expected
