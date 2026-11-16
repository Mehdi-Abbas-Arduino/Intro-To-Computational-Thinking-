import hashlib
import os
import sys

import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from q4 import are_anagrams


def hashcode(text):
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


q4_testcases = [
    ('Stressed?', 'Desserts!!!!',
     "{'d': 1, 'e': 2, 'r': 1, 's': 3, 't': 1}\n{'d': 1, 'e': 2, 'r': 1, 's': 3, 't': 1}\nAnagrams", True),
    ('Stressed?', 'Dessert.',
     "{'d': 1, 'e': 2, 'r': 1, 's': 3, 't': 1}\n{'d': 1, 'e': 2, 'r': 1, 's': 2, 't': 1}\nNot anagrams", True),
    ('Snooze alarms.', "Alas! No more Z's. =(",
     "{'a': 2, 'e': 1, 'l': 1, 'm': 1, 'n': 1, 'o': 2, 'r': 1, 's': 2, 'z': 1}\n{'a': 2, 'e': 1, 'l': 1, 'm': 1, 'n': 1, 'o': 2, 'r': 1, 's': 2, 'z': 1}\nAnagrams", True),
    ('Snooze alarm.', "Alas! No more Z's. =(",
     "{'a': 2, 'e': 1, 'l': 1, 'm': 1, 'n': 1, 'o': 2, 'r': 1, 's': 1, 'z': 1}\n{'a': 2, 'e': 1, 'l': 1, 'm': 1, 'n': 1, 'o': 2, 'r': 1, 's': 2, 'z': 1}\nNot anagrams", True),
    ('The eye...', '... it sees!',
     "{'e': 3, 'h': 1, 't': 1, 'y': 1}\n{'e': 2, 'i': 1, 's': 2, 't': 1}\nNot anagrams", True),
    ('123!', '...',
     '{}\n{}\nAnagrams', True),
    ('Dormitory?', 'Dirty room!',
     'dbb583521713509fcd55c14a9bc7e226ea5a053336dfee8da729d5751f88b5f5', False),
    ('a', 'b',
     '600b39ff1fc01db0a45afb818781df748859301fea5155af13ea7ac24c47495b', False),
    ('Eleven plus two?', 'Twelve plus one.',
     'f3a6cf70f67408f08df7dbb34d4e97a6e1ba04eadf19e4edc91c8af256159fee', False),
    ('A', 'a',
     '35216b3c8f12b80e58a5be0322f1cd1f59ffa6f3606dc5f343e9d866405e316e', False),
    ('Vacation time...', 'I am not active!',
     'd4fa9c4267c27ea01f4834d8924f504c83d8b8b971de4af495615063b3b4a5f3', False),
    ('abc 123', 'C-b-a!!',
     '1d2d34761807c4be5de8eb379dfb427783a47490a0586edc3af60154c79eef29', False),
    ('x x y', 'x y',
     '759b40831720639ba551e444d6dab5f0dc73ffc602e35ce21b9fedc63a348b62', False),
    ('10', '123!',
     '89b09fc612db2a19ee6c48be5214f910dac2058ec260eaba63146fc85b0ab483', False),
    ('ABC', '',
     '1d062a36ae0a8c5f73e7629b43c32d7d1a35e46674f20c8a3d4ba29b50a429ea', False),
]


@pytest.mark.parametrize("first_phrase, second_phrase, expected, visible", q4_testcases)
def test_q4(capsys, first_phrase, second_phrase, expected, visible):
    are_anagrams(first_phrase, second_phrase)
    captured_output = capsys.readouterr().out.rstrip('\n')
    if visible:
        assert captured_output == expected
    else:
        assert hashcode(captured_output) == expected
