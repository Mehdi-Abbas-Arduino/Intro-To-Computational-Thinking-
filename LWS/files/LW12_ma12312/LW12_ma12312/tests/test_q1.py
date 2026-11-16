import hashlib
import os
import sys

import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from q1 import print_dates_in_long_form

def hashcode(output):
    return hashlib.sha256(output.encode('utf-8')).hexdigest()

q1_testcases = [

    ([{'day': 12, 'month': 12, 'year': 1996},
 {'day': 8, 'month': 12, 'year': 1995},
 {'day': 30, 'month': 4, 'year': 1999}],
     'December 12, 1996\nDecember 8, 1995\nApril 30, 1999', True),

    ([{'year': 1996, 'month': 12, 'day': 12},
 {'year': 1995, 'month': 12, 'day': 8},
 {'year': 1999, 'month': 4, 'day': 30},
 {'year': 1998, 'month': 7, 'day': 30}],
     'December 12, 1996\nDecember 8, 1995\nApril 30, 1999\nJuly 30, 1998', True),

    ([{'year': 1996, 'month': 12, 'day': 12},
 {'year': 1995, 'month': 12, 'day': 8},
 {'year': 1999, 'month': 4, 'day': 30},
 {'year': 1998, 'month': 4, 'day': 30}],
     'December 12, 1996\nDecember 8, 1995\nApril 30, 1999\nApril 30, 1998', True),

    ([{'year': 1995, 'month': 8, 'day': 3},
 {'year': 1994, 'month': 7, 'day': 15},
 {'year': 1997, 'month': 3, 'day': 17},
 {'year': 1995, 'month': 10, 'day': 17},
 {'year': 1999, 'month': 3, 'day': 7},
 {'year': 1995, 'month': 6, 'day': 4},
 {'year': 1994, 'month': 4, 'day': 29},
 {'year': 1999, 'month': 5, 'day': 18},
 {'year': 1994, 'month': 7, 'day': 3},
 {'year': 1994, 'month': 8, 'day': 7},
 {'year': 1999, 'month': 4, 'day': 5},
 {'year': 1998, 'month': 9, 'day': 30}],
     'August 3, 1995\nJuly 15, 1994\nMarch 17, 1997\nOctober 17, 1995\nMarch 7, 1999\nJune 4, 1995\nApril 29, 1994\nMay 18, 1999\nJuly 3, 1994\nAugust 7, 1994\nApril 5, 1999\nSeptember 30, 1998', True),

    ([{'year': 1998, 'month': 8, 'day': 24},
 {'year': 1999, 'month': 4, 'day': 22},
 {'year': 1996, 'month': 3, 'day': 2},
 {'year': 1995, 'month': 5, 'day': 19},
 {'year': 1998, 'month': 6, 'day': 14},
 {'year': 1999, 'month': 5, 'day': 20},
 {'year': 1996, 'month': 6, 'day': 14},
 {'year': 1998, 'month': 11, 'day': 15},
 {'year': 1997, 'month': 12, 'day': 31},
 {'year': 1997, 'month': 2, 'day': 22},
 {'year': 1998, 'month': 6, 'day': 27},
 {'year': 1998, 'month': 11, 'day': 18}],
     'August 24, 1998\nApril 22, 1999\nMarch 2, 1996\nMay 19, 1995\nJune 14, 1998\nMay 20, 1999\nJune 14, 1996\nNovember 15, 1998\nDecember 31, 1997\nFebruary 22, 1997\nJune 27, 1998\nNovember 18, 1998', True),

    ([{'year': 1994, 'month': 8, 'day': 29},
 {'year': 1997, 'month': 7, 'day': 31},
 {'year': 1994, 'month': 10, 'day': 18},
 {'year': 1998, 'month': 8, 'day': 31}],
     'August 29, 1994\nJuly 31, 1997\nOctober 18, 1994\nAugust 31, 1998', True),

    ([{'year': 1994, 'month': 8, 'day': 29},
 {'year': 1997, 'month': 7, 'day': 31},
 {'year': 1994, 'month': 10, 'day': 18},
 {'year': 1998, 'month': 4, 'day': 31}],
     'August 29, 1994\nJuly 31, 1997\nOctober 18, 1994\nApril 31, 1998', True),

    ([{'year': 1996, 'month': 3, 'day': 5},
 {'year': 1999, 'month': 5, 'day': 3},
 {'year': 1998, 'month': 5, 'day': 13},
 {'year': 1995, 'month': 6, 'day': 1},
 {'year': 1997, 'month': 12, 'day': 4},
 {'year': 1997, 'month': 8, 'day': 5},
 {'year': 1997, 'month': 11, 'day': 12},
 {'year': 1999, 'month': 10, 'day': 4}],
     'March 5, 1996\nMay 3, 1999\nMay 13, 1998\nJune 1, 1995\nDecember 4, 1997\nAugust 5, 1997\nNovember 12, 1997\nOctober 4, 1999', True),

    ([{'year': 1994, 'month': 11, 'day': 30}],
     'November 30, 1994', True),

    ([{'day': 1, 'month': 1, 'year': 2026}],
     'a810e9532fd3d5d73fbb1172e16b8559040799f9b553d0f13d9d72871e8f726f', False),

    ([{'year': 2024, 'day': 29, 'month': 2}],
     '31b7a50e23ba1d968e4edc68a15cfb3cceac9c93e6516394940faf61efcc8374', False),

    ([{'day': 1, 'month': 1, 'year': 2025},
 {'day': 2, 'month': 2, 'year': 2025},
 {'day': 3, 'month': 3, 'year': 2025},
 {'day': 4, 'month': 4, 'year': 2025},
 {'day': 5, 'month': 5, 'year': 2025},
 {'day': 6, 'month': 6, 'year': 2025},
 {'day': 7, 'month': 7, 'year': 2025},
 {'day': 8, 'month': 8, 'year': 2025},
 {'day': 9, 'month': 9, 'year': 2025},
 {'day': 10, 'month': 10, 'year': 2025},
 {'day': 11, 'month': 11, 'year': 2025},
 {'day': 12, 'month': 12, 'year': 2025}],
     'f317ae99bdadc8dddfa095001d553979208dfa9046f5a8e7995d0ab0847c9edf', False),

    ([{'month': 6, 'year': 2020, 'day': 9},
 {'year': 2019, 'month': 5, 'day': 10},
 {'day': 9, 'month': 6, 'year': 2020}],
     '9070d767ee036fc8c9ebabddcb818792faa531b31ebdab7d5184e81dd9d5a2e4', False),

    ([{'day': 31, 'month': 4, 'year': 1998}, {'day': 30, 'month': 2, 'year': 2001}],
     '9c6a9da5b612cc774ea6f1bb19cc11a01e6196ea312dca7d7fa7e0afa6ee149b', False),

    ([{'day': 7, 'month': 10, 'year': 2001},
 {'day': 7, 'month': 9, 'year': 2001},
 {'day': 7, 'month': 10, 'year': 2000}],
     '2121a4dbcd1348fc8c4e29b031c2dcdff38177950a1102b2adc87738da801181', False),

]

@pytest.mark.parametrize("date_records, expected_output, visible", q1_testcases)
def test_q1(capsys, date_records, expected_output, visible):
    print_dates_in_long_form(date_records)
    printed_output = capsys.readouterr().out.rstrip('\n')

    if visible:
        assert printed_output == expected_output
    else:
        assert hashcode(printed_output) == expected_output
