import pytest
import hashlib
import ast
import inspect
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from q5 import *


q5_testcases = [
    # Visible Testcases
    (12345, 54321, True),
    (33602, 20633, True),
    (1200, 21, True),
    (507, 705, True),
    (91, 19, True),

    # Hidden Testcases
    (5600, "108c995b953c8a35561103e2014cf828eb654a99e310f87fab94c2f4b7d2a04f", False),
    (7, "7902699be42c8a8e46fbbb4501726517e86b22c56a189f7625a6da49081b2451", False),
    (100000, "6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b", False),
    (40050, "6078ab6da8612a510479dcb8b82d13bd492ca3666578f77b98b563f78453af2c", False),
    (90909, "8068bfc9883ac82ffd51d27e3b3e0350355f1f10411359c63f4fc4472bcfc999", False),
    (10001, "e443169117a184f91186b401133b20be670c7c0896f9886075e5d9b81e9d076b", False),
    (24680, "b03fad7e896f0497f4f3c88a5bb083c8976608495abbf14b476e6a4bb6fd2c7f", False),
    (10010, "fe675fe7aaee830b6fed09b64e034f84dcbdaeb429d9cccd4ebb90e15af8dd71", False),
    (99999, "fd5f56b40a79a385708428e7b32ab996a681080a166a2206e750eb4819186145", False),
    (10203, "56c1b52704dad7bf126b970878593341983de81021196461e1bbc20c4808fc05", False),
]


def hashcode(n) -> str:
    return hashlib.sha256(str(n).encode("utf-8")).hexdigest()


@pytest.mark.parametrize("locker_number, result, testcase", q5_testcases)
def test_q5(locker_number, result, testcase):
    if testcase:
        assert reverse_number(locker_number) == result
    else:
        assert hashcode(reverse_number(locker_number)) == result


def test_q5_no_string_conversion():
    source = inspect.getsource(reverse_number)
    tree = ast.parse(source)

    for node in ast.walk(tree):

        if isinstance(node, ast.JoinedStr):
            pytest.fail(
                "Do not convert locker_number to a string. "
                "Solve the question arithmetically."
            )

        if isinstance(node, ast.Call):

            if isinstance(node.func, ast.Name):
                if node.func.id in {"str", "repr", "format"}:
                    pytest.fail(
                        "Do not convert locker_number to a string. "
                        "Solve the question arithmetically."
                    )

            if isinstance(node.func, ast.Attribute):
                if node.func.attr == "format":
                    pytest.fail(
                        "Do not use string formatting to reverse the number. "
                        "Solve the question arithmetically."
                    )