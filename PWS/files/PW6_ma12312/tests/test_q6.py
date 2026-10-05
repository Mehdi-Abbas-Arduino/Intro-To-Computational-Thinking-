import pytest
import hashlib
import ast
import inspect
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from q6 import potato_song

def hashcode(value):
    return hashlib.sha256(str(value).encode("utf-8")).hexdigest()

q6_testcases = [
    # Visible Testcases
    (1, '1 potato, 2 potato, 3 potato, 4!\n5 potato, 6 potato, 7 potato, MORE!', True),
    (2, '1bfc75865ab8a97e4749cd6c1c008395e8adc4dc3431378714ca79f4b95266eb', False),
    (3, '1 potato, 2 potato, 3 potato, 4!\n5 potato, 6 potato, 7 potato, MORE!\n8 potato, 9 potato, 10 potato, 11!\n12 potato, 13 potato, 14 potato, MORE!\n15 potato, 16 potato, 17 potato, 18!\n19 potato, 20 potato, 21 potato, MORE!', True),
    
    # Hidden Testcases
    (5, 'fccef6896c02edd58dbac28dedd6765e7b41e94bf74b25d4cea2883eb11e39ee', False), 
    (10, '1c5721f73d8dd61688cf98392dde9b4eeed63478dbe967b6cb89f65b87a66610', False), 
    (4, '87f4e23c462949105feeea8b82595a14d834608893639433521f9e83982af688', False), 
    (7, '48967e0c624f3dcc4ace7341a674ffe5198b6482b12719a717e1b64c42b9821f', False), 
    (17, '285abaff36ead23eae74c1a450659b89c39138f0de7a9d2a74bb41a76dfd82a8', False), 
    (20, '454ebf2db53bc124c702232ba107ef5197a4f91312ef53a82c66d3fab8e4c7ff', False), 
    (23, '83684dde7a49dcc75216cb0053ed9d0143bb6a27d525ae17dc0a34bd6abe06e5', False),
    (6, '7cad1744dc682affc83e2b973373da1a0ab3ce0480d4741b2ae4c36c85a2f0b1', False),
    (8, 'cfa5dde0ed69017c0c6e43344e6df0d3de3e28c68f9033dff873c75a43db23bf', False),
    (9, '76759d8ddf2d2204217a13e3f42a1cadb3bad6ac9f156670fb1a5b1b09a67ecb', False),
    (12, 'f55580c6c1198c7df72ce8bb402f1cfcd310a8bd5bcb2044a9a7481b58149d69', False),
    (15, '42f041bc3a5c61cad1cffa84a1426070b237a1315c828bebf7e6b830a5bab10b', False),
    (25, '7d900a9a881e8538d1cac224494532872e49687140b6966598eff0b4b47a1c0c', False),
    (30, 'bf787acd28953915a3fba16d11267a7e4b2ef77359e206219e67cc5c84bc7def', False),
    (50, '3350b53b31abd24bdc9c8b38232a27a1b5c459dfec75f0b5936ab0c470ef0f5c', False),
    (75, '0c4858c968b8740000d6f03b8e76bcf60105cd576b80c7401f544fbc3668dbe7', False),
    (100, 'd9d783a2f2d0182f393bc1348a08d587dd3a47981416430e4ea36d6ffaa7c2d6', False)
]

@pytest.mark.parametrize("verses, expected, visible", q6_testcases)
def test_q6(verses, expected, visible):
    if visible:
        assert potato_song(verses) == expected
    else:
        assert hashcode(potato_song(verses)) == expected