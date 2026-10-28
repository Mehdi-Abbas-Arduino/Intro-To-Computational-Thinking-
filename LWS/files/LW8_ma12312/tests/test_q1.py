import pytest
import hashlib
import inspect
import ast
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from q1 import *


def hashcode(value):
    return hashlib.sha256(str(value).encode("utf-8")).hexdigest()


q1_testcases = [
    (3, ['5', '10', '15'], [5, 10, 15], True),
    (4, ['10', '20', '30', '40'], 'c502dfa70190f0c45a36e4ecd63dea5ed73ecdee6fc7c73f0b2cf9b23887412b', False),
    (1, ['99'], 'c6dcb442b19ede93608de74770c730e6d19be562f3b0ac9802c27bebf7e5d848', False),
    (0, [], '4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945', False),
    (5, ['7', '14', '21', '28', '35'], '781214598082244e3946c27da2c14b7852e32cefdc17562dbff578d80bf1dd7a', False),
    (6, ['0', '1', '2', '3', '4', '5'], 'b0229c06acf4d5c98db175d4d054cd39e7fff51d8c37754b4a4b424f7967710d', False),
    (3, ['-1', '-2', '-3'], 'e0e675d19b01ccfd79c09ee861ed05f9c87eb49b7901df017df65bef901e639b', False),
    (4, ['1000', '2000', '3000', '4000'], '7d7b96d7721be63e07748c3f94cc16139a630d8eb2137aa1907ba50a8e9655e0', False),
    (2, ['42', '0'], 'f3c3226373700c2d4f8fe2d7da520c0fc94bb990246cb226e35eccf639f9a5b7', False),
    (1, ['-50'], 'ea67e7696befa16713a1b6098da451ff708dd4711e42aa771513060f960caa58', False),
    (3, ['0', '-10', '25'], 'f5adda967b0cecb85f0b67cf1109597cce3f6757531cf5c35b3a5276899b90f2', False),
    (5, ['8', '8', '8', '8', '8'], 'c6d988dc9e65095f7f6f9b0669863b95b89345ebe763142f0e10497199b79d6f', False),
    (4, ['-1000', '5000', '-250', '75'], 'c27ebe64a1f86f53db21236ea50ade3d11c1fea811be25c5565b1741deb68cfb', False),
    (2, ['123456', '-123456'], '678798f0f3615b65005048fb96a981cd006232cfcfa55acd94717dcd3156c0a5', False),
]


@pytest.mark.parametrize("count, inputs, expected, visible", q1_testcases)
def test_q1(monkeypatch, count, inputs, expected, visible):
    input_lines = inputs.copy()

    def mock_input(prompt=""):
        if input_lines:
            return input_lines.pop(0)
        raise IndexError("No more input available")

    monkeypatch.setattr("builtins.input", mock_input)

    output = read_integer_list(count)

    if visible:
        assert output == expected
    else:
        assert hashcode(output) == expected


def test_q1_uses_iteration():
    tree = ast.parse(inspect.getsource(read_integer_list))
    assert any(isinstance(node, (ast.For, ast.While)) for node in ast.walk(tree))