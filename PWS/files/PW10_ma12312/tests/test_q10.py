import ast
import hashlib
import inspect
import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
import q10


def hashcode(value):
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


q10_testcases = [
    # Visible testcases
    ('Pizza!', 'P\nPi\nPiz\nPizz\nPizza\nPizza!', True),
    ('Hi', 'H\nHi', True),
    ('A', 'A', True),
    ('', '', True),
    ("And just like that... he's gone.", "A\nAn\nAnd\nAnd \nAnd j\nAnd ju\nAnd jus\nAnd just\nAnd just \nAnd just l\nAnd just li\nAnd just lik\nAnd just like\nAnd just like \nAnd just like t\nAnd just like th\nAnd just like tha\nAnd just like that\nAnd just like that.\nAnd just like that..\nAnd just like that...\nAnd just like that... \nAnd just like that... h\nAnd just like that... he\nAnd just like that... he'\nAnd just like that... he's\nAnd just like that... he's \nAnd just like that... he's g\nAnd just like that... he's go\nAnd just like that... he's gon\nAnd just like that... he's gone\nAnd just like that... he's gone.", True),
    ('0123456789', '0\n01\n012\n0123\n01234\n012345\n0123456\n01234567\n012345678\n0123456789', True),
    ('Hi!', 'H\nHi\nHi!', True),

    # Hidden testcases
    ('aaaa', 'f8edb16532ae0101c5cce1a9b3dfb0a3def448e434c4ce0297d25503b51068f8', False),
    ('XyZ123', '3cb180996973ebf3a2c5e464db5e498ba11a4402308204472a5da5e83efd60ee', False),
    ('Hello, world', '7e45c31fc95f667fa6e6a6f632d355f76abb35b67e5b49241a8e64426134e697', False),
    ('123-456!', 'a79f56281b57aa64541f9b95a03c98c3fe6f0b6247bb26925dd6e876ed0b82c2', False),
    ('Go!', '70d11239e0be1c301f4542f1f4b5cc82e901a20e8da730018775e8cefbe7784f', False),
    (' ', '36a9e7f1c95b82ffb99743e0c5c4ce95d83c9a430aac59f84ef3cbfab6145068', False),
    ('A  B', '529735a3d0791e841cc2e312ad100328a14607e950bc92247b723dae57bca5a9', False),
    ('ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ', 'c420aa959f7e69334a31f94d462e7b85af4039d5cc033748d77f276f4c7cb27f', False),
]


def validate_structure():
    source = inspect.getsource(q10)
    module = ast.parse(source)
    functions = [node for node in ast.walk(module) if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))]
    assert len(functions) == 1 and functions[0].name == "slow_reveal", (
        "Only slow_reveal() may be defined; helper functions are not allowed."
    )
    function = functions[0]
    assert len(function.args.posonlyargs) == 0 and len(function.args.args) == 1, (
        "slow_reveal() must take exactly one parameter."
    )
    assert not function.args.kwonlyargs and function.args.vararg is None and function.args.kwarg is None, (
        "slow_reveal() must take exactly one parameter."
    )
    assert not function.args.defaults and not function.args.kw_defaults, (
        "slow_reveal() must take exactly one required parameter."
    )
    prohibited = (ast.For, ast.AsyncFor, ast.While, ast.ListComp, ast.SetComp,
                  ast.DictComp, ast.GeneratorExp, ast.Global, ast.Nonlocal)
    assert not any(isinstance(node, prohibited) for node in ast.walk(function)), (
        "Loops, comprehensions, and global variables are not allowed."
    )
    assert any(isinstance(node, ast.Call) and isinstance(node.func, ast.Name)
               and node.func.id == "slow_reveal" for node in ast.walk(function)), (
        "slow_reveal() must call itself recursively."
    )


@pytest.mark.parametrize("message, expected, visible", q10_testcases)
def test_q10(message, expected, visible, capsys):
    validate_structure()
    returned = q10.slow_reveal(message)
    actual = capsys.readouterr().out
    assert returned is None, "slow_reveal() must print and return nothing."
    # Permit one final newline, but preserve all spaces in the partial messages.
    if actual.endswith("\n"):
        actual = actual[:-1]
    if visible:
        assert actual == expected, "Incorrect sequence of printed prefixes."
    else:
        assert hashcode(actual) == expected, "Incorrect sequence of printed prefixes."
