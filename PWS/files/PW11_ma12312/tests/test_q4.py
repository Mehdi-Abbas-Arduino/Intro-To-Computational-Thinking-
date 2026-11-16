import hashlib
import os
import sys

import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
sys.path.insert(0, os.path.dirname(__file__))
import q4
from _pw_runner import run_solution
from _pw_rules import validate_rules, assert_recursion_executed


q4_testcases = [
    (2, 3, 5, 6, 1091, True),
    (1, 2, 0, 10, 512, True),
    (1, 2, 1, 8, 255, True),
    (3, 4, 2, 4, 234, True),
    (9, 15, 7, 1, 9, True),
    (2, 5, 0, 6, 6250, True),
    (1, 7, 1, 4, 400, True),
    (2, 5, 3, 5, 1718, True),
    (3, 4, 5, 6, 4777, True),
    (11, 23, 8, 1, 11, True),

    (0, 2, 0, 1, '5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9', False),
    (0, 1, 5, 100, 'ac1270c5058af65025e5b2a3e3014cea69460e7d9f159ae667028e1b6eab433e', False),
    (5, 1, 0, 100, 'ef2d127de37b942baad06145e54b0c619a1f22327b2ebbcfbec78f5564afe39d', False),
    (1, 2, 0, 100, '8f5054e678de19564136524adfd4016b201ac677ae0b92e8fd589ca5c7c8df88', False),
    (0, 3, 1, 7, 'b3dfdc6efe322a6feccb0d081e88ffac20b0f28e8495efa76188c8dc3ada6181', False),
]


def test_q4_rules():
    validate_rules(q4, 4)


def test_q4_recursion_executed():
    assert_recursion_executed(q4, q4.chickens_needed, (2, 3, 5, 6))


@pytest.mark.parametrize('starting_chickens, multiplier, bonus, level, expected, visible', q4_testcases)
def test_q4(starting_chickens, multiplier, bonus, level, expected, visible):
    outcome = run_solution(4, 'chickens_needed', starting_chickens, multiplier, bonus, level)
    result = outcome.value
    assert outcome.result_type == 'int', "Return an int."
    if visible:
        assert result == expected
    else:
        assert hashlib.sha256(str(result).encode("utf-8")).hexdigest() == expected
