import pytest
import hashlib
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from q4 import *

q4_testcases = [
    # Visible Testcases
    ("abxy", "Sad", True),
    ("abcdeeafg", "Happy", True),
    ("aeiou", "Happy", True),
    ("abedfeg", "Sad", True),
    ("ewkiaou", "Happy", True),

    # Hidden Testcases
    ("aei", "725accb5a8e46d19bc3f3a7636d0860a85470fa450be7f0f6a8c7572756765fd", False),
    ("baei", "725accb5a8e46d19bc3f3a7636d0860a85470fa450be7f0f6a8c7572756765fd", False),
    ("aeib", "725accb5a8e46d19bc3f3a7636d0860a85470fa450be7f0f6a8c7572756765fd", False),
    ("queue", "725accb5a8e46d19bc3f3a7636d0860a85470fa450be7f0f6a8c7572756765fd", False),
    ("banana", "3ba6f1aeede102d36c0511309781ae5df4ee0f2cd43621942988fe186fb62bad", False),
    ("ae", "3ba6f1aeede102d36c0511309781ae5df4ee0f2cd43621942988fe186fb62bad", False),
    ("bcdfg", "3ba6f1aeede102d36c0511309781ae5df4ee0f2cd43621942988fe186fb62bad", False),
    ("cooee", "725accb5a8e46d19bc3f3a7636d0860a85470fa450be7f0f6a8c7572756765fd", False),
    ("aebic", "3ba6f1aeede102d36c0511309781ae5df4ee0f2cd43621942988fe186fb62bad",False),
    ("education", "3ba6f1aeede102d36c0511309781ae5df4ee0f2cd43621942988fe186fb62bad", False),
]

def hashcode(n: int) -> str:
    return hashlib.sha256(str(n).encode('utf-8')).hexdigest()

@pytest.mark.parametrize("word, result, testcase", q4_testcases)
def test_q4(word, result, testcase):
    if testcase == True:
        assert word_mood(word) == result
    else:
        assert hashcode(word_mood(word)) == result