import pytest
import hashlib
import ast
import inspect
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from q3 import can_form_same_word

def hashcode(value):
    return hashlib.sha256(str(value).encode("utf-8")).hexdigest()

q3_testcases = [
    # Visible Testcases
    ('baba', True, True), 
    ('cbcba', False, True), 
    ('abca', False, True), 
    
    # Hidden Testcases
    ('a', '60a33e6cf5151f2d52eddae9685cfa270426aa89d8dbc7dfb854606f1d1a40fe', False), 
    ('aa', '3cbc87c7681f34db4617feaa2c8801931bc5e42d8d0f560e756dd4cd92885f18', False), 
    ('ab', '60a33e6cf5151f2d52eddae9685cfa270426aa89d8dbc7dfb854606f1d1a40fe', False), 
    ('aabb', '3cbc87c7681f34db4617feaa2c8801931bc5e42d8d0f560e756dd4cd92885f18', False),
    ('abab', '3cbc87c7681f34db4617feaa2c8801931bc5e42d8d0f560e756dd4cd92885f18', False),
    ('abcabc', '3cbc87c7681f34db4617feaa2c8801931bc5e42d8d0f560e756dd4cd92885f18', False),
    ('aabbcc', '3cbc87c7681f34db4617feaa2c8801931bc5e42d8d0f560e756dd4cd92885f18', False),
    ('aabbc', '60a33e6cf5151f2d52eddae9685cfa270426aa89d8dbc7dfb854606f1d1a40fe', False),
    ('zzzz', '3cbc87c7681f34db4617feaa2c8801931bc5e42d8d0f560e756dd4cd92885f18', False),
    ('abcddcba', '3cbc87c7681f34db4617feaa2c8801931bc5e42d8d0f560e756dd4cd92885f18', False),
    ('aabbbbcc', '3cbc87c7681f34db4617feaa2c8801931bc5e42d8d0f560e756dd4cd92885f18', False),
    ('abcd', '60a33e6cf5151f2d52eddae9685cfa270426aa89d8dbc7dfb854606f1d1a40fe', False),
    ('aaaaaa', '3cbc87c7681f34db4617feaa2c8801931bc5e42d8d0f560e756dd4cd92885f18', False),
    ('aaccbbdd', '3cbc87c7681f34db4617feaa2c8801931bc5e42d8d0f560e756dd4cd92885f18', False),
    ('abcabcdd', '3cbc87c7681f34db4617feaa2c8801931bc5e42d8d0f560e756dd4cd92885f18', False),
    ('mmnnoopp', '3cbc87c7681f34db4617feaa2c8801931bc5e42d8d0f560e756dd4cd92885f18', False),
    ('xyyx', '3cbc87c7681f34db4617feaa2c8801931bc5e42d8d0f560e756dd4cd92885f18', False)
]

@pytest.mark.parametrize("letters, expected, visible", q3_testcases)
def test_q3(letters, expected, visible):
    if visible:
        assert can_form_same_word(letters) == expected
    else:
        assert hashcode(can_form_same_word(letters)) == expected