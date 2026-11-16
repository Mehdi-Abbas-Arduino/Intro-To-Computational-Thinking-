import hashlib
import os
import sys

import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
sys.path.insert(0, os.path.dirname(__file__))
import q1
from _lw11_rules import validate_rules, assert_recursion_executed


q1_testcases = [
    # Visible testcases
    ('recursion', 'rcrsn', True),
    ('Defenestrate', 'Dfnstrt', True),
    ('Orange', 'rng', True),
    ('The quick brown fox jumps over the lazy dog.', 'Th qck brwn fx jmps vr th lzy dg.', True),
    ('', '', True),
    ('AI in 2026!', ' n 2026!', True),
    ('AEIOUaeiou', '', True),
    ('Python Programming', 'Pythn Prgrmmng', True),
    ('Why so serious?', 'Why s srs?', True),

    # Hidden testcases
    ('I owe you a ewe.', '44898cdb9d5ce6fe69e02a3c33714385d8b318c3ebc16810931cf3f77ab7aeb3', False),
    ('Supercalifragilisticexpialidocious', '62bb4af1fb8cf1716a23acff9c5e7e65c021f9cef96e9bd98dc816daef7a66ff', False),
    ('12345 AEIOU and symbols!@#$', '2edc2a608fbe7b2bf4d4209842617671ae4e5efe907e0bceaed564d6f0b7aaaa', False),
    ('Recursive tests are fun!!!', '99724b63d0b2340b351d3ecb5ea1130beb0d8021d328f83a6ad71e78421a5b1c', False),
    ('a e i o u A E I O U', '670af646a34cdc2a616874dc29d30abc2b5523cc091c081c25a2e51079484b9c', False),
    ('Ab' * 250, '4b6864de8563969279cb13b1bcbab4541ba7c42b72f007ae0a503d891eb4ae33', False),
]



def test_q1_rules():
    validate_rules(q1, 1)


def test_q1_recursion_executed():
    assert_recursion_executed(q1, q1.remove_vowels, ('recursion',))


@pytest.mark.parametrize('text, expected, visible', q1_testcases)
def test_q1(text, expected, visible):
    result = q1.remove_vowels(text)
    assert isinstance(result, str), "Return a str."
    if visible:
        assert result == expected
    else:
        assert hashlib.sha256(result.encode("utf-8")).hexdigest() == expected
