import pytest
import hashlib
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from q1 import *

def hashcode(value):
    return hashlib.sha256(str(value).encode("utf-8")).hexdigest()

q1_testcases = [
    # Visible Testcases
    ([2, 3, 2, 4, 1], 'cacta', True, True),
    ([5], 'z', True, True),
    ([7, 9], 'ab', True, True),
    ([1, 2, 2, 1], 'xqqr', False, True),
    ([1, 2, 3, 2, 1], 'wwwww', True, True),

    # Hidden Testcases
    ([1, 2, 3, 4, 1, 1, 2], 'abababb', '60a33e6cf5151f2d52eddae9685cfa270426aa89d8dbc7dfb854606f1d1a40fe', False),
    ([1, 4, 2, 9, 3, 8], 'azzfdb', '3cbc87c7681f34db4617feaa2c8801931bc5e42d8d0f560e756dd4cd92885f18', False),
    ([9, 7, 7, 9, 8, 3, 7, 2, 9, 7, 9, 2, 7, 9, 9, 3, 0, 9, 9, 8, 8, 6, 9, 8, 4, 8, 8, 0, 7, 8, 4, 6, 0, 2, 2, 7, 6, 6, 7, 2], 'bohiegnqkrqiupnxkkcspvxggrbrzrlcxgtxiuar', '60a33e6cf5151f2d52eddae9685cfa270426aa89d8dbc7dfb854606f1d1a40fe', False),
    ([4, 3, 0, 2, 4, 1, 8, 3, 6, 8, 0, 7, 7, 7, 2, 7, 0, 6, 5, 7, 4, 0, 6, 1, 9, 8, 9, 8, 7, 8, 1, 3, 5, 4, 1, 7, 4, 1, 1, 5, 9, 4, 5, 2, 1, 3, 2, 1, 7, 8, 3, 8, 2, 5, 8, 4, 7, 7, 7, 1, 5, 9, 1, 6, 5, 2, 3, 7, 9, 2, 4, 8, 8, 8, 0, 0, 3, 5, 5, 0, 7, 8, 2, 4, 6, 2, 1, 0, 3, 5, 6, 6, 8, 8, 2, 2, 1, 9, 2, 5], 'nblmqtsjzsyxaohogxfmufellztyfbcxhoyqkudlsfvbnzqbsipjrzwbqecaimwcnkpmqfyoshyxgzmfocyqoslraurcviputrnl', '60a33e6cf5151f2d52eddae9685cfa270426aa89d8dbc7dfb854606f1d1a40fe', False),
    ([3, 9, 2, 2, 4, 7, 5, 3, 4, 4, 9, 7, 0, 7, 7, 5, 4, 5, 2, 6, 3, 1, 0, 0, 4, 8, 8, 0, 7, 0, 7, 9, 8, 5, 4, 0, 6, 7, 6, 0, 2, 6, 7, 3, 7, 8, 5, 9, 9, 7, 1, 8, 4, 1, 0, 5, 7, 1, 7, 0, 4, 1, 9, 6, 4, 5, 2, 3, 2, 9, 2, 2, 4, 8, 7, 0, 7, 2, 9, 8, 3, 0, 1, 8, 6, 2, 6, 7, 4, 9, 1, 7, 4, 0, 4, 0, 8, 2, 2, 2, 1, 5, 7, 7, 1, 5, 2, 2, 5, 9, 0, 1, 7, 7, 5, 8, 6, 7, 3, 8, 5, 1, 9, 0, 9, 0, 8, 1, 3, 7, 2, 9, 5, 6, 0, 1, 5, 9, 5, 3, 4, 2, 0, 9, 1, 6, 8, 4, 2, 9, 4, 6, 3, 9, 0, 7, 5, 4, 1, 8, 3, 6, 0, 8, 9, 3, 4, 1, 7, 3, 7, 4, 3, 5, 6, 5, 3, 0, 0, 7, 2, 9, 1, 7, 1, 5, 1, 3, 1, 6, 7, 7, 9, 2, 5, 6, 5, 6, 0, 4], 'djccehfdeejhahhfefcgdbaaeiiahahjifeaghgacghdhifjjhbiebafhbhaebjgefcdcjcceihahcjidabigcghejbheaeaicccbfhhbfccfjabhhfighdifbjajaibdhcjfgabfjfdecajbgiecjegdjahfebidgaijdebhdhedfgfdaahcjbhbfbdbghhjcfgfgae', '3cbc87c7681f34db4617feaa2c8801931bc5e42d8d0f560e756dd4cd92885f18', False),
    ([7, 5, 7, 2, 2, 6, 3, 8, 8, 4, 2, 1, 1, 5, 4, 8, 2, 5, 1, 5, 4, 6, 6, 7, 0, 2, 3, 2, 7, 2, 9, 4, 0, 8, 2, 1, 9, 8, 8, 6, 9, 3, 8, 8, 8, 8, 5, 6, 3, 8, 1, 3, 8, 7, 4, 9, 2, 1, 0, 1, 3, 7, 0, 5, 5, 9, 5, 1, 4, 7, 5, 2, 4, 5, 7, 3, 8, 6, 5, 7, 4, 6, 8, 5, 6, 6, 6, 8, 0, 8, 1, 4, 4, 4, 0, 7, 7, 3, 2, 4, 3, 1, 6, 8, 8, 9, 2, 3, 2, 3, 7, 3, 0, 1, 0, 6, 3, 8, 1, 3, 7, 6, 3, 9, 5, 8, 6, 5, 3, 2, 6, 0, 5, 7, 8, 2, 5, 6, 5, 6, 7, 8, 2, 6, 6, 1, 2, 7, 0, 7, 9, 4, 7, 5, 9, 6, 5, 0, 8, 7, 7, 0, 5, 0, 2, 6, 5, 6, 9, 5, 7, 4, 4, 6, 5, 3, 3, 8, 2, 3, 2, 3, 6, 8, 1, 6, 4, 5, 3, 3, 9, 4, 7, 3, 7, 4, 7, 4, 1, 9, 7, 7, 5, 6, 9, 9, 3, 3, 9, 8, 0, 2, 6, 3, 2, 4, 5, 6, 0, 7, 5, 7, 6, 3, 1, 0, 7, 1, 8, 3, 4, 0, 8, 7, 5, 6, 4, 6, 3, 1, 1, 6, 3, 0, 4, 9, 1, 0, 4, 7, 7, 3, 8, 9, 9, 9, 3, 6, 5, 4, 1, 8, 2, 9, 0, 1, 8, 4, 9, 1, 6, 6, 6, 8, 3, 2, 9, 0, 7, 6, 7, 3, 0, 4, 4, 6, 4, 5, 8, 3, 2, 5, 3, 4, 3, 2, 3, 1, 5, 9, 5, 6, 0, 6, 0, 4, 9, 7, 4, 4, 6, 9, 7, 7, 4, 2, 6, 9, 6, 6, 5, 8, 6, 1, 5, 6, 9, 8, 4, 3, 5, 2, 9, 6, 9, 7, 4, 2, 1, 5, 7, 8, 3, 6, 8, 1, 9, 0, 7, 0, 6, 7, 1, 5, 7, 0, 7, 9, 4, 9, 7, 7, 4, 6, 3, 4, 8, 3, 0, 2, 8, 9, 9, 8, 9, 8, 2, 4, 4, 4, 3, 3, 5, 7, 3, 0, 7, 3, 2, 4, 7, 3, 7, 4, 4, 1, 6, 2, 2, 8, 0, 3, 2, 0, 7, 7, 2, 0, 8, 4, 7, 9, 6, 9, 9, 9, 6, 6, 0, 9, 6, 6, 9, 6, 6, 3, 0, 4, 5, 9, 9, 3, 3, 7, 6, 0, 0, 5, 7, 3, 3, 9, 2, 6, 9, 7, 4, 4, 6, 7, 7, 5, 5, 5, 8, 5, 0, 0, 4, 5, 4, 6, 0, 1, 0, 2, 6, 8, 0, 2, 3, 1, 7, 6, 1, 6, 5, 2, 7, 7, 9, 4, 1, 6, 5, 5, 5, 9, 9, 7, 4, 8, 3, 6, 9, 1, 1, 6, 6, 7], 'hfhccgdiiecbbfeicfbfegghacdchcjeaicbjiigjdiiiifgdibdihejcbabdhaffjfbehfcefhdigfhegifgggiaibeeeahhdcedbgiijcdcdhdabagdibdhgdjfigfdcgafhicfgfghicggbchahjehfjgfaihhafacgfgjfheegfddicdcdgibgefddjehdhehebjhhfgjjddjiacgdcefgahfhgdbahbideaihfgegdbbgdaejbaehhdijjjdgfebicjabiejbgggidcjahghdaeegefidcfdedcdbfjfgagaejheegjhhecgjggfigbfgjiedfcjgjhecbfhidgibjahaghbfhahjejhhegdeidacijjijiceeeddfhdahdcehdheebgcciadcahhcaiehjgjjjggajggjggdaefjjddhgaafhddjcgjheeghhfffifaaefegabacgiacdbhgbgfchhjebgfffjjheidgjbbggh', '3cbc87c7681f34db4617feaa2c8801931bc5e42d8d0f560e756dd4cd92885f18', False),
    ([0, 0], 'aa', '3cbc87c7681f34db4617feaa2c8801931bc5e42d8d0f560e756dd4cd92885f18', False),
    ([0, 0], 'ab', '60a33e6cf5151f2d52eddae9685cfa270426aa89d8dbc7dfb854606f1d1a40fe', False),
    ([9, 9, 9, 9], 'zzzz', '3cbc87c7681f34db4617feaa2c8801931bc5e42d8d0f560e756dd4cd92885f18', False),
    ([9, 9, 9, 9], 'zzzy', '60a33e6cf5151f2d52eddae9685cfa270426aa89d8dbc7dfb854606f1d1a40fe', False),
]

@pytest.mark.parametrize("num, word, expected, visible", q1_testcases)
def test_q1(num, word, expected, visible):
    result = selek_sees(num, word)
    assert isinstance(result, bool)
    if visible:
        assert result == expected
    else:
        assert hashcode(result) == expected
