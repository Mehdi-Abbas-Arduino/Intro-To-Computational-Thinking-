import hashlib
import os
import sys

import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.insert(0, os.path.dirname(__file__))
import q8
from _pw_runner import run_solution
from _pw_rules import validate_rules, assert_recursion_executed


q8_testcases = [
    ('aabbbaacd', 3, 'cd', True),
    ('aaa', 3, '', True),
    ('abbbcccaaa', 3, '', True),
    ('abcabc', 3, 'abcabc', True),
    ('aaabbaaac', 3, 'bbc', True),
    ('ababababa', 3, 'ababababa', True),
    ('aaaaabbbbcccccddddd', 3, '', True),
    ('abbcccbbba', 3, 'aa', True),
    ('z', 3, 'z', True),
    ('xxxyyyxxxyyyzzz', 3, '', True),

    ('acccbba', 3, 'e22115b5d76640e2389bcac25c46a2df03b2df657c5b3ff32cbaed141f8e8ef0', False),
    ('abbbaa', 3, 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855', False),
    ('dddde', 3, '3f79bb7b435b05321651daefd374cdc681dc06faa65e374e38337b88ca046dea', False),
    ('aabba', 2, 'ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb', False),
    ('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
     10, 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855', False),
    ('aaaabbbcccc', 4, '3e744b9dc39389baf0c5a0660589b8402f3dbb49b89b3e75f2c9355852a3c677', False),
    ('aaaaabbbbbccccc', 5, 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855', False),
    ('aaaabbbbcccccdddd', 4, 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855', False),
    ('aaabbbcccccccccdd', 9, '3d9dd9271faf6784b7aa7949c32db4912fcb988c0d3ec35a5b719dd54cf13eb1', False),
    ('aaaabbbbaaaa', 4, 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855', False),
    ('zzzaaaaaazzzz', 6, 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855', False),
    ('aabbcccddddd', 5, '3458b03d1da07c94ab27780590a6fd3bc7ae0ce61f1eeee0dedc01a6f8a3192a', False),
    ('abbbbccc', 4, 'aac5cafd87fd184e3665cf6b347b9a112f495158ff216f6bff45261fc29d9f0e', False),
    ('kkkkkkkk', 9, 'fa0422d5025ecfa96b9f58a222dc7422f2bdfa184e0880954e28563974e393a6', False),
    ('kkkkkkkkkk', 10, 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855', False),
    ('abbbbbbbbbcc', 9, '414322309db5c06d090a2e922ccc3e00708c993b9b96405de127b7fd8da2dd21', False),
    ('aaaabbbb', 5, 'e5c1edb50ff8b4fcc3ead3a845ffbe1ad51c9dae5d44335a5c333b57ac8df062', False),
    ('aabbbbaaaa', 4, 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855', False),
    ('aaaaabbbbbcccccc', 6, 'ed74b5c9ceaa577420d8ec549a9e55c9480ea02f6718c4095687f67e4ab220d4', False),
    ('aaaabbaa', 2, 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855', False),
    ('xxxxxxxy', 7, 'a1fce4363854ff888cff4b8e7875d600c2682390412a8cf79b37d0b11148b0fa', False),
    ('xxxxxxxxy', 8, 'a1fce4363854ff888cff4b8e7875d600c2682390412a8cf79b37d0b11148b0fa', False),
    ('xxxxxxxy', 8, '5fc573cb8951399d6656a5f2467c0448f98bea5bd12681f006adc2cec22a174c', False),
    ('xxxxxxxxy', 9, 'b3d942c28bcb98a148a4415e03afd163751479afc9ad71ce042e009d503f88dc', False),
    ('aaabbbcccccbbbaaa', 5, 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855', False),

]


def test_q8_rules():
    validate_rules(q8, 8)


def test_q8_recursion_executed():
    assert_recursion_executed(q8, q8.pop_bubbles, ('abbcccbbba', 3))


@pytest.mark.parametrize('bubbles, min_group_size, expected, visible', q8_testcases)
def test_q8(bubbles, min_group_size, expected, visible):
    outcome = run_solution(8, 'pop_bubbles', bubbles, min_group_size)
    result = outcome.value
    assert outcome.result_type == 'str', 'Return a string.'
    if visible:
        assert result == expected
    else:
        assert hashlib.sha256(str(result).encode('utf-8')).hexdigest() == expected
