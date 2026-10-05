import pytest
import hashlib
import inspect
import ast
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from q2 import *

q2_testcases = [
    # Visible Testcases
    (12, 18, 6, True),
    (9, 9, 9, True),
    (16, 17, 1, True),
    (32, 52, 4, True),
    (256, 128, 128, True),

    # Hidden Testcases
    (7, 7, '7902699be42c8a8e46fbbb4501726517e86b22c56a189f7625a6da49081b2451', False),
    (35, 64, '6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b', False),
    (25, 100, 'b7a56873cd771f2c446d369b649430b65a756ba278ff97ec81bb6f55b2e73569', False),
    (80, 48, 'b17ef6d19c7a5b1ee83b907c595526dcb1eb06db8227d650d5dda0a9f4ce8cd9', False),
    (97, 97, 'd6d824abba4afde81129c71dea75b8100e96338da5f416d2f69088f1960cb091', False),
    (1000, 375, '0f8ef3377b30fc47f96b48247f463a726a802f62f3faa03d56403751d2f66c67', False),
    (42, 30, 'e7f6c011776e8db7cd330b54174fd76f7d0216b612387a5ffcfb81e6f0919683', False),
    (81, 54, '670671cd97404156226e507973f2ab8330d3022ca96e0c93bdbdb320c41adcaf', False),
    (121, 44, '4fc82b26aecb47d2868c4efbe3581732a3e7cbcc6c2efb32062c08170a05eeb8', False),
    (144, 216, '8722616204217eddb39e7df969e0698aed8e599ba62ed2de1ce49b03ade0fede', False),
]

def hashcode(n: int) -> str:
    return hashlib.sha256(str(n).encode('utf-8')).hexdigest()

@pytest.mark.parametrize("juice_boxes, snack_bars, result, testcase", q2_testcases)
def test_q2(juice_boxes, snack_bars, result, testcase):
    if testcase == True:
        assert max_equal_guests(juice_boxes, snack_bars) == result
    else:
        assert hashcode(max_equal_guests(juice_boxes, snack_bars)) == result

def test_q2_no_gcd_function():
    source = inspect.getsource(max_equal_guests)
    tree = ast.parse(source)

    for node in ast.walk(tree):

        if isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name) and node.func.id == "gcd":
                pytest.fail(
                    "Do not use the gcd() function. "
                    "Solve the question using iteration."
                )

        if isinstance(node, ast.Call):
            if (
                isinstance(node.func, ast.Attribute)
                and node.func.attr == "gcd"
            ):
                pytest.fail(
                    "Do not use the gcd() function. "
                    "Solve the question using iteration."
                )

        if isinstance(node, ast.ImportFrom):
            for name in node.names:
                if name.name == "gcd":
                    pytest.fail(
                        "Do not import or use gcd(). "
                        "Solve the question using iteration."
                    )