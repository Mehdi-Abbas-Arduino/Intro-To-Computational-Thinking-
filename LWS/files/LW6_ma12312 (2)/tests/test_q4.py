import pytest
import hashlib
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from q4 import *

def hashcode(value):
    return hashlib.sha256(str(value).encode("utf-8")).hexdigest()

q4_testcases = [
    # Visible Testcases
    ('LVLEL', 'LVEEL', True),
    ('VLLVE', 'VEEVE', True),
    ('LLLLL', 'LLLLL', True),
    ('VVVV', 'VVVV', True),
    ('LVLVLV', 'LVEVEV', True),
    ('LLLV', 'LLEV', True),
    ('VLLL', 'VELL', True),
    ('LVLELVLEVL', 'LVEELVEEVE', True),
    ('LLLLLVVVVV', 'LLLLEVVVVV', True),
    ('EVVEVLELV', 'EVVEVEEEV', True),

    # Hidden Testcases
    ('L', '72dfcfb0c470ac255cde83fb8fe38de8a128188e03ea5ba5b2a93adbea1062fa', False),
    ('V', 'de5a6f78116eca62d7fc5ce159d23ae6b889b365a1739ad2cf36f925a140d0cc', False),
    ('E', 'a9f51566bd6705f7ea6ad54bb9deb449f795582d6529a0e22207b8981233ec58', False),
    ('VL', '2c99d952bd19b482918811dabcac61711f57ee68f2f15c5b297b70be3e416b00', False),
    ('LV', '20e95ada67c778758b26bd6425863f9a53bb666a98e3fe060eec15866e87cc12', False),
    ('LVL', '64b509dbc852d68c0aa4bce69ea3d21ac487550f724f089ea597281aadc1fd30', False),
    ('LLVLL', 'e4b974fdc93686a23cfc3e7681134fca7500c0621915671cd0647b5aace8bc4a', False),
    ('VLVLV', '15b0db64ad5ddd8d5a493704ddbf313cf0a053863d9870a7a57c28639c50e8c1', False),
    ('ELVLE', '0e0b0435cb02e5210c7e1b08b3685273bd4b87324e39c1a296632a043f259f87', False),
    ('LLVVLLV', '0dd6abd7c47c1fd1a9282315442ac3baa5ac1004ad3e1a0200ba980d87ec39c3', False),
]


@pytest.mark.parametrize("walkway, expected, visible", q4_testcases)
def test_q4(walkway, expected, visible):
    if visible:
        assert clean_walkway(walkway) == expected
    else:
        assert hashcode(clean_walkway(walkway)) == expected