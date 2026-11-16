import copy
import hashlib
import os
import sys

import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
sys.path.insert(0, os.path.dirname(__file__))
import q7
from _pw_runner import run_solution
from _pw_rules import validate_rules, assert_recursion_executed


q7_testcases = [
    ([], [], True),
    ([2, 3, 5], ['int'], True),
    (['Programming', 'List', 'Fundamentals'], ['str'], True),
    ([5, 6, 'six', ['eight', 'nine'], True], ['int', 'str', 'list', 'bool'], True),
    (['hello', [2, [False, [3.5]]], 'world'], ['str', 'list', 'int', 'bool', 'float'], True),
    ('this is not right', "Error: Bad argument. Function 'check_types' only accepts lists", True),

    ([True, 1, 1.0], '641ebd5a1fd9410e4b6e25e34e74d3b5a976c339a11fdaa558199dec02a59309', False),
    ([[], []], 'bedf2350927adc6810833f2d58722c46124b0ca91d413437af76a9d3fffb5a8d', False),
    ([[[]]], 'bedf2350927adc6810833f2d58722c46124b0ca91d413437af76a9d3fffb5a8d', False),
    ([[], 1, False, 1.0, 'x', [1, 'hello'], 2],
     '94aa72c5b1d0022c80d7e3839ba24f7f7ce9b2d1f07e2860a02c1b501babc299', False),
    ([False, 0, True, 1, 0.0, '0'],
     '5eb5f0be28aa63f0a54257990e3a2532cca1235e7d2ff56a7082bf8d3e1b7636', False),
    (['a', [1, 'b'], [True, []], 1.5],
     '12b374822a4e531e2a396fdc5ebbf158b83aeb5902ede4e60a40c54ecd7de2bd', False),
    ([[[[[[[[42]]]]]]]], 'ec697cc6edce7b1d19e2e42b72ca8206f42e9b138620061ede1dada30282b043', False),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
      0, 0, [], False, 1.5, 'end', 2],
     '25fe238af208d9f40b6d26a2c547de2d8880e34cc53e326709f51a87760d0d92', False),
    (1234, 'f11775ea2483f41d6a71e590961acb9446e8642b9640d866a7b857bc59b8a43b', False),
    ([1, 'hello', 2], 'ddc0e83cbff46def1889e8bcd3d7e1a7037a4694bfc64c54036b0286e745d803', False),
    ([[1], 2], 'ec697cc6edce7b1d19e2e42b72ca8206f42e9b138620061ede1dada30282b043', False),
    ([1, [2]], 'abb908804d1b6e305446df4907e788f15ec174fcc46ba579781d1185752bacac', False),
    ([[], [], 0], 'ec697cc6edce7b1d19e2e42b72ca8206f42e9b138620061ede1dada30282b043', False),
    ([True, [1, 2], 1.0, 'x'], 'f657b4649fba7477efb6a7837ec478857cee4d5b05be6fcf7adec4b6cc418382', False),
]


def test_q7_rules():
    validate_rules(q7, 7)


def test_q7_recursion_executed():
    assert_recursion_executed(q7, q7.check_types,
                              (['hello', [2, [False, [3.5]]], 'world'],))


@pytest.mark.parametrize('items, expected, visible', q7_testcases)
def test_q7(items, expected, visible):
    before = copy.deepcopy(items)
    outcome = run_solution(7, 'check_types', items)
    result = outcome.value
    assert outcome.arguments_after[0] == before, 'Do not modify the input list or nested lists.'
    if type(items) is list:
        assert outcome.result_type == 'list', 'Return a list of unique type names.'
    else:
        assert outcome.result_type == 'str', 'Return the specified error string for invalid inputs.'
    if visible:
        assert result == expected
    else:
        assert hashlib.sha256(str(result).encode('utf-8')).hexdigest() == expected
