import copy
import hashlib
import os
import sys

import pytest

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from q3 import add_study_hours


def hashcode(value):
    return hashlib.sha256(str(value).encode("utf-8")).hexdigest()


q3_testcases = [
    ([[4, 8], [3, 7]], [[1, 0], [5, 2]], [[5, 8], [8, 9]], True), 
    ([[5, 2], [0, 1], [1, 9]], [[2, 3], [4, 1], [0, 2]], [[7, 5], [4, 2], [1, 11]], True),
    ([[1], [2]], [[3, 5], [4, 6]], "Grids don't have the same dimensions.", True),
    ([[12, 7, 3], [4, 5, 6], [7, 8, 9]], [[5, 8, 1], [6, 7, 3], [4, 5, 9]], [[17, 15, 4], [10, 12, 9], [11, 13, 18]], True),
    ([[1, 2], [0, 3], [6, 7]], [[4, 5], [7, 8]], "Grids don't have the same dimensions.", True),
    ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[9, 8, 7], [6, 5, 4], [3, 2, 1]], 'bc3d3382ef7e3c6035ca629ee6343b0473a36c1ff1e9958997b9e5b95319b502', False),
    ([[0, 1, 2], [9, 8, 7]], [[6, 5, 4], [3, 4, 5]], '1f1b921a5aca627fb5dc09ba30663d83ed313c9afaa2f1d16ec425d62b15fe0c', False),
    ([[1], [1], [1]], [[2], [2], [4]], '1f52583532426b1f02ba8a8f234a2a2912ed7b8d19a4481564c92a6a02c3a6a7', False),
    ([[1, 1, 1]], [[2, 2, 4]], '7abcc72ef8ad7d64feff987fe230b1a8b33efe515d7afae9d8cfee783c67c6dd', False),
    ([[1, 2], [0, 3]], [[4, 5, 6], [7, 8, 9]], '721c625b74eeff5e7aef74a9a83f2c982ccffd253c1a1c0c0e66674b15b01b9e', False),
    ([[12]], [[12]], '84377fa78279b94980226e19983054b7c579c97cdbc8921c843b174d35fd0012', False),
    ([[1, 2, 3, 4, 5, 6, 7]], [[7, 6, 5, 4, 3, 2, 1]], '4a164d6f71349454a3a7db3ccaa2335f5dd4429545b9c5ebc815e97d6e837dc2', False),
    ([[0, 3, 6, 9, 12, 2, 5], [2, 5, 8, 11, 1, 4, 7], [4, 7, 10, 0, 3, 6, 9], [6, 9, 12, 2, 5, 8, 11], [8, 11, 1, 4, 7, 10, 0], [10, 0, 3, 6, 9, 12, 2]], [[1, 6, 11, 3, 8, 0, 5], [5, 10, 2, 7, 12, 4, 9], [9, 1, 6, 11, 3, 8, 0], [0, 5, 10, 2, 7, 12, 4], [4, 9, 1, 6, 11, 3, 8], [8, 0, 5, 10, 2, 7, 12]], 'ad197a5542c7f6109423d55b04136a94d1b44537854362c5967f4a3dd65919fe', False),
    ([[3, 6, 9], [4, 8, 12]], [[2, 4, 6], [1, 3, 5], [7, 8, 9]], '721c625b74eeff5e7aef74a9a83f2c982ccffd253c1a1c0c0e66674b15b01b9e', False),
    ([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], '99bc33c74625e4db96cf4c6900ececf74e45f08216f7b6c9a9c5f1225b6ce7ef', False)
]


@pytest.mark.parametrize("campus_hours, home_hours, expected, visible", q3_testcases)
def test_q3(campus_hours, home_hours, expected, visible):
    original_campus = copy.deepcopy(campus_hours)
    original_home = copy.deepcopy(home_hours)
    result = add_study_hours(campus_hours, home_hours)

    assert campus_hours == original_campus, "Do not modify campus_hours."
    assert home_hours == original_home, "Do not modify home_hours."
    dimensions_match = (len(campus_hours) == len(home_hours)
                        and len(campus_hours[0]) == len(home_hours[0]))
    if dimensions_match:
        assert type(result) is list, "Return a nested list for matching grids."
        assert all(type(row) is list for row in result), "Return a nested list."
    else:
        assert type(result) is str, "Return the specified error string for mismatched grids."

    if visible:
        assert result == expected
    else:
        assert hashcode(result) == expected
