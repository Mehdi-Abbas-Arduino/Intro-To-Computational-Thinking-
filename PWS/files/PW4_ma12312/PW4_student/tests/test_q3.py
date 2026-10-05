import pytest
import hashlib
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from q3 import *

q3_testcases = [
    # Visible Testcases
    (1, "1", True),
    (4, "1, 3, 6, 10", True),
    (3, "1, 3, 6", True),
    (
        20,
        "1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210",
        True
    ),

    # Hidden Testcases
    (2, "b4dedd704580c9257d4ed374957ce244a02e5316f79bafc8c0ea470d7efe6826", False),
    (5, "81ddf839c9b37c55349ae870bf9540a57437d03753c82aa7180cccc1bf92dd49", False),
    (6, "aaa669da3cc87d249ea394d379c671bda54a5dcfe05d6def6109d5c498f1ed2c", False),
    (7, "77f39390d1290c7386f7992184ebe3d2aad9f446829000b9f3aed4a78d9a6d3d", False),
    (8, "f4d37c503bdfd7a20f298315c2553fa32a15b20773991cf24094446546ea2452", False),
    (9, "4df67d77a0daeffac8f8176ba335748141928ab2754bcfa5d0830f6df41429a6", False),
    (10, "5413f39f8b1a850e0d42a1fe45e9fec4453c89048e044af147de0eb0f0b1b994", False),
    (11, "ffa0f5769d31ead49ab3efd8a2b12255040fdbceef0534d89473d43ea1f4b94a", False),
    (12, "269c985cb4e5fa71136706364c58ad5fa8e7f9e066b152367c56d5b9b9f114c1", False),
    (15, "1da01afddf7e75df60ea85adbe7d49d00bd6c3fe5bfefec1d455ecd2b4971950", False),
    (19, "1ed78683637784b742d95802c072a207bad5999cd5b9283195d18f2aff648e06", False)
]

def hashcode(n) -> str:
    return hashlib.sha256(str(n).encode("utf-8")).hexdigest()

@pytest.mark.parametrize("term_count, result, testcase", q3_testcases)
def test_q3(capsys, term_count, result, testcase):
    triangle_number_sequence(term_count)

    captured, err = capsys.readouterr()
    captured = captured.strip()

    if testcase:
        assert captured == result
    else:
        assert hashcode(captured) == result