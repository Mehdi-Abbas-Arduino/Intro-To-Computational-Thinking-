import copy
import hashlib
import os
import sys

import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

sys.path.insert(0, os.path.dirname(__file__))

from q4 import num_toppings


def hashcode(value):
    return hashlib.sha256(str(value).encode('utf-8')).hexdigest()


q4_testcases = [
    ({'olives': 250, 'chicken': 350, 'onions': 150, 'tomatoes': 200, 'pineapple': 300}, 700, 4, True),
    ({'olives': 250, 'chicken': 350, 'onions': 150, 'tomatoes': 200, 'pineapple': 300}, 550, '5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9', False),
    ({'olives': 250, 'chicken': 350, 'onions': 150, 'tomatoes': 200, 'pineapple': 300}, 650, 'd4735e3a265e16eee03f59718b9b5d03019c07d8b6c51f90da3a666eec13ab35', False),
    ({'olives': 250, 'chicken': 350, 'onions': 150, 'tomatoes': 200, 'pineapple': 300}, 750, 'e7f6c011776e8db7cd330b54174fd76f7d0216b612387a5ffcfb81e6f0919683', False),
    ({'olives': 250, 'chicken': 350, 'onions': 150, 'tomatoes': 200, 'pineapple': 300}, 800, '2c624232cdd221771294dfbb310aca000a0df6ac8b66b696d90ef06fdefb64a3', False),
    ({'olives': 250, 'chicken': 350, 'onions': 150, 'tomatoes': 200, 'pineapple': 300}, 850, '19581e27de7ced00ff1ce50b2047e7a567c76b1cbaebabe5ef03f7c3017bb5b7', False),
    ({'olives': 250, 'chicken': 350, 'onions': 150, 'tomatoes': 200, 'pineapple': 300}, 900, '4a44dc15364204a80fe80e9039455cc1608281820fe2b24f1e5233ade6af1dd5', False),
    ({'olives': 250, 'chicken': 350, 'onions': 150, 'tomatoes': 200, 'pineapple': 300}, 950, '4a44dc15364204a80fe80e9039455cc1608281820fe2b24f1e5233ade6af1dd5', False),
    ({'olives': 250, 'chicken': 350, 'onions': 150, 'tomatoes': 200, 'pineapple': 300}, 1000, '4a44dc15364204a80fe80e9039455cc1608281820fe2b24f1e5233ade6af1dd5', False),
    ({'olives': 250, 'chicken': 350, 'onions': 150, 'tomatoes': 200, 'pineapple': 300}, 400, 0, True),
    ({'olives': 100, 'onions': 150, 'tomatoes': 200}, 450, 1, True),
    ({'red': 100, 'green': 100, 'blue': 100, 'yellow': 100}, 300, '4b227777d4dd1fc61c6f884f48641d02b4d121d3fd328cb08b5531fcacdabf8a', False),
    ({'paneer': 75, 'corn': 50, 'peppers': 25, 'olives': 100, 'mushrooms': 60, 'chicken': 200}, 160, '4e07408562bedb8b60ce05c1decfe3ad16b72230967de01f640b7e4729b49fce', False),
    ({'a': 15, 'b': 25, 'c': 35}, 74, '5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9', False),
    ({'cap': 7, 'onion': 11, 'chili': 17, 'garlic': 19, 'tomato': 23, 'pepper': 29, 'olive': 31}, 65, 'b7a56873cd771f2c446d369b649430b65a756ba278ff97ec81bb6f55b2e73569', False),
]


@pytest.mark.parametrize('toppings,budget,expected,is_visible', q4_testcases)
def test_q4(toppings, budget, expected, is_visible):
    original = copy.deepcopy(toppings)
    result = num_toppings(toppings, budget)

    assert type(result) is int
    assert toppings == original
    if is_visible:
        assert result == expected
    else:
        assert hashcode(result) == expected
