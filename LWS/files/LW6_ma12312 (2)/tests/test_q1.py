import pytest
import hashlib
import inspect
import ast
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from q1 import *


def hashcode(value):
    return hashlib.sha256(str(value).encode("utf-8")).hexdigest()


q1_testcases = [
    # Visible Testcases
    ('123456789012345678901234567890', '35690258014570', True),
    ('pomegranate', 'mgrat', True),
    ('Burqa Avenger', 'ra ene', True),
    ('racecar', 'cca', True),

    # Hidden Testcases
    ('', 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855', False),
    ('ab', 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855', False),
    ('abc', '2e7d2c03a9507ae265ecf5b5356885a53393a2029d241394997265a1a25aefc6', False),
    ('abcde', 'e64c826b6b33f307cecf54ff843c5f9797c1056eb33f9dd60bc632f519712cb9', False),
    ('abcdef', '7708169e4fc7c45b16dc161fc7ff561b67f45f3671fa83053adfb11976711e07', False),
    ('abcdefghij', 'ac714ea2b5da820f540c4d339560f4faa76a703dbe30023545d87d79516ec883', False),
    ('HELLO WORLD', 'bc0a61563154c97d4d0f5ed521082e958bc87cf4d9583450d59be76b30c5f0f9', False),
    ('12345', '9f14025af0065b30e47e23ebb3b491d39ae8ed17d33739e5ff3827ffb3634953', False),
    ('!@#$%^&*()', 'c7d670a040211c409a56ae4d6d55db546d2ec17ee2d15232a994ed698ca9eb6c', False),
    ('Habib University', '34161f1f4ec9787e1ead6528ff312eeeb65ccdceeb940ebee7529b11433ef906', False),
    ('CS101 Strings Lab', '49b849b2078029e7540d55a5d507b195a89c4e02c490aa366b7788126b3631c6', False),
    ('aaaaabbbbbccccc', 'a53f82437d8243f4524ac4073a38969fa4d5f6521c86d178ab3dd145f7633d5f', False),
    ('with spaces inside', '67c170ea74e3f724c6eb2e0cda196fd0404d3bdd4feef91fc4ae8e8a2eaad1e0', False),
    ('A-B_C+D=E', 'c60814c2fca4ad90bf7523c5e89da2d10aeec1f72e890eb02abfad67d3ac091c', False),
    ('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz', 'd57e27e5c090207a6ea1a87baf95585f2daacd217aa74035e7fd83ccf42113aa', False),
]

@pytest.mark.parametrize("event_message, expected, visible", q1_testcases)
def test_q1(event_message, expected, visible):
    if visible:
        assert event_code(event_message) == expected
    else:
        assert hashcode(event_code(event_message)) == expected

def test_q1_uses_iteration():
    tree = ast.parse(inspect.getsource(event_code))
    assert any(isinstance(node, (ast.For, ast.While)) for node in ast.walk(tree))