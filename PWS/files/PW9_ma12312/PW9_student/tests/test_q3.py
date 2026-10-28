import hashlib
import os
import sys
from copy import deepcopy

import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from q3 import dostiyaariXI


def hashcode(value):
    return hashlib.sha256(str(value).encode("utf-8")).hexdigest()


q3_testcases = [
    (
        [
            'quddusi', 'swifthyderabad', 'CEmajorAT', 'skibidiali', 'valverde',
            'baqir', 'ronaldo', 'hassan', 'alonso', 'etoo',
            'mrgreedy', 'mbappe', 'messi', 'evra', 'mraura',
            'amir', 'mufaddal', 'isco', 'saifibhai', 'iniesta',
            'abdullah', 'hussainshah', 'askarizz', 'basim', 'raphina',
            'usman', 'coldp@lm4r',
        ],
        [
            ['alonso', 'etoo', 'evra', 'iniesta', 'isco'],
            ['abdullah', 'amir', 'askarizz', 'mbappe', 'messi',
             'mraura', 'quddusi', 'raphina', 'ronaldo', 'saifibhai',
             'skibidiali', 'usman', 'valverde'],
            ['CEmajorAT', 'baqir', 'basim', 'coldp@lm4r', 'hassan',
             'hussainshah', 'mrgreedy', 'mufaddal', 'swifthyderabad'],
        ],
        True,
    ),
    (
        [
            'Ava', 'Amir', 'Bilal', 'O',
        ],
        [
            ['Ava', 'O'],
            ['Amir'],
            ['Bilal'],
        ],
        True,
    ),
    (
        [],
        [
            [],
            [],
            [],
        ],
        True,
    ),
    (
        [
            'quddusi', 'swifthyderabad', 'CEmajorAT', 'skibidiali', 'valverde',
            'baqir', 'ronaldo', 'hassan', 'alonso', 'etoo',
            'mrgreedy', 'mbappe', 'messi', 'evra', 'mraura',
            'amir', 'mufaddal', 'isco', 'saifibhai', 'iniesta',
            'abdullah', 'babarazam', 'hussainshah', 'askarizz', 'basim',
            'raphina', 'usman', 'coldp@lm4r',
        ],
        [
            ['alonso', 'etoo', 'evra', 'iniesta', 'isco'],
            ['abdullah', 'amir', 'askarizz', 'mbappe', 'messi',
             'mraura', 'quddusi', 'raphina', 'ronaldo', 'saifibhai',
             'skibidiali', 'usman', 'valverde'],
            ['CEmajorAT', 'babarazam', 'baqir', 'basim', 'coldp@lm4r',
             'hassan', 'hussainshah', 'mrgreedy', 'mufaddal', 'swifthyderabad'],
        ],
        True,
    ),
    (
        [
            'amir', 'babarazam', 'otto', 'ali', 'saifibhai',
            'hassan', 'evra', 'mrgreedy', 'mraura', 'etoo',
            'alonso', 'messi', 'ronaldo', 'usman', 'abdullah',
            'mbappe', 'quddusi', 'skibidiali', 'valverde', 'coldp@lm4r',
            'askari', 'babarazam', 'faheem', 'leo', 'nash',
            'tito', 'zio', 'O_o', 'u2u', 'EVE',
            'ae', 'Ai',
        ],
        [
            ['Ai', 'EVE', 'O_o', 'ae', 'ali',
             'alonso', 'askari', 'etoo', 'evra', 'otto',
             'u2u'],
            ['abdullah', 'amir', 'leo', 'mbappe', 'messi',
             'mraura', 'quddusi', 'ronaldo', 'saifibhai', 'skibidiali',
             'tito', 'usman', 'valverde', 'zio'],
            ['babarazam', 'babarazam', 'coldp@lm4r', 'faheem', 'hassan',
             'mrgreedy', 'nash'],
        ],
        True,
    ),
    (
        [
            'ae', 'Ai', 'aoa', 'u2u', 'EVE',
            'eve', 'EVA', 'iZZi', 'usman', 'mufaddal',
            'faheem', 'coldp@lm4r', 'mrgreedy', 'mraura', 'Amira',
            'apollo', 'babarazam', 'AAA', 'Ali', 'otto',
            'iso', 'eko', 'e3e', 'O_o', 'babarazam',
            'aeIOU', 'ae', 'ooo', 'uu', 'ii',
        ],
        [
            ['AAA', 'Ai', 'Ali', 'Amira', 'EVA',
             'EVE', 'O_o', 'ae', 'ae', 'aeIOU',
             'aoa', 'apollo', 'e3e', 'eko', 'eve',
             'iZZi', 'ii', 'iso', 'ooo', 'otto',
             'u2u', 'uu'],
            ['mraura', 'usman'],
            ['babarazam', 'babarazam', 'coldp@lm4r', 'faheem', 'mrgreedy',
             'mufaddal'],
        ],
        True,
    ),
    (
        [
            'ronaldo', 'Messi', 'Mbappe', 'Neymar', 'Xavi',
            'Iniesta', 'Lewandowski', 'benzema', 'messi', 'Haaland',
            'babarazam', 'abc', 'amir', 'otto', 'ali',
            'EVE', 'saif', 'usman', 'evra', 'hassan',
            'mehmood', 'ramos', 'gavi', 'pedri', 'isco',
            'rafa', 'mrgreedy', 'leo', 'tito', 'O_o',
            'u2u', 'Ae', 'AAA', 'AE', 'EVE',
        ],
        [
            ['AAA', 'AE', 'Ae', 'EVE', 'EVE',
             'Iniesta', 'O_o', 'ali', 'evra', 'isco',
             'otto', 'u2u'],
            ['Lewandowski', 'Mbappe', 'Messi', 'Xavi', 'abc',
             'amir', 'benzema', 'gavi', 'leo', 'messi',
             'pedri', 'rafa', 'ronaldo', 'tito', 'usman'],
            ['Haaland', 'Neymar', 'babarazam', 'hassan', 'mehmood',
             'mrgreedy', 'ramos', 'saif'],
        ],
        True,
    ),
    (
        [
            'AE', 'aeiou', 'eve', 'apollo', 'skibidiali',
            'hEllo', 'usman', 'faheem', 'meow', 'baqir',
            'mraura', 'saifibhai', 'coldp@lm4r', 'iniesta', 'abdullah',
            'ronaldo', 'alonso', 'etoo', 'valverde', 'messi',
            'babarazam', 'A2A', 'EVE', 'otto', 'ae',
            'uSU', 'O_o', 'Ai', 'Ali',
        ],
        [
            ['A2A', 'AE', 'Ai', 'Ali', 'EVE',
             'O_o', 'ae', 'aeiou', 'alonso', 'apollo',
             'etoo', 'eve', 'iniesta', 'otto', 'uSU'],
            ['abdullah', 'hEllo', 'messi', 'mraura', 'ronaldo',
             'saifibhai', 'skibidiali', 'usman', 'valverde'],
            ['babarazam', 'baqir', 'coldp@lm4r', 'faheem', 'meow'],
        ],
        True,
    ),
    (
        [
            'adam', 'eve', 'isa', 'ozu', 'uma',
            'zuzu', 'otto', 'ali', 'Oscar', 'erik',
            'ian', 'aaron', 'ellen', 'bob', 'babarazam',
            'ae', 'aeiou', 'mufaddal', 'skibidiali', 'saifibhai',
            'quddusi', 'ronaldo', 'abdullah', 'coldp@lm4r', 'evee',
            'leo', 'O_o', 'uuu',
        ],
        '01da63800e424269548ec408e8a2b8494256adc2128c2ac95ef095620af6371b',
        False,
    ),
    (
        [
            'amir', 'Ali', 'bob', 'babarazam', 'Oreo',
            'oreo', 'EVA', 'eve', 'ae', 'uzi',
            'apollo', 'usa', 'faheem', 'otto', 'EEE',
            'skibidiali', 'MUFADDAL', 'coldp@lm4r', 'AE', 'AAA',
            'aeiou', 'EVE', 'ISA', 'OBE', 'ABE',
            'zohaib', 'irfan', 'usman', 'leona', 'neymar',
            'messi', 'iniesta', 'valverde', 'ronaldo', 'mbappe',
            'abdullah',
        ],
        '077a6929b6bf555fd31b72a653d6a65f7dd6158ca2c3f31d99e5b7ddfa910c72',
        False,
    ),
    (
        [
            'AE', 'O_o', 'e3e', 'coldp@lm4r', 'aeIOU',
            'ae', 'Ai', 'otto', 'EVE', 'eee',
            'uSU', 'babarazam', 'BOB', 'Ali@', 'mrgreedy',
            'skibidiali', 'uuu', 'leo', 'tito', 'Ae',
            'iii', 'ooO', 'uuU', 'babarazam',
        ],
        'a9ddd7715e13865eee8225eb83a7515c594daf3a8bb8f3c35565ef112bc15a07',
        False,
    ),
    (
        [
            'ronaldo', 'Messi', 'mbappe', 'neymar', 'hassan',
            'amir', 'hussainshah', 'alonso', 'etoo', 'valverde',
            'kaka', 'isco', 'rafa', 'evra', 'abdullah',
            'usman', 'faheem', 'iniesta', 'babarazam', 'mrgreedy',
            'mraura', 'zizo', 'EVE', 'otto', 'ae',
            'Ali', 'Oscar', 'baqir', 'coldp@lm4r', 'leo',
            'O_o', 'u2u',
        ],
        '05b886c3ec322473745910d6b6231993c26ed972431e822eebfa3a52c11e3272',
        False,
    ),
    (
        [
            'ae', 'Ai', 'aoa', 'u2u', 'EVE',
            'eve', 'EVA', 'iZZi', 'usman', 'mufaddal',
            'faheem', 'coldp@lm4r', 'mrgreedy', 'mraura', 'Amira',
            'apollo', 'babarazam', 'AAA', 'Ali', 'otto',
            'iso', 'eko', 'e3e', 'O_o', 'babarazam',
            'aeIOU', 'ae', 'ooo', 'uu', 'ii',
            'leo', 'tito', 'skibidiali', 'messi', 'ronaldo',
        ],
        'fa15b983c5694100fe530136e8f1b4618e774739cbc79130266e398d39b1fdbb',
        False,
    ),
    (
        [
            'A', 'E', 'I', 'O', 'U',
            'Amir', 'Omar', 'Ayesha', 'Bilal', 'Mariam',
            'BaA', 'Meow', 'Cecilia', 'A2A', 'eVe',
        ],
        'f35800ed8da27ec7c99b088fe0fa313cd2da964076de7cebe3c1eb893384b235',
        False,
    ),
    (
        [
            'A', 'O', 'e3e', 'Ali', 'aa',
            'baa', 'BaA', 'BOB', 'I', 'eve',
        ],
        '826eb3025459c290c03d7491434ade7099331722ee62ddcdfe85c5d091188347',
        False,
    ),
]


@pytest.mark.parametrize("player_names, expected, visible", q3_testcases)
def test_q3(player_names, expected, visible):
    original_names = deepcopy(player_names)
    actual = dostiyaariXI(player_names)
    assert player_names == original_names, (
        "The original player_names list must not be modified."
    )
    assert isinstance(actual, list) and len(actual) == 3, (
        "dostiyaariXI must return a list containing exactly three lists."
    )
    assert all(isinstance(group, list) for group in actual), (
        "Each category must be a list."
    )
    if visible:
        assert actual == expected, f"{actual!r} != {expected!r}"
    else:
        assert hashcode(actual) == expected, (
            "Incorrect player categories for this hidden test case."
        )