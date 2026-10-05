import pytest
import hashlib
import ast
import inspect
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from q5 import same_pattern

def hashcode(value):
    return hashlib.sha256(str(value).encode("utf-8")).hexdigest()

q5_testcases = [
    # Visible Testcases
    ('foo', 'bar', False, True), 
    ('egg', 'add', True, True), 
    ('ab', 'cc', False, True), 
    ('aabb', 'ccdd', True, True), 
    
    # Hidden Testcases
    ('a', 'x', '3cbc87c7681f34db4617feaa2c8801931bc5e42d8d0f560e756dd4cd92885f18', False), 
    ('aa', 'bb', '3cbc87c7681f34db4617feaa2c8801931bc5e42d8d0f560e756dd4cd92885f18', False), 
    ('aa', 'bc', '60a33e6cf5151f2d52eddae9685cfa270426aa89d8dbc7dfb854606f1d1a40fe', False), 
    ('ab', 'cd', '3cbc87c7681f34db4617feaa2c8801931bc5e42d8d0f560e756dd4cd92885f18', False), 
    ('aabb', 'cccc', '60a33e6cf5151f2d52eddae9685cfa270426aa89d8dbc7dfb854606f1d1a40fe', False), 
    ('aabbcc', 'ddeeff', '3cbc87c7681f34db4617feaa2c8801931bc5e42d8d0f560e756dd4cd92885f18', False), 
    ('aabbcc', 'ddeeee', '60a33e6cf5151f2d52eddae9685cfa270426aa89d8dbc7dfb854606f1d1a40fe', False), 
    ('abb', 'cdd', '3cbc87c7681f34db4617feaa2c8801931bc5e42d8d0f560e756dd4cd92885f18', False), 
    ('abb', 'ccd', '60a33e6cf5151f2d52eddae9685cfa270426aa89d8dbc7dfb854606f1d1a40fe', False), 
    ('aab', 'ccd', '3cbc87c7681f34db4617feaa2c8801931bc5e42d8d0f560e756dd4cd92885f18', False), 
    ('aab', 'ccc', '60a33e6cf5151f2d52eddae9685cfa270426aa89d8dbc7dfb854606f1d1a40fe', False), 
    ('xxxyy', 'aaabb', '3cbc87c7681f34db4617feaa2c8801931bc5e42d8d0f560e756dd4cd92885f18', False), 
    ('xxxyy', 'aaaab', '60a33e6cf5151f2d52eddae9685cfa270426aa89d8dbc7dfb854606f1d1a40fe', False), 
    ('1122', 'aabb', '3cbc87c7681f34db4617feaa2c8801931bc5e42d8d0f560e756dd4cd92885f18', False), 
    ('!!@@', 'xxyy', '3cbc87c7681f34db4617feaa2c8801931bc5e42d8d0f560e756dd4cd92885f18', False), 
    ('abc', 'dee', '60a33e6cf5151f2d52eddae9685cfa270426aa89d8dbc7dfb854606f1d1a40fe', False)
]

@pytest.mark.parametrize("original_message, encoded_message, expected, visible", q5_testcases)
def test_q5(original_message, encoded_message, expected, visible):
    if visible:
        assert same_pattern(original_message, encoded_message) == expected
    else:
        assert hashcode(same_pattern(original_message, encoded_message)) == expected
