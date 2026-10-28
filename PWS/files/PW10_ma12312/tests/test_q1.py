import ast
import hashlib
import inspect
import textwrap

import os
import sys

import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import q1


q1_testcases = [
    # Visible testcases
    (1, '1', True),
    (5, '5\n16\n8\n4\n2\n1', True),
    (52, '52\n26\n13\n40\n20\n10\n5\n16\n8\n4\n2\n1', True),
    (7, '7\n22\n11\n34\n17\n52\n26\n13\n40\n20\n10\n5\n16\n8\n4\n2\n1', True),
    (12, '12\n6\n3\n10\n5\n16\n8\n4\n2\n1', True),
    (63, '63\n190\n95\n286\n143\n430\n215\n646\n323\n970\n485\n1456\n728\n364\n182\n91\n274\n137\n412\n206\n103\n310\n155\n466\n233\n700\n350\n175\n526\n263\n790\n395\n1186\n593\n1780\n890\n445\n1336\n668\n334\n167\n502\n251\n754\n377\n1132\n566\n283\n850\n425\n1276\n638\n319\n958\n479\n1438\n719\n2158\n1079\n3238\n1619\n4858\n2429\n7288\n3644\n1822\n911\n2734\n1367\n4102\n2051\n6154\n3077\n9232\n4616\n2308\n1154\n577\n1732\n866\n433\n1300\n650\n325\n976\n488\n244\n122\n61\n184\n92\n46\n23\n70\n35\n106\n53\n160\n80\n40\n20\n10\n5\n16\n8\n4\n2\n1', True),

    # Hidden testcases
    (102, '5dbc1d95a8166750dc234dbdcc2e18bb7e2a988f61ef76867c3a2af25e56caf3', False),
    (97, 'b7aebdc13b8eaee0d6aeaed9e848b4aee4ae874f8ffd08017ba897e6f7e5a3a1', False),
    (258, '5fa82d2119a6dfd49204cf8e86fe293f9dd6856489500d068c90e607b79b12ea', False),
    (905, '1b45bc9a44b5acb3d837fedd1946944ce9193749a1b5301bbd76d81e6c0f6d6d', False),
    (2, '56d4275def58246bd5d0cc057d91b21648992ecee6fc1947058fba34683a7c3b', False),
    (3, '3bef7ac90f912426ac080085a49f49a5406f55a87724fba463fb9977a5028211', False),
    (6, '864e37ddbdbd920fe1cc99339c3cf4308ee279c5070368870f8fe1664eef6ef0', False),
    (27, '9d91800b918f4b42fa0a573df9438c3dcddd311fca72c319f5bcdf75bf5f17ba', False),
    (1000, '5e1b10032614ebc871deea919ef96fdfbd8180d5e6caa49c5c82475471e80ee7', False),
]


def hashcode(value):
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def normalize_output(output):
    # A final newline is optional; trailing spaces on lines are ignored.
    output = output.replace("\r\n", "\n")
    if output.endswith("\n"):
        output = output[:-1]
    return "\n".join(line.rstrip(" \t") for line in output.split("\n"))


def verify_recursion_rules():
    # Inspect the student's function only, not the visible demonstration code.
    source = inspect.getsource(q1.verify_collatz)
    tree = ast.parse(textwrap.dedent(source))
    function = tree.body[0]

    signature = inspect.signature(q1.verify_collatz)
    parameters = list(signature.parameters.values())
    assert len(parameters) == 1 and parameters[0].kind in (
        inspect.Parameter.POSITIONAL_ONLY,
        inspect.Parameter.POSITIONAL_OR_KEYWORD,
    ), "verify_collatz() must accept exactly one positional parameter."
    assert parameters[0].default is inspect.Parameter.empty, (
        "The single parameter should not have a default value."
    )

    prohibited = (
        ast.Global, ast.Nonlocal, ast.For, ast.AsyncFor, ast.While,
        ast.ListComp, ast.SetComp, ast.DictComp, ast.GeneratorExp,
        ast.Lambda, ast.AsyncFunctionDef,
    )
    assert not any(isinstance(node, prohibited) for node in ast.walk(function)), (
        "Use direct recursion without loops, comprehensions, globals, or helper functions."
    )
    assert not any(
        isinstance(node, ast.FunctionDef) and node is not function
        for node in ast.walk(function)
    ), "Helper functions are not allowed."

    # No extra user-defined top-level functions in q1.py.
    assert not any(
        isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
        and node.name != "verify_collatz"
        for node in ast.parse(inspect.getsource(q1)).body
    ), "Helper functions are not allowed."

    assert any(
        isinstance(node, ast.Call)
        and isinstance(node.func, ast.Name)
        and node.func.id == "verify_collatz"
        for node in ast.walk(function)
    ), "verify_collatz() must call itself recursively."


@pytest.mark.parametrize("starting_number, expected, visible", q1_testcases)
def test_q1(starting_number, expected, visible, capsys):
    verify_recursion_rules()
    result = q1.verify_collatz(starting_number)
    actual = normalize_output(capsys.readouterr().out)

    assert result is None, "verify_collatz() must print the sequence and return nothing."
    if visible:
        assert actual == expected, (
            f"Incorrect Collatz sequence for {starting_number}."
        )
    else:
        assert hashcode(actual) == expected, (
            f"Incorrect Collatz sequence for hidden input {starting_number}."
        )
