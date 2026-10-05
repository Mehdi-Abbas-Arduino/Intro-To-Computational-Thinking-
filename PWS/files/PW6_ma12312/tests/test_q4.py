import pytest
import hashlib
import ast
import inspect
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from q4 import minimum_reversals

def hashcode(value):
    return hashlib.sha256(str(value).encode("utf-8")).hexdigest()

q4_testcases = [
    # Visible Testcases
    ('00111', 0, True), 
    ('111000', 1, True), 
    ('010101', 2, True), 
    
    # Hidden Testcases
    ('0', '5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9', False), 
    ('1', '5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9', False), 
    ('01', '5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9', False),
    ('10', '6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b', False), 
    ('1010', 'd4735e3a265e16eee03f59718b9b5d03019c07d8b6c51f90da3a666eec13ab35', False), 
    ('01010', 'd4735e3a265e16eee03f59718b9b5d03019c07d8b6c51f90da3a666eec13ab35', False), 
    ('11001100', 'd4735e3a265e16eee03f59718b9b5d03019c07d8b6c51f90da3a666eec13ab35', False), 
    ('000111', '5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9', False), 
    ('111111', '5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9', False), 
    ('000000', '5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9', False), 
    ('100001', '6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b', False), 
    ('10101010', '4b227777d4dd1fc61c6f884f48641d02b4d121d3fd328cb08b5531fcacdabf8a', False), 
    ('00110011', '6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b', False), 
    ('11010100', '4e07408562bedb8b60ce05c1decfe3ad16b72230967de01f640b7e4729b49fce', False), 
    ('0111100001', '6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b', False), 
    ('101', '6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b', False), 
    ('10010', 'd4735e3a265e16eee03f59718b9b5d03019c07d8b6c51f90da3a666eec13ab35', False)
]

@pytest.mark.parametrize("binary_string, expected, visible", q4_testcases)
def test_q4(binary_string, expected, visible):
    if visible:
        assert minimum_reversals(binary_string) == expected
    else:
        assert hashcode(minimum_reversals(binary_string)) == expected