import pytest
import hashlib
import inspect
import ast
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from q9 import *

q9_testcases = [
    # Visible Testcases
    (101, "Yes", True),
    (119, "No", True),
    (158, "Yes", True),
    (291, "No", True),

    # Hidden Testcases
    (5, "85a39ab345d672ff8ca9b9c6876f3adcacf45ee7c1e2dbd2408fd338bd55e07e", False),
    (10, "85a39ab345d672ff8ca9b9c6876f3adcacf45ee7c1e2dbd2408fd338bd55e07e", False),
    (1234, "1ea442a134b2a184bd5d40104401f2a37fbc09ccf3f4bc9da161c6099be3691d", False),
    (98765, "85a39ab345d672ff8ca9b9c6876f3adcacf45ee7c1e2dbd2408fd338bd55e07e", False),
    (44444, "1ea442a134b2a184bd5d40104401f2a37fbc09ccf3f4bc9da161c6099be3691d", False),
    (90909, "85a39ab345d672ff8ca9b9c6876f3adcacf45ee7c1e2dbd2408fd338bd55e07e", False),
    (11111, "1ea442a134b2a184bd5d40104401f2a37fbc09ccf3f4bc9da161c6099be3691d", False),
    (54321, "85a39ab345d672ff8ca9b9c6876f3adcacf45ee7c1e2dbd2408fd338bd55e07e", False),
    (1001, "85a39ab345d672ff8ca9b9c6876f3adcacf45ee7c1e2dbd2408fd338bd55e07e", False),
    (99995, "85a39ab345d672ff8ca9b9c6876f3adcacf45ee7c1e2dbd2408fd338bd55e07e", False),
    (100000, "85a39ab345d672ff8ca9b9c6876f3adcacf45ee7c1e2dbd2408fd338bd55e07e", False),
]


def hashcode(n) -> str:
    return hashlib.sha256(str(n).encode("utf-8")).hexdigest()


@pytest.mark.parametrize("ticket_number, result, testcase", q9_testcases)
def test_q9(ticket_number, result, testcase):
    if testcase:
        assert lucky_ticket(ticket_number) == result
    else:
        assert hashcode(lucky_ticket(ticket_number)) == result


def test_q9_no_string_conversion():
    source = inspect.getsource(lucky_ticket)
    tree = ast.parse(source)

    for node in ast.walk(tree):

        # Reject f-strings
        assert not isinstance(node, ast.JoinedStr), \
            "Do not convert ticket_number to a string."

        if isinstance(node, ast.Call):

            # Reject str(), repr(), and format()
            if isinstance(node.func, ast.Name):
                assert node.func.id not in {"str", "repr", "format"}, \
                    "Do not convert ticket_number to a string."

            # Reject .format()
            if isinstance(node.func, ast.Attribute):
                assert node.func.attr != "format", \
                    "Do not convert ticket_number to a string."