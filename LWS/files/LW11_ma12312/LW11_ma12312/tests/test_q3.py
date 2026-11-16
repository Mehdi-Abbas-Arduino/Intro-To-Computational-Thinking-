import copy
import hashlib
import os
import sys

import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.insert(0, os.path.dirname(__file__))
import q3
from _lw11_rules import validate_rules, assert_recursion_executed


q3_testcases = [
    # Visible testcases
    (['how', 'is', 'it', 'going', 'this', 'morning', 'mr', 'browning'], ['going', 'morning', 'browning'], True),
    (['ing', 'in', 'king'], ['ing', 'king'], True),
    (['is', 'it', 'in'], [], True),
    ([], [], True),
    (['going', 'doing', 'going'], ['going', 'doing', 'going'], True),
    (['singing', 'morning', 'singer', 'ings'], ['singing', 'morning'], True),

    # Hidden testcases
    (['ing'], 'd3b2f91417e3d3cc9278d51cb1980592231891f3aa386837849e08e3b7376298', False),
    (['i', 'in', 'inn', 'interesting', 'ing'], '72aac87c0391e33989ccd2e1f9ebf577c95495a1d4e9bf67eef7af3908ec57b2', False),
    (['nothing', 'something', 'anything'], '63a98aa9ee01f6c14910f7c2387e77ab048b1ade7199587f7dd5d6410ee282ea', False),
    (['thing', 'things', 'thinking', 'think'], '434d06c66c6a06ef93506930c5f493f3cd364219b619841976c0c4567c8a4fe9', False),
    (['a', 'b', 'c', 'd'], '4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945', False),
    (['ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing', 'ing'], '3a607f42cedd22360fa09059a1883b3183e9a985bd3364cc09730a9bfc6d5acc', False),
    (['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'ring'], '4a0121f794fdebaeb24ebe3dda0a822e21be721277cc536ab9bebe08407f75c3', False),
    (['king', 'swing', 'ping', 'zing', 'king', 'swing', 'ping', 'zing', 'king', 'swing', 'ping', 'zing', 'king', 'swing', 'ping', 'zing', 'king', 'swing', 'ping', 'zing', 'king', 'swing', 'ping', 'zing', 'king', 'swing', 'ping', 'zing', 'king', 'swing', 'ping', 'zing', 'king', 'swing', 'ping', 'zing', 'king', 'swing', 'ping', 'zing', 'king', 'swing', 'ping', 'zing', 'king', 'swing', 'ping', 'zing', 'king', 'swing', 'ping', 'zing', 'king', 'swing', 'ping', 'zing', 'king', 'swing', 'ping', 'zing', 'king', 'swing', 'ping', 'zing', 'king', 'swing', 'ping', 'zing', 'king', 'swing', 'ping', 'zing', 'king', 'swing', 'ping', 'zing', 'king', 'swing', 'ping', 'zing', 'king', 'swing', 'ping', 'zing', 'king', 'swing', 'ping', 'zing', 'king', 'swing', 'ping', 'zing', 'king', 'swing', 'ping', 'zing', 'king', 'swing', 'ping', 'zing', 'king', 'swing', 'ping', 'zing', 'king', 'swing', 'ping', 'zing', 'king', 'swing', 'ping', 'zing', 'king', 'swing', 'ping', 'zing', 'king', 'swing', 'ping', 'zing', 'king', 'swing', 'ping', 'zing', 'king', 'swing', 'ping', 'zing', 'king', 'swing', 'ping', 'zing', 'king', 'swing', 'ping', 'zing', 'king', 'swing', 'ping', 'zing', 'king', 'swing', 'ping', 'zing', 'king', 'swing', 'ping', 'zing', 'king', 'swing', 'ping', 'zing', 'king', 'swing', 'ping', 'zing', 'king', 'swing', 'ping', 'zing', 'king', 'swing', 'ping', 'zing', 'king', 'swing', 'ping', 'zing', 'king', 'swing', 'ping', 'zing', 'king', 'swing', 'ping', 'zing', 'king', 'swing', 'ping', 'zing', 'king', 'swing', 'ping', 'zing', 'king', 'swing', 'ping', 'zing', 'king', 'swing', 'ping', 'zing', 'king', 'swing', 'ping', 'zing', 'king', 'swing', 'ping', 'zing', 'king', 'swing', 'ping', 'zing', 'king', 'swing', 'ping', 'zing', 'king', 'swing', 'ping', 'zing', 'king', 'swing', 'ping', 'zing', 'king', 'swing', 'ping', 'zing', 'king', 'swing', 'ping', 'zing', 'king', 'swing', 'ping', 'zing', 'king', 'swing', 'ping', 'zing', 'king', 'swing', 'ping', 'zing', 'king', 'swing', 'ping', 'zing', 'king', 'swing', 'ping', 'zing', 'king', 'swing', 'ping', 'zing', 'king', 'swing', 'ping', 'zing', 'king', 'swing', 'ping', 'zing', 'king', 'swing', 'ping', 'zing', 'king', 'swing', 'ping', 'zing', 'king', 'swing', 'ping', 'zing', 'king', 'swing', 'ping', 'zing', 'king', 'swing', 'ping', 'zing', 'king', 'swing', 'ping', 'zing', 'king', 'swing', 'ping', 'zing', 'king', 'swing', 'ping', 'zing', 'king', 'swing', 'ping', 'zing', 'king', 'swing', 'ping', 'zing', 'king', 'swing', 'ping', 'zing'], '3ce3afe001f54b56546195878bdaf9c5eb2240d0a441985fc12e151dc9719871', False),
    (['ings', 'playing', 'kingdom', 'ring', 'bring', 'doing', 'bringing', 'browning'], '112f66f5af60d63a613ec6b88272608c4513ebaaf01b6e00f116d3b8ed55fea2', False),
]


def test_q3_rules():
    validate_rules(q3, 3)


def test_q3_recursion_executed():
    assert_recursion_executed(q3, q3.find_ing_words, (['going', 'morning', 'browning'],))


@pytest.mark.parametrize('words, expected, visible', q3_testcases)
def test_q3(words, expected, visible):
    original = copy.deepcopy(words)
    result = q3.find_ing_words(words)
    assert isinstance(result, list), (
        f"Wrong return type. Actual: {type(result).__name__}; Expected: list.")
    assert result is not words, 'Return a new list, not the original input list.'
    assert words == original, 'Do not modify the original words list.'
    if visible:
        assert result == expected, (
            f"Return value mismatch.\nActual: {result!r}\nExpected: {expected!r}")
    else:
        actual_hash = hashlib.sha256(str(result).encode('utf-8')).hexdigest()
        assert actual_hash == expected, (
            'Incorrect return value for a hidden case.\n'
            f"Actual: {repr(result)[:240]}{'...' if len(repr(result)) > 240 else ''}\n"
            'Expected return value: hidden\n'
            f"Actual SHA-256: {actual_hash}\nExpected SHA-256: {expected}")