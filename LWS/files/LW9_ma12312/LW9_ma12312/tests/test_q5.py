import hashlib
import os
import sys

import pytest

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from q5 import get_frequent_items


def hashcode(items):
    return hashlib.sha256(str(sorted(items)).encode("utf-8")).hexdigest()


q5_testcases = [
    ([['Chai', 'Samosa', 'Biscuit'], ['Chai', 'Paratha', 'Omelette'],
      ['Pizza Slice', 'Pepsi', 'Fries'], ['Biryani', 'Raita', 'Lassi'],
      ['Bun Kabab', 'Fries', 'Pepsi'], ['Samosa', 'Roll', 'Jalebi']],
     'Pepsi',
     ['Fries'], True),

    ([['Chai', 'Samosa', 'Paratha', 'Cake Rusk'], ['Chai', 'Biscuit', 'Samosa'],
      ['Samosa', 'Cold Coffee', 'Biscuit'], ['Pizza Slice', 'Fries', 'Pepsi', 'Brownie'],
      ['Omelette', 'Paratha', 'Lassi', 'Samosa'], ['Biscuit', 'Chai', 'Samosa', 'Pakora'],
      ['Chai', 'Biscuit', 'Paratha']],
     'Chai',
     ['Biscuit', 'Samosa'], True),

    ([['Chai', 'Samosa', 'Biscuit'], ['Chai', 'Paratha', 'Omelette'],
      ['Pizza Slice', 'Pepsi', 'Fries'], ['Biryani', 'Raita', 'Lassi'],
      ['Bun Kabab', 'Fries', 'Pepsi'], ['Samosa', 'Roll', 'Jalebi']],
     'Brownie',
     [], True),

    ([['Pepsi', 'Pizza'], ['Milk', 'Tea', 'Sugar'], ['Tissue Box', 'Air Freshner'],
      ['Tea', 'Bread', 'Eggs', 'Butter'], ['Pizza', 'Pepsi', 'Chips'],
      ['Meat', 'Yogurt', 'Onion', 'Tomato', 'Potatoes'], ['Bun', 'Patties', 'Chips', 'Pepsi'],
      ['Samosa', 'Roll', 'Jalebi']],
     'Pepsi',
     ['Chips', 'Pizza'], True),

    ([['Pepsi', 'Pizza'], ['Milk', 'Tea', 'Sugar'], ['Tissue Box', 'Air Freshner'],
      ['Tea', 'Bread', 'Eggs', 'Butter'], ['Pizza', 'Pepsi', 'Chips'],
      ['Meat', 'Yogurt', 'Onion', 'Tomato', 'Potato'], ['Bun', 'Patties', 'Chips', 'Pepsi'],
      ['Samosa', 'Roll', 'Jalebi']],
     'Coffee',
     [], True),

    ([],
     'Pepsi',
     [], True),
    ([['Meat', 'Yogurt', 'Tomato', 'Rice'], ['Meat', 'Onion', 'Yogurt'],
      ['Yogurt', 'Flour', 'Onion'], ['Sugar', 'Oil', 'Soap', 'Detergent'],
      ['Eggs', 'Bread', 'Butter', 'Yogurt'], ['Onion', 'Meat', 'Yogurt', 'Spices'],
      ['Meat', 'Onion', 'Tomato']],
     'Meat',
     ['Onion', 'Yogurt'], True),

    ([['Meat', 'Yogurt', 'Tomato', 'Rice'], ['Meat', 'Onion', 'Yogurt'],
      ['Yogurt', 'Flour', 'Onion'], ['Sugar', 'Oil', 'Soap', 'Detergent'],
      ['Eggs', 'Bread', 'Butter', 'Yogurt'], ['Onion', 'Meat', 'Yogurt', 'Spices'],
      ['Meat', 'Onion', 'Tomato']],
     "",
     [], True),

    ([['Meat', 'Yogurt', 'Tomato', 'Rice'], ['Meat', 'Onion', 'Yogurt'],
      ['Yogurt', 'Flour', 'Onion'], ['Sugar', 'Oil', 'Soap', 'Detergent'],
      ['Eggs', 'Bread', 'Butter', 'Yogurt'], ['Onion', 'Meat', 'Yogurt', 'Spices'],
      ['Meat', 'Onion', 'Tomato']],
     'Tomato',
     ['Meat'], True),

    ([['Tomato'], ['Potato'], ['Onion'], ['Garlic']],
     "Tomato",
     [], True),

    ([['Samosa', 'Jalebi'], ['Roll', 'Jalebi'], ['Samosa', 'Roll', 'Jalebi'],
      ['Samosa', 'Roll', 'Gulab Jamun'], ['Samosa', 'Biscuits', 'Roll'],
      ['Roll', 'Biscuits', 'Jalebi'], ['Samosa']],
     'Samosa',
     ['Roll'], True),

    ([['Samosa', 'Biscuits', 'Roll'], ['Samosa', 'Jalebi'], ['Roll', 'Jalebi'],
      ['Samosa', 'Roll', 'Jalebi'], ['Samosa', 'Roll', 'Gulab Jamun'], ['Samosa'], ['Jalebi'],
      ['Roll', 'Biscuits', 'Jalebi'], ['Samosa', 'Jalebi']],
     'Jalebi',
     ['Roll', 'Samosa'], True),

    ([['Chai']],
     'Chai',
     '4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945', False),

    ([['chai', 'Cookie'], ['Chai', 'Biscuit'], ['Chai', 'Biscuit'], ['chai', 'Sugar']],
     'Chai',
     '0d2b92a1fd5ca818bf66ade64de040a8d5e1b60f060362adc7327dae1e0d88de', False),

    ([['Tea', 'Cake', 'Juice'], ['Tea', 'Cake', 'Bun'], ['Tea', 'Bun', 'Juice'], ['Tea']],
     'Tea',
     '9a56346e8ab73e67747e5ddafd276efcf95a0f21901564a1e545228b68cfbe5d', False)
]


@pytest.mark.parametrize("orders, target_item, expected, visible", q5_testcases)
def test_q5(orders, target_item, expected, visible):
    result = get_frequent_items(orders, target_item)
    assert isinstance(result, list), "Return a list of item names."
    assert all(isinstance(item, str) for item in result), (
        "Every returned item must be a string."
    )
    if visible:
        assert sorted(result) == sorted(expected)
    else:
        assert hashcode(result) == expected