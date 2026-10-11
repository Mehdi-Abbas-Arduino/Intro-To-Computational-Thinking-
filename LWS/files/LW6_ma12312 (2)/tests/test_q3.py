import pytest
import hashlib
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from q3 import *

def hashcode(value):
    return hashlib.sha256(str(value).encode("utf-8")).hexdigest()

q3_testcases = [
    # Visible Testcases
    ('sd2j42n 35', 'There must be at least one upper case character.', True),
    ('ASO3QSA', 'Length must be between 8 and 30 characters (exclusive).', True),
    ('StrongPass9', 'Strong Password!', True),
    ('ABCDEFGHIJ', 'There must be at least one lower case character.', True),
    ('A1b2C3d45FS', 'Strong Password!', True),
    ('Abc123 45', 'There must be no spaces in the password.', True),

    # Hidden Testcases
    ('Abcdef12', '8ca078c3fca3033aeafdc9880b19016838fb48864b7721e58ac7d88009f5786e', False),
    ('Abcdefghijklmnopqrstuvwxyz1234', '8ca078c3fca3033aeafdc9880b19016838fb48864b7721e58ac7d88009f5786e', False),
    ('Abcdefg1X', '89f2b51a850486227687417a9237b51b4d00987dacfec0d79febe3b46136323c', False),
    ('Abcdefghijklmnopqrstuvwxyz123', '89f2b51a850486227687417a9237b51b4d00987dacfec0d79febe3b46136323c', False),
    ('lowercase9', 'f5c1328093bd6986134443d3b2feddbe1399116cb413d72823c9614a8c63eadd', False),
    ('UPPERCASE9', 'a5bac5eea0d4162113bb21dcde16f314ec5d3497acb5f4c1eed760da2cb1d6c1', False),
    ('NoDigitsHere', '70f5815ebeb045486920329ba448bac8da93417cb49a60c02195cb8f567f6719', False),
    ('Valid Pass9', '34c8d44ba3d4c913d8894e2deb1e92e58fd9960e0f038b8787343af055ea5eb3', False),
    ('abc', '8ca078c3fca3033aeafdc9880b19016838fb48864b7721e58ac7d88009f5786e', False),
    ('abcdefgh9', 'f5c1328093bd6986134443d3b2feddbe1399116cb413d72823c9614a8c63eadd', False),
    ('ABCDEFGH9', 'a5bac5eea0d4162113bb21dcde16f314ec5d3497acb5f4c1eed760da2cb1d6c1', False),
    ('Abcdefghi', '70f5815ebeb045486920329ba448bac8da93417cb49a60c02195cb8f567f6719', False),
    ('Abcdefg 1', '34c8d44ba3d4c913d8894e2deb1e92e58fd9960e0f038b8787343af055ea5eb3', False),
    ('A-b_c+d=1', '89f2b51a850486227687417a9237b51b4d00987dacfec0d79febe3b46136323c', False),
]

@pytest.mark.parametrize("password, expected, visible", q3_testcases)
def test_q3(capsys, password, expected, visible):
    check_password_strength(password)
    actual = capsys.readouterr().out.strip()

    if visible:
        assert actual == expected
    else:
        assert hashcode(actual) == expected