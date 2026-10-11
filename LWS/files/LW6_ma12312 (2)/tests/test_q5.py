import pytest
import hashlib
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from q5 import *


def hashcode(value):
    return hashlib.sha256(str(value).encode("utf-8")).hexdigest()

q5_testcases = [
    # Visible Testcases
    ('3[ha]', 'hahaha', True),
    ('2[go] team!', 'gogo team!', True),
    ('2[abc]3[cd]ef', 'abcabccdcdcdef', True),
    ('12[!] done', '!!!!!!!!!!!! done', True),
    ('3[ac]', 'acacac', True),
    ('3[a]2[bc]', 'aaabcbc', True),
    ('ab9[cd]2[ef]g', 'abcdcdcdcdcdcdcdcdcdefefg', True),
    ('2[a]2[b]cd', 'aabbcd', True),

    # Hidden Testcases
    ('1[a]', 'ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb', False),
    ('10[x]', 'fc11d6f28e59d3cc33c0b14ceb644bf0902ebd63d61218dffe9e7dac7c254542', False),
    ('50[z]', 'f85d2e4cb8d56f8c42c328712e99b45d92d1c4778cb6ffacfc570a4020c62845', False),
    ('hello', '2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824', False),
    ('2[a]3[b]', '6ea6115bab5f26516ec79af84239b082a44654ddc87c4a85af8e5b5cc1ec4a02', False),
    ('start 2[go] end', 'c6fe68762f98d878e1d0bcaae6f12cebf99ca9578cc0a53dd8af6ea271c8715f', False),
    ('3[ab]2[c]!', '7a8d49f4dc6b57c73bca42b9701b2ebd6f7b706140d314000d63413b03003573', False),
    ('1[Hello] world', '64ec88ca00b268e5ba1a35678a1b5316d212f4f366b2477232534a8aeca37f3c', False),
    ('5[ ]', '7879981d4f226a8f0191d36730c07205d7a5ff1c780fca9b2f905f25264cf636', False),
    ('2[!?]', '58817f9d77fedd664d374358acec4f8517870c85a9ba0d3a18673fce9d74e370', False),
    ('4[A]B', '0004c44dc96c76174b1b34802de9a798022572f65d52ee31a72892c31e1f834e', False),
    ('15[*]', '15ff3f8ff76d005ea19f81b38e34817ca974b43fc65bd2a55e3eec25770df503', False),
]


@pytest.mark.parametrize("encoded_message, expected, visible", q5_testcases)
def test_q5(encoded_message, expected, visible):
    if visible:
        assert expand_message(encoded_message) == expected
    else:
        assert hashcode(expand_message(encoded_message)) == expected