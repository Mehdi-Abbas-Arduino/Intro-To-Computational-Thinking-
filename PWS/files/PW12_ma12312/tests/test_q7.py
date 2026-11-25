import copy
import hashlib
import os
import sys

import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import q7
from q7 import greedy_knapsack, main


def hashcode(value):
    return hashlib.sha256(str(value).encode("utf-8")).hexdigest()


q7_testcases = [
    ({'clock': [55, 5], 'painting': [90, 9], 'toaster': [20, 4], 'vase': [50, 2], 'book': [10, 1], 'desktop': [150, 15]}, 20, 205, True),
    ({'clock': [55, 5], 'painting': [90, 9], 'toaster': [20, 4]}, 10, 90, True),
    ({'clock': [35, 5], 'painting': [40, 5], 'TV': [100, 10], 'desktop': [150, 15], 'lamp': [20, 2]}, 30, 290, True),
    ({'clock': [35, 5], 'painting': [40, 5], 'TV': [100, 10], 'desktop': [150, 15], 'lamp': [20, 2], 'book': [4, 1]}, 0, 0, True),
    ({'gold': [300, 5], 'clock': [20, 3], 'ring': [70, 2]}, 1, '5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9', False),
    ({'painting': [45, 4]}, 4, '811786ad1ae74adfdd20dd0372abaaebc6246e343aebd01da0bfc4c02bf0106c', False),
    ({'painting': [45, 4]}, 3, '5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9', False),
    ({'safe': [900, 100], 'watch': [60, 3], 'coin': [10, 2], 'vase': [50, 4]}, 7, '9bdb2af6799204a299c603994b8e400e4b1fd625efdb74066cc869fee42c9df3', False),
    ({'heavy': [100, 9], 'light1': [80, 5], 'light2': [70, 5]}, 10, 'ad57366865126e55649ecb23ae1d48887544976efea46a48eb5d85a6eeb4d306', False),
    ({'A': [100, 6], 'B': [85, 4], 'C': [55, 3], 'D': [25, 2], 'E': [10, 1]}, 9, '210e3b160c355818509425b9d9e9fd3ea2e287f2c43a13e5be8817140db0b9e6', False),
    ({'vase': [70, 10], 'pen': [40, 1], 'ring': [15, 1], 'cup': [8, 2]}, 2, '02d20bbd7e394ad5999a4cebabac9619732c343a4cac99470c03e23ba2bdc2bc', False),
    ({'diamond': [90, 4], 'laptop': [80, 4], 'radio': [50, 4]}, 8, '734d0759cdb4e0d0a35e4fd73749aee287e4fdcc8648b71a8d6ed591b7d4cb3f', False),
    ({'phone': [80, 1], 'painting': [40, 5], 'TV': [100, 10], 'desktop': [150, 15], 'lamp': [20, 2]}, 18, '1e472b39b105d349bcd069c4a711b44a2fffb8e274714bb07ecfff69a9a7f67b', False),
    ({'clock': [35, 5], 'painting': [40, 5], 'TV': [100, 10], 'desktop': [150, 15], 'lamp': [20, 2], 'book': [4, 1]}, 500, '72ba187b05e705de2dced5824d716a71872dedccf21f0c179bd2d5f2c7c974b1', False),
    ({'clock': [35, 5], 'painting': [40, 5], 'TV': [100, 10], 'desktop': [150, 15]}, 17, '9ae2bdd7beedc2e766c6b76585530e16925115707dc7a06ab5ee4aa2776b2c7b', False),
]


@pytest.mark.parametrize("items, capacity, expected, visible", q7_testcases)
def test_q7(items, capacity, expected, visible, monkeypatch, capsys):
    original = copy.deepcopy(items)

    actual = greedy_knapsack(items, capacity)
    assert items == original, "greedy_knapsack must not modify items"
    if visible:
        assert actual == expected
    else:
        assert hashcode(actual) == expected

    # Run main using the same input as the function test.
    input_lines = [str(len(items))]
    for name, pair in items.items():
        input_lines.append(f"{name} {pair[0]} {pair[1]}")
    input_lines.append(str(capacity))
    iterator = iter(input_lines)
    monkeypatch.setattr("builtins.input", lambda: next(iterator))

    # Verify that main actually calls the required function and builds
    # the dictionary values as lists [value, weight], not tuples.
    called = []
    original_function = q7.greedy_knapsack

    def checked_greedy(parsed_items, parsed_capacity):
        called.append(True)
        assert parsed_items == original
        assert parsed_capacity == capacity
        assert all(type(pair) is list and len(pair) == 2 for pair in parsed_items.values())
        assert all(type(number) is int for pair in parsed_items.values() for number in pair)
        return original_function(parsed_items, parsed_capacity)

    monkeypatch.setattr(q7, "greedy_knapsack", checked_greedy)
    main()
    assert called, "main() must call greedy_knapsack()"
    printed = capsys.readouterr().out.strip()
    if visible:
        assert printed == str(expected)
    else:
        assert hashcode(printed) == expected
