import hashlib
import os
import sys

import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import q9


CASES = [
    ('423692', '923857614', 8, True),
    ('5111', '752961348', 1, True),
    ('91566165', '639485712', 11, True),
    ('595275', '396748521', 7, True),
    ('444', '923857614', 0, True),
    ('4487', '428567391', '4e07408562bedb8b60ce05c1decfe3ad16b72230967de01f640b7e4729b49fce', False),
    ('86346387', '265349871', '2c624232cdd221771294dfbb310aca000a0df6ac8b66b696d90ef06fdefb64a3', False),
    ('65', '328749156', '6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b', False),
    ('42', '314962578', '6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b', False),
    ('9', '923857614', '5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9', False),
    ('99999999', '923857614', '5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9', False),
    ('94', '923857614', 'd4735e3a265e16eee03f59718b9b5d03019c07d8b6c51f90da3a666eec13ab35', False),
    ('21', '923857614', 'd4735e3a265e16eee03f59718b9b5d03019c07d8b6c51f90da3a666eec13ab35', False),
    ('35753', '923857614', '4b227777d4dd1fc61c6f884f48641d02b4d121d3fd328cb08b5531fcacdabf8a', False),
    ('123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789', '987654321', '4c8d5b6c695d265fb63dd73f275a21043a5887b37cb4fea0552ecc7b417c8f88', False),
]


@pytest.mark.parametrize(
    "digits_to_type, keypad, expected, visible",
    CASES,
    ids=[f"{'visible' if case[3] else 'hidden'}-{i:02d}" for i, case in enumerate(CASES, 1)],
)
def test_q9(digits_to_type, keypad, expected, visible):
    result = q9.entryTime(digits_to_type, keypad)
    assert type(result) is int, "entryTime() must return an integer number of seconds."
    if visible:
        assert result == expected, f"Expected {expected} seconds, got {result}."
    else:
        digest = hashlib.sha256(str(result).encode("utf-8")).hexdigest()
        assert digest == expected, "Incorrect typing time for this hidden test case."
