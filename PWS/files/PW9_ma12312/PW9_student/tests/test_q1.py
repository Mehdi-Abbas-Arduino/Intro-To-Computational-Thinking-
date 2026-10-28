import hashlib
import os
import sys
from copy import deepcopy
from decimal import Decimal

import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from q1 import compute_my_bill


def normalized(value):
    if isinstance(value, list):
        return [normalized(element) for element in value]
    if isinstance(value, bool):
        return ("bool", value)
    if isinstance(value, (int, float)):
        return ("number", str(Decimal(str(value)).normalize()))
    if isinstance(value, str):
        return ("text", value)
    return value


def hashcode(value):
    return hashlib.sha256(str(normalized(value)).encode("utf-8")).hexdigest()


q1_testcases = [
    ([['Milk', 10.99, 2], ['Cake', 12.5, 5], ['Tapal Family Mixture', 450, 1], ['Shan Bombay Biryani', 70, 2]], [['Milk', 10.99, 2, 21.98], ['Cake', 12.5, 5, 62.5], ['Tapal Family Mixture', 450, 1, 450], ['Shan Bombay Biryani', 70, 2, 140], ['Quantity', 10, 'Total Bill', 674.48]], True),
    ([['Lux Soap', 45.87, 6], ['Zeera Plus', 20, 10], ['Dry Dates', 160, 3], ['Lipton Green Tea', 120, 2]], [['Lux Soap', 45.87, 6, 275.22], ['Zeera Plus', 20, 10, 200], ['Dry Dates', 160, 3, 480], ['Lipton Green Tea', 120, 2, 240], ['Quantity', 21, 'Total Bill', 1195.22]], True),
    ([['Pen', 0.99, 10], ['Notebook', 2.5, 5], ['Printer', 150.75, 2], ['Desk Chair', 50, 1]], [['Pen', 0.99, 10, 9.9], ['Notebook', 2.5, 5, 12.5], ['Printer', 150.75, 2, 301.5], ['Desk Chair', 50, 1, 50], ['Quantity', 18, 'Total Bill', 373.9]], True),
    ([['Apple', 3.0, 10], ['Banana', 3.0, 8], ['Orange', 3.0, 12]], [['Apple', 3.0, 10, 30.0], ['Banana', 3.0, 8, 24.0], ['Orange', 3.0, 12, 36.0], ['Quantity', 30, 'Total Bill', 90.0]], True),
    ([], [['Quantity', 0, 'Total Bill', 0]], True),
    ([['Rice', 1.99, 50], ['Sugar', 2.49, 60]], 'a228995e1c1f8cbde725e9c82ff85d233433af2d60de72f088bf064f005018fa', False),
    ([['Gum', 0.99, 20], ['Candy', 0.5, 30], ['Mint', 0.75, 25]], '036266d7c33688e66858e8dda3c84871a34fac479e141cc044c4c84a657c21a2', False),
    ([['Smartphone', 599.99, 1], ['Charger', 20.0, 2], ['USB Cable', 5.0, 3]], '1b52658455ab9b63e1e1ad61e37c8e0429656405b774f0f6bc5850194cffa545', False),
    ([['Laptop', 799.99, 1], ['Keyboard', 29.99, 2], ['Mouse', 15.99, 3], ['Headphones', 100.0, 2]], 'df7eb8585c1f9ffaee06aaee1fb5155883bc656c043b6f0302fe6eba90677a82', False),
    ([['Free Sample', 0, 2], ['Gift Bag', 0.0, 1]], '48e99ec9cf9e12666b287bb138e99cacedf533367745170ab0f3a0db3ad7b055', False),
    ([['Bread', 3.4, 2], ['Bread', 3.4, 1], ['Eggs', 0.25, 12]], 'd29c339cfb5d9120d9c8672087b56562e7d542e6d1a2c64f9b33bd6f26529578', False),
    ([['Water', 0.01, 1]], '4d527a29fd5a7f1f97d0a7ee7aad9c0e783f20a8679e3a94cef55cd96795938e', False),
    ([['Cookies', 0.1, 3], ['Juice', 0.2, 4]], '8696b13b909e1c66624ebe10ebed8bbe9e9e7fe083d0b9c435f6a21590bd848f', False),
    ([['Zebra Fruit', 5.0, 1], ['Apple', 1.25, 3], ['Mango', 0.85, 2]], '5996779e37feff40b75c8977f6e976e55ac9c06e4bd9c3a7ad9e1cc6f3abaaf5', False),
    ([['Party Cups', 0.45, 120], ['Napkins', 0.02, 1500], ['Ice', 2.5, 20]], '5c7fc67cd771b65098ee60990ecbfaddd7cb631b124219e947f0f87280905121', False),
]


@pytest.mark.parametrize("purchased_items, expected, visible", q1_testcases)
def test_q1(purchased_items, expected, visible):
    original_items = deepcopy(purchased_items)
    receipt = compute_my_bill(purchased_items)
    assert purchased_items == original_items, "The original purchased_items list must not be modified."
    assert isinstance(receipt, list), "The function must return a nested list."
    if visible:
        assert receipt == expected, f"{receipt!r} != {expected!r}"
    else:
        assert hashcode(receipt) == expected, "Incorrect receipt or total for this hidden test case."