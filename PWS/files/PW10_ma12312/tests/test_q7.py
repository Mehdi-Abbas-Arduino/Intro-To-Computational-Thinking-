import ast
import hashlib
import inspect
import os
import sys

import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import q7


q7_testcases = [
    # Visible testcases
    (2, '* *\n *', True),
    (4, '* * * *\n * * *\n  * *\n   *', True),
    (7, '* * * * * * *\n * * * * * *\n  * * * * *\n   * * * *\n    * * *\n     * *\n      *', True),
    (10, '* * * * * * * * * *\n * * * * * * * * *\n  * * * * * * * *\n   * * * * * * *\n    * * * * * *\n     * * * * *\n      * * * *\n       * * *\n        * *\n         *', True),
    (15, '* * * * * * * * * * * * * * *\n * * * * * * * * * * * * * *\n  * * * * * * * * * * * * *\n   * * * * * * * * * * * *\n    * * * * * * * * * * *\n     * * * * * * * * * *\n      * * * * * * * * *\n       * * * * * * * *\n        * * * * * * *\n         * * * * * *\n          * * * * *\n           * * * *\n            * * *\n             * *\n              *', True),
    (1, '*', True),

    # Hidden testcases
    (6, '224696da5e0d3c57527108e4a9976749e8646c6c23620fe5f17ab1d18646d9d4', False),
    (12, '8dc939df18550b7bfe4f00acfe7fa1aa78359c7efe863d29ef9a8600409d1a70', False),
    (19, '3eef5fec2afd4b68fbdcbb9ad0f8c330d7cf9260f96fc7e85bab3fa8d63bad69', False),
    (28, '8538451c5c08bb7f1debd21f86d8e013c0d1a52c7e6fb2be80fa4ec91920ef8c', False),
    (3, 'ef80c52b544900b0c22c4bc97cf2cd2510c9496b594aec3c404b6b18c2dd3580', False),
    (8, 'b0395ce82df85a2e35fa97b4a5c34effb573e59b31876c664a10238dc56c49e1', False),
    (25, '2553c6c92429ef7ffaaa603da2027bae78a8df1319d3fc1cd414929c946ec8d3', False),
    (31, '394c641d9938c313343cb1a391af3e0fd18e0cf65fbc983c5deddae0e727542b', False),
    (50, '42b47383117ffe4f3dd7afd658eb2ec1fffc4141eaa60282521260df08881903', False),
]


def hashcode(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def check_recursion_rules():
    tree = ast.parse(inspect.getsource(q7))
    defined = [node for node in ast.walk(tree) if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))]
    cup_defs = [node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name == "cup"]
    assert len(cup_defs) == 1, "Define the required cup(n) function."
    cup_function = cup_defs[0]
    assert len(cup_function.args.posonlyargs) + len(cup_function.args.args) == 1, (
        "cup() must accept one parameter."
    )
    assert not cup_function.args.defaults and not cup_function.args.kwonlyargs and not cup_function.args.vararg and not cup_function.args.kwarg, (
        "cup() must accept just its required argument."
    )
    forbidden = (ast.Global, ast.For, ast.AsyncFor, ast.While,
                 ast.ListComp, ast.SetComp, ast.DictComp, ast.GeneratorExp)
    assert not any(isinstance(node, forbidden) for node in ast.walk(tree)), (
        "Loops, comprehensions, and global variables are not allowed."
    )
    # A recursive helper function is mandatory. Its name and placement are unrestricted.
    helpers = [function for function in defined if function is not cup_function]
    assert helpers, "You must define a recursive helper function and call it from cup()."

    def direct_calls(function):
        # Ignore bodies of nested functions when identifying the caller.
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

    called_from_cup = direct_calls(cup_function)
    assert any(
        helper.name in called_from_cup and helper.name in direct_calls(helper)
        for helper in helpers
    ), "cup() must call a helper function that recursively calls itself."


def normalized_pattern(printed):
    # Retain all leading spaces, but permit trailing spaces at the ends of rows.
    # A final newline is fine; extra blank lines are not.
    return "\n".join(row.rstrip(" ") for row in printed.splitlines())


@pytest.mark.parametrize("n, expected, visible", q7_testcases)
def test_q7(n, expected, visible, capsys):
    check_recursion_rules()
    result = q7.cup(n)
    printed = capsys.readouterr().out
    assert result is None, "cup() must print the pattern and return nothing."
    actual = normalized_pattern(printed)
    if visible:
        assert actual == expected, "Printed asterisks or leading spaces do not match the expected pattern."
    else:
        assert hashcode(actual) == expected, "Printed asterisks or leading spaces do not match the expected pattern."
