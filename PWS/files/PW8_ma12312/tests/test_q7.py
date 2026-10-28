import hashlib
import os
import sys
import pytest

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from q7 import *

def hashcode(value):
    return hashlib.sha256(str(value).encode("utf-8")).hexdigest()

q7_testcases = [
    # Visible Testcases
    (0, 1, [1], True),
    (2, 8, [2, 5, 14, 42, 132, 429], True),
    (0, 8, [1, 1, 2, 5, 14, 42, 132, 429], True),
    (3, 6, [5, 14, 42], True),
    (5, 10, [42, 132, 429, 1430, 4862], True),

    # Hidden Testcases
    (11, 21, '9f61c148cf311d3d3ce1ca00e5c848575bb6c7e97a060146df92750ba92ecbec', False),
    (0, 15, 'a40ac8453a7ba9f6729c86025f73a44cd21991ebc1e0ba5645a072bf9f9ab12d', False),
    (6, 15, '56db055bb8078431ea4d95f6793e899a37cb3e6c8351a761b0afd0adc1ddaeae', False),
    (17, 42, 'c4def6de22cb7f74eae5b1effad532a9c910a68032e2f10718c2a4677552b371', False),
    (1, 2, '080a9ed428559ef602668b4c00f114f1a11c3f6b02a435f0bdc154578e4d7f22', False),
    (1, 5, '2d7f579f4f0e6748d7b573d737bd22f938f7730e76c7314f8eb37cec07260d86', False),
    (4, 9, 'eecde960282111f12cfff40cc8484718a0963506fc6e8fe5849dfdadf7071843', False),
    (8, 18, '1ec2956b23218ccb7a0c442a7fa5badffe588a7630ceaaaeda47d31ce602bfdf', False),
    (20, 30, '69d972a11e519acb8cb776c77d24667c4dbb423cbfcee8be222f5ee6141e8858', False),
    (25, 35, '727367caf306441df4f2e7518385eb4743519f1faca6a429df8a918d69ff25e5', False),
]

@pytest.mark.parametrize("j, k, expected, visible", q7_testcases)
def test_q7(j,k,expected,visible):
    result=catalan(j,k)
    assert isinstance(result,list)
    assert len(result)==k-j
    assert all(isinstance(v,int) for v in result)
    if visible:
        assert result == expected
    else:
        assert hashcode(result) == expected
