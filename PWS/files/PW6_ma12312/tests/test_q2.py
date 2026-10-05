import pytest
import hashlib
import ast
import inspect
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from q2 import decode_message

def hashcode(value):
    return hashlib.sha256(str(value).encode("utf-8")).hexdigest()

q2_testcases = [
    # Visible Testcases
    ('2qc2a3zt', 'cat', True),
    ('xgo11', 'go', True),
    ('H0zi3', 'Hi', True),
    ('1a2 2b', 'a b', True),
    ('habib', '', True),
    
    # Hidden Testcases
    ('0', '5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9', False),
    ('1a', 'ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb', False),
    ('1a1b', 'f55ff16f66f43360266b95db6f8fec01d76031054306ae4a4b380598f6cfd114', False),
    ('3abX0', 'ecc76c19c9f3c5108773d6c3a18a6c25c9bf1131c4e250b71213274e3b2b5d08', False),
    ('abc', 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855', False),
    ('2Xy1z', '03e0769b10886aef0ff2170851dd67d41755c87037c4319d9901e7fdf518c485', False),
    ('4abcZ0', '099987a5188a32ab07b68b4219a824bb83bfcc10aca0fd4f58e41c99b37f09f9', False),
    ('1 1a', 'e12a7e051731cf1dbeefa2142a8e1abb1eb5898e2cbe4aa522120829a5588dc7', False),
    ('9abcdefghZ', 'bbeebd879e1dff6918546dc0c179fdde505f2a21591c9a9c96e36b054ec5af83', False),
    ('2a3bcdef', 'da0568a25209c76552026c3b87ac374acd8e8aeafc061e04ac55fac18c45cb2d', False),
    ('1A2BC3DEF', '69f0fb8cb1d2195340160eb0e4fcf019b4500be11e00fc55f5d3d108b4914d44', False),
    ('2--2++2**', '5577006f5924569e28577741a83d6e91d26611ceca7244e869e96773e294e990', False),
    ('0hello', '5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9', False),
    ('3xy!2ab', '0266b93cf3014995a269f322cc0dee93b5fa794a67e1105486f31b49575515dc', False),
    ('1x0y0z', 'cd2eb0837c9b4c962c22d2ff8b5441b7b45805887f051d39bf133b583baf6860', False)
]

@pytest.mark.parametrize("encoded_text, expected, visible", q2_testcases)
def test_q2(encoded_text, expected, visible):
    if visible:
        assert decode_message(encoded_text) == expected
    else:
        assert hashcode(decode_message(encoded_text)) == expected