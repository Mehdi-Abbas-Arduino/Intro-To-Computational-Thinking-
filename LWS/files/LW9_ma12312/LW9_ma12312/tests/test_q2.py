import copy
import hashlib
import os
import sys

import pytest

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from q2 import diagonal_difference


def hashcode(value):
    return hashlib.sha256(str(value).encode("utf-8")).hexdigest()

q2_testcases = [
    ([[11, 2, 4], [4, 5, 6], [10, 8, -12]], 15, True),
    ([[1, 2], [3, 10]], 6, True),
    ([[-5]], 0, True),
    ([[2]], 0, True),
    ([[1, 2], [3, 4]], 0, True),
    ([[3, 5, 7], [1, 4, 9], [2, 8, 6]], 0, True),
    ([[10, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]], 9, True),
    ([[1, 1, 1], [1, 1, 1], [1, 1, 0]], "6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b", False),
    ([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1]], "6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b", False),
    ([[-1, -2, -3], [1, 2, 0], [1, 1, -2]], "6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b", False),
    ([[5, 1, 2], [0, 3, 4], [7, 8, 9]], "ef2d127de37b942baad06145e54b0c619a1f22327b2ebbcfbec78f5564afe39d", False),
    ([[2, 4, 6, 8], [1, 3, 5, 7], [9, 11, 13, 15], [10, 12, 14, 16]], "5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9", False),
    ([[100]], "5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9", False),
    ([[-100, 0, 0, 0, 100], [4, -90, 9, 80, -4], [1, 2, -50, 3, 4], [-7, -80, 7, 90, 6], [100, 12, 8, -15, -100]], "26d228663f13a88592a12d16cf9587caab0388b262d6d9f126ed62f9333aca94", False),
    ([[((row * 37 - col * 19) % 201) - 100 for col in range(100)] for row in range(100)], "43974ed74066b207c30ffd0fed5146762e6c60745ac977004bc14507c7c42b50", False)
]


@pytest.mark.parametrize("net_changes, expected, visible", q2_testcases)
def test_q2(net_changes, expected, visible):
    original = copy.deepcopy(net_changes)
    output = diagonal_difference(net_changes)

    assert net_changes == original, "Do not modify the input matrix."
    assert type(output) is int, "The result must be an integer."

    if visible:
        assert output == expected
    else:
        assert hashcode(output) == expected
