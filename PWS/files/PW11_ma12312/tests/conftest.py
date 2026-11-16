"""Check mandatory worksheet rules, and avoid redundant errors for unfinished code.

Each question has one explicit rules test. When it fails, its other tests are
skipped until the student fixes the mandatory rule violation.
"""
import importlib
import re
from functools import lru_cache

import pytest

from _pw_rules import validate_rules
from _pw_runner import run_solution

# These same public inputs are used by the explicit recursion tests. Once a
# representative recursive call fails, functional cases are skipped instead
# of accidentally receiving most of their marks for a nonrecursive solution.
_RECURSION_CASES = {
    1: [('gcd', (2322, 654))],
    2: [('add_check_digit', (7172,)), ('verify_check_digit', (678291,))],
    3: [('diamond', (3,))],
    4: [('chickens_needed', (2, 3, 5, 6))],
    5: [('dot', ([0, -3, 6], [4, 9, 1]))],
    6: [('minmax', ([0, -3, 6, 4, 9, 1],))],
    7: [('check_types', (['hello', [2, [False, [3.5]]], 'world'],))],
    8: [('pop_bubbles', ('abbcccbbba', 3))],
    9: [('create_scroll', ('aab', 'cck'))],
}


@lru_cache(maxsize=None)
def _recursion_failure(question):
    for func, args in _RECURSION_CASES.get(question, []):
        try:
            outcome = run_solution(question, func, *args)
        except AssertionError as exc:
            return f'{func}() failed the required recursion check: {exc}'
        if not outcome.recursion_executed:
            return (f'{func}() did not actually execute recursion on the '
                    'representative input. See the explicit recursion test.')
    return None


@pytest.fixture(autouse=True)
def enforce_question_rules(request):
    match = re.fullmatch(r'test_q(\d+)', request.module.__name__)
    if match is None:
        return
    question = int(match.group(1))
    if request.node.name == f'test_q{question}_rules':
        # Let the explicit rules test report the one actionable failure.
        return
    module = importlib.import_module('q%d' % question)
    try:
        validate_rules(module, question)
    except AssertionError as exc:
        pytest.skip(f'Fix the Q{question} rule failure first: {exc}')
    if 'recursion_executed' not in request.node.name:
        failure = _recursion_failure(question)
        if failure:
            pytest.skip(f'Fix the Q{question} recursion requirement first: {failure}')
