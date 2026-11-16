import hashlib
import os
import sys

import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.insert(0, os.path.dirname(__file__))
import q10
from _pw_runner import run_solution
from _pw_rules import validate_rules


q10_testcases = [
    ('kitten', 'KittEN', 0, True),
    ('spa ces', 'a ces', 2, True),
    ('kitten', 'sitting', 3, True),
    ('xyz', 'abc', 3, True),
    ('sTaLl', 'StaBle', 2, True),
    ('a b!ce', 'bacd', 4, True),
    ('dangerous', 'bingedous', 3, True),
    ('soap', 'ship', 2, True),
    ('protect', 'protest', 1, True),
    ('infect', 'ingest', 2, True),
    ('abc', 'axbcy', 3, True),

    ('space', 'pace', '6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b',
     False),
    ('pace', 'spaces', 'd4735e3a265e16eee03f59718b9b5d03019c07d8b6c51f90da3a666eec13ab35',
     False),
    ('yohsin', 'university',
     '2c624232cdd221771294dfbb310aca000a0df6ac8b66b696d90ef06fdefb64a3', False),
    ('university', 'yohsin',
     '2c624232cdd221771294dfbb310aca000a0df6ac8b66b696d90ef06fdefb64a3', False),
    ('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
     'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAb',
     '6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b', False),

    ('z', 'a' * 100, 'ad57366865126e55649ecb23ae1d48887544976efea46a48eb5d85a6eeb4d306', False),

]


def test_q10_rules():
    validate_rules(q10, 10)


@pytest.mark.parametrize('first_word, second_word, expected, visible', q10_testcases)
def test_q10(first_word, second_word, expected, visible):
    outcome = run_solution(10, 'word_distance', first_word, second_word)
    result = outcome.value
    assert outcome.result_type == 'int', 'Return the distance as an integer.'
    if visible:
        assert result == expected
    else:
        assert hashlib.sha256(str(result).encode('utf-8')).hexdigest() == expected
