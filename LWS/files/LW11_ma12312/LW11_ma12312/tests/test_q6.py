import hashlib
import os
import sys
import copy

import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
sys.path.insert(0, os.path.dirname(__file__))
import q6
from _lw11_rules import validate_rules, assert_recursion_executed


q6_testcases = [
    # Visible testcases
    ([1, 2, 3, 4, 5], 2, [9, 6], True),
    ([1, 2, 3, 4, 5], 3, [5, 7, 3], True),
    ([1, 2, 3], 5, [1, 2, 3, 0, 0], True),
    ([], 3, [0, 0, 0], True),
    ([4, 5, 6, 7], 1, [22], True),
    ([3] * 300, 4, [225, 225, 225, 225], True),

    # Hidden testcases
    ([], 1, 'd0bca111f8628137adc4c16f123496dcdd1d590d06cb5d9acd68b39fe656fb97', False),
    ([20], 50, 'e24cc1d7c25e8a50eed4db45e3867fdeb0b112c263e45feca9cc1dd4401ffb78', False),
    ([1, 20, 2, 19, 3, 18, 4], 3, 'f01ebf169664260cb98672a59b6cafe6fe2968f4df687ca6ef0beb140da270e6', False),
    ([20] * 300, 50, '33757cd48404bcf8e227ccb296b1ee357199101806d6dffd60c2e75d58bae4e0', False),
    ([1] * 299, 7, '2df1b8022150dd223d35c39e5cf1936fb7143817822600e0ca2d15a0e1733019', False),
    ([3, 10, 7, 1, 20, 1, 5, 13, 16, 2, 11], 4, '9f1bbee750dfe3b24a36b9893ff723188abf78d7cac429363c2e75dd0f4a7238', False),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10, '047c3537400c225da832d4d7dc924b01a3c0bac65ce23c5dcf182f4dd6895e73', False),
    ([5] * 50, 1, '997829838bafa8a23b0559a15318bb2c9ba221574c1c5402934c1ac6555e2873', False),
    (list(range(1, 21)) * 15, 9, 'e1a950eeb1ae2c6613269b4d275a8d646ebc3c9e22bbf0239abe35c01e9d7992', False),
]



def test_q6_rules():
    validate_rules(q6, 6)


def test_q6_recursion_executed():
    assert_recursion_executed(q6, q6.hours_per_member, ([1, 2, 3, 4, 5], 2))


@pytest.mark.parametrize('task_hours, member_count, expected, visible', q6_testcases)
def test_q6(task_hours, member_count, expected, visible):
    original = copy.deepcopy(task_hours)
    result = q6.hours_per_member(task_hours, member_count)
    assert isinstance(result, list), "Return a list."
    assert task_hours == original, "Do not modify task_hours."
    assert len(result) == member_count, "Return one total per member."
    if visible:
        assert result == expected
    else:
        assert hashlib.sha256(str(result).encode("utf-8")).hexdigest() == expected
