import copy
import hashlib
import os
import sys

import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
sys.path.insert(0, os.path.dirname(__file__))

from q3 import partition_modulo_n


def hashcode(dictionary):
    return hashlib.sha256(repr(sorted(dictionary.items())).encode("utf-8")).hexdigest()


q3_testcases = [(3,
  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
  {0: [0, 3, 6, 9], 1: [1, 4, 7, 10], 2: [2, 5, 8, 11]},
  True),
 (3,
  [-6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5],
  '608587a697dec60a940fd7de9683c14d93789be2ede3cafe8b5045e3233040d5',
  False),
 (3,
  [17, 20, -16, 34, 28, 47, -49, 37, -43, -19, -8, 19],
  'bdb60988872b21b184caf4fec9dc3fc0af34f0a026523f9004ea13f2df99de4c',
  False),
 (3,
  [-50, 15, 29, 49, 18, -7, 42, -46, 10, -13, -44, 48],
  '338e20d23ad41cc699e15d68be139263d749619bb3c9eb0e9cac8055b2d58085',
  False),
 (3, [], {0: [], 1: [], 2: []}, True),
 (4,
  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
  {0: [0, 4, 8], 1: [1, 5, 9], 2: [2, 6, 10], 3: [3, 7, 11]},
  True),
 (4,
  [-6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5],
  'f5410d918e75d60ff7cb699d958f1c99b0bfa972d7febb16115d06187f4475dd',
  False),
 (4,
  [17, 20, -16, 34, 28, 47, -49, 37, -43, -19, -8, 19],
  '969d053c93acdf9665594c0de1f35b1f5879a8d201c8a294c872f8ec3cadad37',
  False),
 (4,
  [-50, 15, 29, 49, 18, -7, 42, -46, 10, -13, -44, 48],
  'b84f7b29bc2c1abd8b19e4584e047d1904d25bd70e9f1a5000163db189be49e6',
  False),
 (4, [], '3e723f91d4bdf6695bf9f1eacd2f62c603dbb51853afeb2e7be6676763e085da', False),
 (-4,
  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
  {-3: [1, 5, 9], -2: [2, 6, 10], -1: [3, 7, 11], 0: [0, 4, 8]},
  True),
 (-4,
  [-6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5],
  {-3: [-3, 1, 5], -2: [-6, -2, 2], -1: [-5, -1, 3], 0: [-4, 0, 4]},
  True),
 (-4,
  [17, 20, -16, 34, 28, 47, -49, 37, -43, -19, -8, 19],
  'd6e0b189bce9d392f5d93f02b7ae3511764cf3e2a26edd1389b1acf4d8a87866',
  False),
 (-4,
  [-50, 15, 29, 49, 18, -7, 42, -46, 10, -13, -44, 48],
  'b508728763924ef5a9eb2c2907bb41308621306b5e51bf4f50602b81a4ed9a1e',
  False),
 (-4, [], '1a582dfc82a75e1f568d9c554e9d669a39260beb13ddc5ca2d4769b5be86f90c', False)]


@pytest.mark.parametrize("divisor,numbers,expected,is_visible", q3_testcases)
def test_q3(divisor, numbers, expected, is_visible):
    before = copy.deepcopy(numbers)
    actual = partition_modulo_n(divisor, numbers)

    assert type(actual) is dict
    assert numbers == before
    if is_visible:
        assert actual == expected
    else:
        assert hashcode(actual) == expected

    # Additional visible examples printed in the worksheet PDF.
    # Included in existing visible tests to keep 15 parametrized test cases
    # and preserve all ten originally supplied hidden cases.
    if is_visible and divisor == 3 and numbers == list(range(12)):
        assert partition_modulo_n(3, [4, 7, -2]) == {0: [], 1: [4, 7, -2], 2: []}
    if is_visible and divisor == -4 and numbers == list(range(-6, 6)):
        assert partition_modulo_n(-4, [-6, -5, -4, -3, -2, -1, 0, 1]) == {
            -3: [-3, 1], -2: [-6, -2], -1: [-5, -1], 0: [-4, 0]
        }
