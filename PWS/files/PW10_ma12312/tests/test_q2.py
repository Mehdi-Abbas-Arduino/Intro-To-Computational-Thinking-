import ast
import hashlib
import inspect
import os
import sys

import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import q2

q2_testcases = [
    # Visible testcases
    (2, '  *\n* *', True),
    (4, '      *\n    * *\n  * * *\n* * * *', True),
    (-5, 'Invalid input', True),
    (3000000, "Program can't handle this input", True),
    (0, '', True),
    ('Hello', 'Invalid input', True),
    (1, '*', True),
    (-2, 'Invalid input', True),
    ('four', 'Invalid input', True),
    (51, "Program can't handle this input", True),

    # Hidden testcases
    (2000000, 'e1c8e772621f1dbae0a306174a927cb65e11f8b858c5efefbaadf34e38ed288c', False),
    (50, '7a02ca41aaeeae79979ea76e715e2b4a2baaab61cb4040cccacccf10264ed83e', False),
    (7, '997d51bff9d4c5524a049880b4ffe912634c9cc9562c4a6495bcbe100658cb2b', False),
    (10, '430062f83e913f3df0d8aa61d5c688b01548e4c3fb8fe23396e470714ca4faeb', False),
    (True, 'c9bbbe8347222271664bede21651835a285b4ee792c929c6bc71557f3a29ca5b', False),
]


def hashcode(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def check_recursion_rules():
    tree = ast.parse(inspect.getsource(q2))
    pattern_defs = [node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name == "pattern"]
    assert len(pattern_defs) == 1, "Define the required pattern(number_of_rows) function."
    pattern_def = pattern_defs[0]
    arguments = pattern_def.args
    assert len(arguments.posonlyargs) + len(arguments.args) == 1 and not (
        arguments.kwonlyargs or arguments.vararg or arguments.kwarg or arguments.defaults or arguments.kw_defaults
    ), "pattern() must take one parameter."

    forbidden = (ast.Global, ast.For, ast.AsyncFor, ast.While,
                 ast.ListComp, ast.SetComp, ast.DictComp, ast.GeneratorExp)
    assert not any(isinstance(node, forbidden) for node in ast.walk(tree)), (
        "Loops, comprehensions, and global variable statements are not allowed."
    )

    helpers = [node for node in ast.walk(tree)
               if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and node is not pattern_def]
    assert helpers, "You must define a recursive helper function and call it from pattern()."

    def direct_calls(function):
        # Ignore the bodies of nested function declarations while inspecting each caller.
        pending = list(function.body)
        called = set()
        while pending:
            node = pending.pop()
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.Lambda)):
                continue
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
                called.add(node.func.id)
            pending.extend(ast.iter_child_nodes(node))
        return called

    called_from_pattern = direct_calls(pattern_def)
    assert any(
        helper.name in called_from_pattern and helper.name in direct_calls(helper)
        for helper in helpers
    ), "pattern() must call a helper function that recursively calls itself."


def normalized_output(printed, n):
    # No output is allowed for zero; otherwise, only one final newline is optional.
    if n == 0 and type(n) is int:
        assert printed == "", "pattern(0) must print nothing."
        return printed
    return printed[:-1] if printed.endswith("\n") else printed


@pytest.mark.parametrize("number_of_rows, expected, visible", q2_testcases)
def test_q2(number_of_rows, expected, visible, capsys):
    check_recursion_rules()
    result = q2.pattern(number_of_rows)
    printed = capsys.readouterr().out
    assert result is None, "pattern() must print the result and return nothing."
    actual = normalized_output(printed, number_of_rows)
    if visible:
        assert actual == expected, "Printed pattern or error message does not match the required output."
    else:
        assert hashcode(actual) == expected, "Printed pattern or error message does not match the required output."
