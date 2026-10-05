import pytest
import hashlib
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from q7 import replace_not_bad

def hashcode(value):
    return hashlib.sha256(str(value).encode("utf-8")).hexdigest()

q7_testcases = [
    # Visible Testcases
    ('This dinner is not that bad!', 'This dinner is good!', True),
    ('not not abada', '041a75d5d2b7def4c031ba532b8430955aab46f7417db204425bee4b8f9efe0e', False),
    ('Not bad, for a first directorial effort.', 'cf74563c1bf2133bb51171fce836cc5c1c995b1d364331d9daff09ba833428c9', False),
    ('"Do not call him bad!" said Natasha.', '1b9346b1b74ccf84fedea2ce301ab453c807b5b019c6e680919dc9efa4b2f3a0', False),
    ('Maula Jatt is awesome.', 'Maula Jatt is awesome.', True),
    ('Cheating is not my cup of tea.', 'Cheating is not my cup of tea.', True),
    ('Babar was not a badminton player growing up in Islamabad.', 'Babar was goodminton player growing up in Islamabad.', True),
    ('abadi in nothing', '6e5a3dd10d71fe81f1cd95a26114a0cdb7034b994702e469df2bcd891521823c', False),
    ('There is nothing to do in Islamabad.', '8ea638864a420c5f61242c8d4cbb3aefdf7a8dffa164265fac94836a801f851d', False),
    ('Badminton is not a bad sport.', '959bdeba1d89c4f0b66228f53280c7eb2df80da0315f9e136a1d78dfef253e9e', False),
    ('Not every Badshah is a Maharaja.', 'Goodshah is a Maharaja.', True),

    # Hidden Testcases
    ('This is not really bad at all.', '21f2907105b7a76767d493d417be956b2693826a823f3ed1677496c7cb3e72a1', False),
    ('The result is not completely bad.', '6cd895e3f12c094c9eef8e0354685616fa06b5947962caf33ba851c9bf71077f', False),
    ('NOT so BAD after all.', '1aa162af557c1c0e2ffab5b923d7bea3441516f6c70d3b48b6988b18188e8d5a', False),
    ('The weather is not bad today.', '69029e074ee0655bdc8427a770e26cf3052d903a5ba1d5d100463cf2aa930f02', False),
    ('This is not good and never bad.', 'bc5bff84ea1a5c84a310811baabf710bed4af57251e71b12872b6bc74a4404e7', False),
    ('Nothing bad happened.', 'a1333c62f2a1b7c602a388aa63d12817d37b031964329a6b470d7c3f16100fd5', False),
    ('not123bad', '770e607624d689265ca6c44884d0807d9b054d23c473c106c72be9de08b7376c', False),
    ('I said Not VERY bad indeed.', '1430e44457e782a5c01050c6b12e6537f0525d3a441ddce1ff328180ffd4f521', False),
    ('notable work is bad.', 'f5ff9b4a9f4940ea3a678684168012fb1980c3808692ad26cf5d7e9a70f5ab51', False)
]

@pytest.mark.parametrize("text, expected, visible", q7_testcases)
def test_q7(text, expected, visible):
    if visible:
        assert replace_not_bad(text) == expected
    else:
        assert hashcode(replace_not_bad(text)) == expected