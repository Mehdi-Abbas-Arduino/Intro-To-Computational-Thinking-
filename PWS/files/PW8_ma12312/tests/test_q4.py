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
    ('prime', 6552, [2, 2, 2, 3, 3, 7, 13], True),
    ('prime', 1567, [1567], True),
    ('prime', 1, [], True),
    ('special', 25, [2, 3, 4, 5, 7, 11, 13, 17, 19, 23], True),
    ('prime', 36, [2, 2, 3, 3], True),

    # Hidden Testcases
    ('prime', 256, '637a64721006c1ea156279f8e7dd3d81200f5af1e8ab51fc6145f84354a45949', False),
    ('prime', 97, '05080dc082c6df88129efbbe3f2c5a354e5348c963564f889914d0252f48b17d', False),
    ('special', 1, '4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945', False),
    ('special', 4, 'd3404059a01f4426ac8962d8a2d07f4b82824293477b5c929e4303678cbf0359', False),
    ('special', 50, '794cb21c0fc2c6bfd88446c4ee5558e01812341671a24907181b2600cf31f31d', False),
    ('special', 150, '9b4abf26782b6a457796dec0ce5643aeb23b8ef7bd7fe5f36fb21004ae1af95d', False),
    ('prime', 2, '038966de9f6b9a901b20b4c6ca8b2a46009feebe031babc842d43690c0bc222b', False),
    ('prime', 100, '166bd3f7af9235cf0f76af18be4745995cc70acc8b7bdddf93b21259905f7a97', False),
    ('prime', 999, 'd17ea7a2bfaa7171249c23302765d499d6f8e4d0637a31b3c11843b5e329b4a0', False),
    ('special', 100, '64f18c47cec853cb2847580071fe655460ca73795fab611169d278a4bb39b560', False),
]

@pytest.mark.parametrize("kind, num, expected, visible", q4_testcases)
def test_q4(kind, num, expected, visible):
    result = prime_factors(num) if kind == "prime" else special_numbers(num)
    assert isinstance(result, list)
    assert all(isinstance(value, int) for value in result)
    if visible:
        assert result == expected
    else:
        assert hashcode(result) == expected
