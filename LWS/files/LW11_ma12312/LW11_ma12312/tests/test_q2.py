import hashlib
import os
import sys

import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
sys.path.insert(0, os.path.dirname(__file__))
import q2
from _lw11_rules import validate_rules, assert_recursion_executed


q2_testcases = [
    # Visible testcases
    (-3, '-11', True),
    (0, '0', True),
    (156, '10011100', True),
    (42, '101010', True),
    (-40, '-101000', True),
    (-42, '-101010', True),
    (1, '1', True),
    (8, '1000', True),

    # Hidden testcases
    (-1, '1bad6b8cf97131fceab8543e81f7757195fbb1d36b376ee994ad1cf17699c464', False),
    (-1024, 'a3b616cdac42b49a56bc977d4e701e0eb3d8c8a6248b15de8339281d2a891c3c', False),
    (999, '0df93b22560393c6b551bcbe472c4108a8b59762107bb15c68d41257b4c8e9cd', False),
    (2, '4a44dc15364204a80fe80e9039455cc1608281820fe2b24f1e5233ade6af1dd5', False),
    (7, 'f6e0a1e2ac41945a9aa7ff8a8aaa0cebc12a3bcc981a929ad5cf810a090e11ae', False),
    (-2, 'c171d4ec282b23db89a99880cd624e9ba2940c1d894783602edab5d7481dc1ea', False),
    (1000000000, 'b3f00683bdf264caa73f6725512d8e11d1be423030480f4c360f1f9313403de5', False),
]



def test_q2_rules():
    validate_rules(q2, 2)


def test_q2_recursion_executed():
    assert_recursion_executed(q2, q2.to_binary, (156,))


@pytest.mark.parametrize('number, expected, visible', q2_testcases)
def test_q2(number, expected, visible):
    result = q2.to_binary(number)
    assert isinstance(result, str), "Return a str."
    if visible:
        assert result == expected
    else:
        assert hashlib.sha256(result.encode("utf-8")).hexdigest() == expected