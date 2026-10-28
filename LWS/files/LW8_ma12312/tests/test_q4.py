import pytest
import hashlib
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from q4 import *


def hashcode(value):
    return hashlib.sha256(str(value).encode("utf-8")).hexdigest()


q4_testcases = [
    (['quddusi', 'MNT', 'swifthyderabad', 'CEmajorAT', 'skibidiali', 'valverde', 'baqir', 'ronaldo', 'hassan', 'alonso', 'etoo', 'mrgreedy', 'mbappe', 'messi', 'evra', 'mraura', 'amir', 'mufaddal', 'isco', 'saifibhai', 'iniesta', 'abdullah', 'babarazam', 'hussainshah', 'sr4', 'kdb', 'askarizz', 'basim', 'raphina', 'usman', 'coldp@lm4r', ''], ['quddusi', 'swifthyderabad', 'CEmajorAT', 'skibidiali', 'valverde', 'baqir', 'ronaldo', 'hassan', 'alonso', 'etoo', 'mrgreedy', 'mbappe', 'messi', 'evra', 'mraura', 'amir', 'mufaddal', 'isco', 'saifibhai', 'iniesta', 'abdullah', 'hussainshah', 'askarizz', 'basim', 'raphina', 'usman', 'coldp@lm4r'], True),
    (['amir', 'MNT', 'xyz', 'babarazam', 'otto', 'ali', 'saifibhai', 'hassan', 'evra', 'mrgreedy', 'mraura', 'etoo', 'alonso', 'messi', 'ronaldo', 'usman', 'abdullah', 'kdb', 'mbappe', 'quddusi', 'skibidiali', 'valverde', 'coldp@lm4r', '', 'askari', 'babarazam', 'faheem', 'leo', 'nash', 'tito', 'zio', 'O_o', 'u2u', 'EVE', 'ae', 'Ai'], ['amir', 'otto', 'ali', 'saifibhai', 'hassan', 'evra', 'mrgreedy', 'mraura', 'etoo', 'alonso', 'messi', 'ronaldo', 'usman', 'abdullah', 'mbappe', 'quddusi', 'skibidiali', 'valverde', 'coldp@lm4r', 'askari', 'faheem', 'leo', 'nash', 'tito', 'zio', 'O_o', 'u2u', 'EVE', 'ae', 'Ai'], True),
    (['ae', 'Ai', 'aoa', 'u2u', 'bcd', 'MNT', 'sr4', 'Xyz', 'EVE', 'eve', 'EVA', 'iZZi', 'usman', 'mufaddal', 'faheem', 'coldp@lm4r', 'mrgreedy', 'mraura', 'Amira', 'apollo', 'babarazam', 'AAA', 'bbb', 'zzz', 'zzzZ', 'Ali', 'otto', 'iso', 'eko', 'e3e', 'O_o', 'babarazam', 'aeIOU', 'ae', 'ooo', 'uu', 'ii'], ['ae', 'Ai', 'aoa', 'u2u', 'EVE', 'eve', 'EVA', 'iZZi', 'usman', 'mufaddal', 'faheem', 'coldp@lm4r', 'mrgreedy', 'mraura', 'Amira', 'apollo', 'AAA', 'Ali', 'otto', 'iso', 'eko', 'e3e', 'O_o', 'aeIOU', 'ae', 'ooo', 'uu', 'ii'], True),
    (['ronaldo', 'Messi', 'Mbappe', 'Neymar', 'Xavi', 'Iniesta', 'Lewandowski', 'benzema', 'messi', 'Haaland', 'KDB', 'babarazam', 'MNT', 'sr4', 'xyz', 'abc', 'amir', 'otto', 'ali', 'EVE', 'saif', 'usman', 'evra', 'hassan', 'mehmood', 'ramos', 'gavi', 'pedri', 'isco', 'rafa', 'mrgreedy', 'leo', 'tito', 'O_o', 'u2u', 'Ae', 'AAA', 'AE', 'EVE'], ['ronaldo', 'Messi', 'Mbappe', 'Neymar', 'Xavi', 'Iniesta', 'Lewandowski', 'benzema', 'messi', 'Haaland', 'abc', 'amir', 'otto', 'ali', 'EVE', 'saif', 'usman', 'evra', 'hassan', 'mehmood', 'ramos', 'gavi', 'pedri', 'isco', 'rafa', 'mrgreedy', 'leo', 'tito', 'O_o', 'u2u', 'Ae', 'AAA', 'AE', 'EVE'], True),
    (['AE', 'aeiou', 'eve', 'apollo', 'skibidiali', 'sky', 'hEllo', 'usman', 'faheem', 'meow', 'baqir', 'mraura', 'saifibhai', 'coldp@lm4r', 'iniesta', 'abdullah', 'ronaldo', 'alonso', 'etoo', 'valverde', 'messi', 'babarazam', 'kdb', 'MNT', 'xyz', 'zzz', 'zzzZ', 'A2A', 'EVE', 'otto', 'ae', 'uSU', 'O_o', 'Ai', 'Ali'], ['AE', 'aeiou', 'eve', 'apollo', 'skibidiali', 'hEllo', 'usman', 'faheem', 'meow', 'baqir', 'mraura', 'saifibhai', 'coldp@lm4r', 'iniesta', 'abdullah', 'ronaldo', 'alonso', 'etoo', 'valverde', 'messi', 'A2A', 'EVE', 'otto', 'ae', 'uSU', 'O_o', 'Ai', 'Ali'], True),
    (['adam', 'eve', 'isa', 'ozu', 'uma', 'zuzu', 'bcd', 'fgh', 'mNt', 'xyz', 'otto', 'ali', 'Oscar', 'erik', 'ian', 'aaron', 'ellen', 'bob', 'babarazam', 'ae', 'aeiou', 'mufaddal', 'skibidiali', 'saifibhai', 'quddusi', 'ronaldo', 'kdb', 'abdullah', 'coldp@lm4r', 'zzzZ', 'evee', 'leo', 'O_o', 'uuu'], 'd219281c4b247ef1cc0a708e23ea4d62da26f69ac04e0b8577d01b8d6f304501', False),
    (['amir', 'Ali', 'bob', 'mNt', 'babarazam', 'Oreo', 'oreo', 'EVA', 'eve', 'ae', 'uzi', 'bbb', 'xyz', 'apollo', 'usa', 'faheem', 'otto', 'EEE', 'skibidiali', 'MUFADDAL', 'coldp@lm4r', 'sr4', 'bcd', 'AE', 'AAA', 'aeiou', 'EVE', 'ISA', 'OBE', 'ABE', 'zohaib', 'irfan', 'usman', 'leona', 'neymar', 'messi', 'iniesta', 'valverde', 'ronaldo', 'mbappe', 'abdullah'], '8933773dae0b5d4e2e56eeb946d3a368dd2f0a42ab45bc86ad5168967878189f', False),
    (['AE', 'O_o', 'e3e', '123', '', 'coldp@lm4r', '@@@', '####', 'aeIOU', 'bcd!', 'xyz', 'ae', 'Ai', 'otto', 'EVE', 'eee', 'uSU', 'babarazam', 'MNT', 'sr4', 'BOB', 'Ali@', 'mrgreedy', 'skibidiali', 'zzz', 'uuu', 'pqr', 'leo', 'tito', 'Ae', 'iii', 'ooO', 'uuU', 'babarazam'], 'ed788f9f1fc4f1fded32ed0e99aec91d969f33aed562013b4f33166d14ec9307', False),
    (['ronaldo', 'Messi', 'mbappe', 'neymar', 'hassan', 'amir', 'hussainshah', 'alonso', 'etoo', 'valverde', 'kaka', 'isco', 'rafa', 'evra', 'abdullah', 'usman', 'faheem', 'iniesta', 'babarazam', 'MNT', 'sr4', 'kdb', 'mrgreedy', 'mraura', 'zizo', 'EVE', 'otto', 'ae', 'Ali', 'Oscar', 'baqir', 'coldp@lm4r', 'zzz', 'leo', 'O_o', 'u2u'], '12e67291d41cfc6feaf564bdce82d83272faf4e43b24b00cba3cb35168dcbf30', False),
    (['ae', 'Ai', 'aoa', 'u2u', 'bcd', 'MNT', 'sr4', 'Xyz', 'EVE', 'eve', 'EVA', 'iZZi', 'usman', 'mufaddal', 'faheem', 'coldp@lm4r', 'mrgreedy', 'mraura', 'Amira', 'apollo', 'babarazam', 'AAA', 'bbb', 'zzz', 'zzzZ', 'Ali', 'otto', 'iso', 'eko', 'e3e', 'O_o', 'babarazam', 'aeIOU', 'ae', 'ooo', 'uu', 'ii', 'leo', 'tito', 'skibidiali', 'messi', 'ronaldo'], '61bebcca957f265363b0c31ea6b849347cc18503692a5794459283c10a6a7c85', False),
    ([], '4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945', False),
    (['MNT', 'kdb', 'sr4', '', 'babarazam', 'BABARAZAM'], '4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945', False),
    (['ali', 'EVE', 'otto', 'Usman', 'aeiou'], '08e8e7130ef6fd4a3ccb48e4e617ddb02836c47c16df134a333ca05da529b594', False),
    (['BabarAzam', 'babaraZAM', 'babarazam', 'amir', 'MNT', 'ronaldo'], '3622208ced0899dadc15a2b7f305c4bdb17fde9322a0956aedc72f8e848a045d', False),
    (['ae', 'ae', 'XYZ', 'u2u', 'O_o', 'coldp@lm4r', 'bbb', 'Ali'], 'd9081e3db7bd3e89aa68138b2b7c6c16c6790a6ac02ae4fa34ac1352ad6bc077', False),
]


@pytest.mark.parametrize("player_names, expected, visible", q4_testcases)
def test_q4(player_names, expected, visible):
    result = remove_excluded_players(player_names)

    assert result is None

    if visible:
        assert player_names == expected
    else:
        assert hashcode(player_names) == expected