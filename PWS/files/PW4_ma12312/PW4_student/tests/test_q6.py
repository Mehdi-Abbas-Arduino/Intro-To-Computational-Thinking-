import pytest
import hashlib
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from q6 import *

q6_testcases = [
    # Visible Testcases
    (5, 0, 4, 2, True),
    (3, 6, 7, 0, True),
    (5, 5, 0, 4, True),
    (5, 0, 5, 4, True),
    (11, 2, 10, 4, True),

    # Hidden Testcases
    (1, 0, 0, "5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9", False),
    (6, 2, 9, "4e07408562bedb8b60ce05c1decfe3ad16b72230967de01f640b7e4729b49fce", False),
    (6, 9, 2, "4e07408562bedb8b60ce05c1decfe3ad16b72230967de01f640b7e4729b49fce", False),
    (8, 3, 6, "4e07408562bedb8b60ce05c1decfe3ad16b72230967de01f640b7e4729b49fce", False),
    (10, 4, 4, "ef2d127de37b942baad06145e54b0c619a1f22327b2ebbcfbec78f5564afe39d", False),
    (10, 10, 10, "5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9", False),
    (7, 7, 3, "4e07408562bedb8b60ce05c1decfe3ad16b72230967de01f640b7e4729b49fce", False),
    (7, 3, 7, "4e07408562bedb8b60ce05c1decfe3ad16b72230967de01f640b7e4729b49fce", False),
    (100, 0, 99, "0e17daca5f3e175f448bacace3bc0da47d0655a74c8dd0dc497a3afbdad95f1f", False),
    (100, 50, 100, "1a6562590ef19d1045d06c4055742d38288e9e6dcd71ccde5cee80f1d5a774eb", False),
]

def hashcode(n) -> str:
    return hashlib.sha256(str(n).encode("utf-8")).hexdigest()

@pytest.mark.parametrize("planet_count, power_source_1, power_source_2, result, testcase", q6_testcases)
def test_q6(planet_count, power_source_1, power_source_2, result, testcase):
    if testcase:
        assert max_power_distance(planet_count, power_source_1, power_source_2) == result
    else:
        assert hashcode(max_power_distance(planet_count, power_source_1, power_source_2)) == result