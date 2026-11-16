import hashlib
import os
import sys

import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
sys.path.insert(0, os.path.dirname(__file__))
import q3
from _pw_runner import run_solution
from _pw_rules import validate_rules, assert_recursion_executed


q3_testcases = [
    (1, '*', True),
    (2, ' *\n* *\n *', True),
    (4, '   *\n  * *\n * * *\n* * * *\n * * *\n  * *\n   *', True),
    (7, '      *\n     * *\n    * * *\n   * * * *\n  * * * * *\n * * * * * *\n* * * * * * *\n * * * * * *\n  * * * * *\n   * * * *\n    * * *\n     * *\n      *', True),
    (10, '         *\n        * *\n       * * *\n      * * * *\n     * * * * *\n    * * * * * *\n   * * * * * * *\n  * * * * * * * *\n * * * * * * * * *\n* * * * * * * * * *\n * * * * * * * * *\n  * * * * * * * *\n   * * * * * * *\n    * * * * * *\n     * * * * *\n      * * * *\n       * * *\n        * *\n         *', True),

    (6, 'df22723c0053639ceb0862fa913fc7291358bc6a57693acba9c1517d1d567edd', False),
    (12, '743a1b7c03e2fdd4540bf983e9fad2203232e0a60b1ce99bf803cecb9bd045ca', False),
    (19, '4c8a6535e4ed5f2bf1f9b36fd3ea5c574fbc9a52188dc31c97b3e1e131d06d69', False),
    (28, '3d7dbf25d2acb6b101c8a0e41b6368fcbd53ade5342b40978c7ca753a7a89757', False),
    (15, 'a9af18930bb069266d24e44870fd02e3313702fd8fb6bd112208b90b8c66bd14', False),
    (3, '33a99d6239ef7ef2f86b4e9e0e89099ae13e455d9689e4a90f9104c87ccf2752', False),
    (5, '4d264de4d89c023d05852a459851a6e02907f477c2653cb6c0c2c798edaeb0ea', False),
    (8, '2b1f40dc6c2265c4bf24ea7cb344714f265b78adc0c215666bcc6af37bbc00d0', False),
    (33, 'e25cfbbf3ac19105cfbe4490ee094e967f88234bc26c7b01f48bc71adf84df14', False),
    (50, '18d2aa31983ee4e2bfe415e21e65012462a88c2dc0229ab930e6e2c454af05d6', False),
]



def test_q3_rules():
    validate_rules(q3, 3)


def test_q3_recursion_executed():
    assert_recursion_executed(q3, q3.diamond, (3,))


@pytest.mark.parametrize('size, expected, visible', q3_testcases)
def test_q3(size, expected, visible):
    outcome = run_solution(3, 'diamond', size)
    result = outcome.value
    assert outcome.result_type == 'str', "Return a str."
    assert '\r' not in result, "Rows must be separated by a new line character only."
    assert not result.endswith('\n'), "The string must not end with a new line."
    result = '\n'.join(row.rstrip(' ') for row in result.split('\n'))
    if visible:
        expected = '\n'.join(row.rstrip(' ') for row in expected.split('\n'))
        assert result == expected
    else:
        assert hashlib.sha256(str(result).encode('utf-8')).hexdigest() == expected
