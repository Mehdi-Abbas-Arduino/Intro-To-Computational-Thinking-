import copy
import hashlib
import os
import sys

import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
sys.path.insert(0, os.path.dirname(__file__))

from q1 import remove_user


def hashcode(users_data):
    normalized = [(name, profile[0], list(profile[1]))
                  for name, profile in sorted(users_data.items())]
    return hashlib.sha256(repr(normalized).encode("utf-8")).hexdigest()


q1_testcases = [({'Alice': ['123-456-7890', ['Bob', 'Charlie']],
   'Bob': ['987-654-3210', ['Alice', 'David']],
   'Charlie': ['111-222-3333', ['Alice']],
   'David': ['555-666-7777', ['Bob']]},
  'Alice',
  {'Bob': ['987-654-3210', ['David']],
   'Charlie': ['111-222-3333', []],
   'David': ['555-666-7777', ['Bob']]},
  True),
 ({'Alice': ['123-456-7890', []],
   'Bob': ['987-654-3210', ['Alice']],
   'Charlie': ['111-222-3333', ['Alice']],
   'David': ['555-666-7777', ['Bob']]},
  'Alice',
  {'Bob': ['987-654-3210', []], 'Charlie': ['111-222-3333', []], 'David': ['555-666-7777', ['Bob']]},
  True),
 ({'Alice': ['111', []], 'Bob': ['222', ['Alice']]}, 'Alice', {'Bob': ['222', []]}, True),
 ({'Bob': ['222', []]}, 'Eve', {'Bob': ['222', []]}, True),
 ({}, 'Eve', {}, True),
 ({'Alice': ['123-456-7890', ['Bob']],
   'Bob': ['987-654-3210', ['Alice']],
   'Charlie': ['111-222-3333', ['Alice']],
   'David': ['555-666-7777', ['Bob']]},
  'Eve',
  '5221f4844e2b635188e89a64b3e72ccffd5329935f93240a6d2f8585c048c2d6',
  False),
 ({'Alice': ['123-456-7890', ['Bob']]},
  'Alice',
  '4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945',
  False),
 ({'Alice': ['123-456-7890', ['Bob', 'Charlie']],
   'Bob': ['987-654-3210', ['Alice', 'David']],
   'Charlie': ['111-222-3333', ['Alice', 'Bob']],
   'David': ['555-666-7777', ['Bob', 'Charlie']]},
  'Alice',
  '8c4192f4562beac8d16d58d1104cf88b94d76ca66d0ba491986c19438466e892',
  False),
 ({'Lia': ['111', []]},
  'Lia',
  '4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945',
  False),
 ({'Umar': ['100', []], 'Sana': ['200', []]},
  'Sana',
  '0cf279f59bcf9bb9dd120036eae2236530877eeeb095aee069b95b0c50b9104f',
  False),
 ({'A': ['100', ['B', 'C']], 'B': ['200', ['A', 'C']], 'C': ['300', ['A']], 'D': ['400', ['B', 'C']]},
  'A',
  '013791ba4ac9675701e91d7b6be8f98ec213db2bfe761002f3a4dfd00a57eb26',
  False),
 ({'A': ['100', ['A', 'B']], 'B': ['200', ['A']], 'C': ['300', ['B', 'A']]},
  'A',
  'c3c7ecc49ada40456814e2c20c101ee2434e5d5b718859a2ad70d8390b0c1e38',
  False),
 ({'Alice': ['100', ['alice']], 'alice': ['200', ['Alice']], 'Bob': ['300', ['Alice', 'alice']]},
  'alice',
  '54ca9934498b944519fcbe9313fbe1db3f00d5a377017804d4d9b9ecf799fcff',
  False),
 ({'Noor': ['100', ['Ali', 'Zara']], 'Ali': ['200', ['Zara']], 'Zara': ['300', []]},
  'Noor',
  'cfe8a40f794b8503713c434c1f8c5c36491d0b8e8ade774413c7f092c03fd0ac',
  False),
 ({'Tara': ['1', ['Mia', 'Leo']],
   'Mia': ['2', ['Leo', 'Tara', 'Zoe']],
   'Leo': ['3', ['Tara', 'Zoe']],
   'Zoe': ['4', ['Tara', 'Mia']],
   'Ria': ['5', ['Mia', 'Tara', 'Zoe']]},
  'Tara',
  '7fdad96e4cfbafaa1e9042c98e0a35524e8a86b07138ebbd76bbd51d1bd1c194',
  False)]


@pytest.mark.parametrize("user_profiles,username,expected,is_visible", q1_testcases)
def test_q1(user_profiles, username, expected, is_visible):
    original_dictionary = user_profiles
    actual = remove_user(user_profiles, username)

    assert actual is original_dictionary
    if is_visible:
        assert actual == expected
    else:
        assert hashcode(actual) == expected
