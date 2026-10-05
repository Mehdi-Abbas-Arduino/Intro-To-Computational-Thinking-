import pytest
import hashlib
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from q4 import *

q4_testcases = [
    # Visible Testcases
    (4, 2, 50, "1011", 0, True),
    (3, 2, 66, "110", 66, True),
    (4, 2, 50, "1111", 100, True),
    (5, 3, 30, "11011", 0, True),
    (10, 7, 60, "1111101111", 0, True),

    # Hidden Testcases
    (2, 1, 25, "11", "ad57366865126e55649ecb23ae1d48887544976efea46a48eb5d85a6eeb4d306", False),
    (2, 1, 25, "10", "b7a56873cd771f2c446d369b649430b65a756ba278ff97ec81bb6f55b2e73569", False),
    (2, 1, 25, "01", "5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9", False),
    (6, 3, 40, "111001", "d59eced1ded07f84c145592f65bdf854358e009c5cd705f5215bf18697fed103", False),
    (6, 3, 40, "110111", "5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9", False),
    (10, 9, 99, "1111111110", "8c1f1046219ddd216a023f792356ddf127fce372a72ec9b4cdac989ee5b0b455", False),
    (10, 9, 99, "1111111111", "ad57366865126e55649ecb23ae1d48887544976efea46a48eb5d85a6eeb4d306", False),
    (7, 4, 70, "1111010", "ff5a1ae012afa5d4c889c50ad427aaf545d31a4fac04ffc1c4d03d403ba4250a", False),
    (7, 4, 70, "1110111", "5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9", False),
    (5, 1, 10, "10000", "4a44dc15364204a80fe80e9039455cc1608281820fe2b24f1e5233ade6af1dd5", False),
]

def hashcode(n) -> str:
    return hashlib.sha256(str(n).encode("utf-8")).hexdigest()

@pytest.mark.parametrize("total_tests, required_tests, partial_score, test_results, result, testcase", q4_testcases)
def test_q4(total_tests, required_tests, partial_score, test_results, result, testcase):
    if testcase:
        assert submission_score(total_tests, required_tests, partial_score, test_results) == result
    else:
        assert hashcode(submission_score(total_tests, required_tests, partial_score, test_results)) == result