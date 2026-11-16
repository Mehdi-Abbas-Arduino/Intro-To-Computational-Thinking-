import hashlib
import os
import sys

import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
sys.path.insert(0, os.path.dirname(__file__))
import q1
from _pw_runner import run_solution
from _pw_rules import validate_rules, assert_recursion_executed


q1_testcases = [
    (2322, 654, 6, True),
    (12, 8, 4, True),
    (287, 175, 7, True),
    (175, 287, 7, True),
    (98, 56, 14, True),

    (20, 28, '4b227777d4dd1fc61c6f884f48641d02b4d121d3fd328cb08b5531fcacdabf8a', False),
    (29, 233, '6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b', False),
    (5031, 387, '25dac95b8f595046bc435139636b0e2f1ff6e0ea31a54f3c19e7e726fb98738b', False),
    (24, 36, '6b51d431df5d7f141cbececcf79edf3dd861c3b4069f0b11661a3eefacbba918', False),
    (87808, 151875, '6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b', False),
    (10674846, 6174, '982cba6c0950686e37519d347bfa51deb9c933de7844a3800973b65d78c4667e', False),
    (0, 0, '5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9', False),
    (0, 9, '19581e27de7ced00ff1ce50b2047e7a567c76b1cbaebabe5ef03f7c3017bb5b7', False),
    (13, 0, '3fdba35f04dc8c462986c992bcf875546257113072a909c162f7e470e581e278', False),
    (832040, 514229, '6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b', False),
]



def test_q1_rules():
    validate_rules(q1, 1)


def test_q1_recursion_executed():
    assert_recursion_executed(q1, q1.gcd, (2322, 654))


@pytest.mark.parametrize('a, b, expected, visible', q1_testcases)
def test_q1(a, b, expected, visible):
    outcome = run_solution(1, 'gcd', a, b)
    result = outcome.value
    assert outcome.result_type == 'int', "Return an int."
    if visible:
        assert result == expected
    else:
        assert hashlib.sha256(str(result).encode("utf-8")).hexdigest() == expected
