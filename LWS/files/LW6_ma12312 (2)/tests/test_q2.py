import pytest
import hashlib
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from q2 import *


def hashcode(value):
    return hashlib.sha256(str(value).encode("utf-8")).hexdigest()


q2_testcases = [
    # Visible Testcases
    ('campus', 3, 'puscam', True),
    ('campus', -2, 'uscamp', True),
    ('campus', 8, 'mpusca', True),
    ('campus', -8, 'uscamp', True),

    # Hidden Testcases
    ('campus', 0, '42c97db3df4b1373d9484116af081d539c72309ff2adf6f20cd55c7951a355d3', False),
    ('a', 5, 'ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb', False),
    ('a', -7, 'ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb', False),
    ('abcd', 1, '7140cce4f5d226132b03b2942f5d0478e1823dc4f69d1eb30b03f1e195b5bb9c', False),
    ('abcd', -1, '6acd1f8103640d664877973644ead274c5ba63154d6120a08e43b28d3f4b6fbb', False),
    ('abcd', 4, '88d4266fd4e6338d13b845fcf289579d209c897823b9217da3e161936f031589', False),
    ('abcd', -4, '88d4266fd4e6338d13b845fcf289579d209c897823b9217da3e161936f031589', False),
    ('abcd', 5, '7140cce4f5d226132b03b2942f5d0478e1823dc4f69d1eb30b03f1e195b5bb9c', False),
    ('abcd', -5, '6acd1f8103640d664877973644ead274c5ba63154d6120a08e43b28d3f4b6fbb', False),
    ('hello world', 6, 'd4ca63deecc2672c9e2882f4eeecc61af879fc6c2a6cb3828f0e98062949a22f', False),
    ('12345', 12, '4ae23032dc1e60655f4884d40726aa9efd6099c7d84d4513490d5f3f9ffe2506', False),
    ('12345', -12, '374253898c08575e81c80e4858729c4615d4bd5a18c68e9c17cc4618deb4d7c6', False),
    ('A B C', 2, '6566e668ba08df8227f5f0afa0960a100901e8e3f18dd53568328d0f7c120210', False),
    ('!@#$%', 3, 'b91c19a485bc1e6ddb43d3d3d85dd8c4ac8fa48f89116f9e9272b92306488b44', False),
    ('rotation', 100, '57615eca3cdb2d2aa79530d1f390489476a35792a50537b895d241424821f327', False),
    ('rotation', -100, '57615eca3cdb2d2aa79530d1f390489476a35792a50537b895d241424821f327', False),
]


@pytest.mark.parametrize("display_message, rotation_count, expected, visible", q2_testcases)
def test_q2(display_message, rotation_count, expected, visible):
    if visible:
        assert rotate_message(display_message, rotation_count) == expected
    else:
        assert hashcode(rotate_message(display_message, rotation_count)) == expected