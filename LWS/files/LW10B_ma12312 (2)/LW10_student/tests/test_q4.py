import ast
import hashlib
import inspect
import os
import sys

import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import q4


CASES = [
    (1, '#', '#', True),
    (2, '*', ' *\n**', True),
    (4, '$', '   $\n  $$\n $$$\n$$$$', True),
    (7, '@', '      @\n     @@\n    @@@\n   @@@@\n  @@@@@\n @@@@@@\n@@@@@@@', True),
    (5, '+', '    +\n   ++\n  +++\n ++++\n+++++', True),
    (3, '?', '34cc3944287896c95ac7fd01e453af1384e9c88d7a7e83b755d8e344daa62e0f', False),
    (6, '*', '973118568ff10dd21843a3d1768f6eb540e4f1ac5950c34bb1bc7c5fdb3a2d74', False),
    (8, '0', '4c93519c13d5f2eeceb98b6af2c06c8a27063ac0ce6a7013e01d94913473e63a', False),
    (10, '*', '7c4b75cd2253012ae6cb8fb88c22fd67ed826c871dc2bcf2e6a1211feb7cec60', False),
    (12, '%', '5bfaa60b96a3eed8e917f55f8301352531b76c200329cda3e18f7bf803ae05d7', False),
    (15, '*', '966e06000ccdca616d0193af609e63037584ebd977bb237b58e23279da312f34', False),
    (19, '&', '8295974a32f50d36f457490b9e8b3382390aaa3392a853352dd3648605d48ba8', False),
    (28, '+', '33b4314421db56ff41f09e139bcd25deedddc9c8901db52e5b518a98b6d3f951', False),
    (37, 'X', 'bbf3e9516e91459130c1831966c0b196c1e40d60763d5bf77a999363caeca303', False),
    (50, 'z', '4ee959ecebb47819bc48a04a4b916987f7002231c03680afabce50972e524bf3', False),
]


def direct_calls(function):
    """Read calls in this function's body, excluding nested function bodies."""
    class Calls(ast.NodeVisitor):
        def __init__(self):
            self.names = set()

        def visit_FunctionDef(self, node):
            pass

        def visit_AsyncFunctionDef(self, node):
            pass

        def visit_Call(self, node):
            if isinstance(node.func, ast.Name):
                self.names.add(node.func.id)
            self.generic_visit(node)

    visitor = Calls()
    for statement in function.body:
        visitor.visit(statement)
    return visitor.names


def check_constraints():
    tree = ast.parse(inspect.getsource(q4))
    functions = [
        node for node in ast.walk(tree)
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
    ]
    entries = [node for node in functions if node.name == "print_staircase"]
    assert len(entries) == 1, "Define print_staircase() exactly once."
    main = entries[0]
    assert [arg.arg for arg in main.args.args] == ["step_count", "symbol"], (
        "print_staircase() must take step_count and symbol as parameters."
    )
    assert not (
        main.args.defaults or main.args.kw_defaults or
        main.args.vararg or main.args.kwarg or
        main.args.kwonlyargs or main.args.posonlyargs
    ), "print_staircase() must accept exactly two ordinary parameters."

    forbidden = (
        ast.For, ast.AsyncFor, ast.While,
        ast.ListComp, ast.SetComp, ast.DictComp, ast.GeneratorExp,
        ast.Global, ast.Nonlocal,
    )
    assert not any(isinstance(node, forbidden) for node in ast.walk(tree)), (
        "Use recursion without loops, comprehensions, or global variables."
    )

    helpers = [node for node in functions if node.name != "print_staircase"]
    assert helpers, "Define a recursive helper function and call it from print_staircase()."
    entry_calls = direct_calls(main)
    assert any(helper.name in entry_calls and helper.name in direct_calls(helper)
               for helper in helpers), (
        "print_staircase() must call a recursive helper function. "
        "The helper may have any name or parameters."
    )


@pytest.mark.parametrize(
    "step_count, symbol, expected, visible",
    CASES,
    ids=[f"{'visible' if case[3] else 'hidden'}-{i:02d}" for i, case in enumerate(CASES, 1)],
)
def test_q4(capsys, step_count, symbol, expected, visible):
    check_constraints()
    result = q4.print_staircase(step_count, symbol)
    assert result is None, "print_staircase() must print rather than return the staircase."

    output = capsys.readouterr().out
    if output.endswith("\n"):
        output = output[:-1]
    assert "\r" not in output, "Use a separate line for each staircase row."
    # Compare EXACT output, including leading spaces and absence of trailing spaces.
    if visible:
        assert output == expected, f"Expected {expected!r}; printed {output!r}."
    else:
        digest = hashlib.sha256(output.encode("utf-8")).hexdigest()
        assert digest == expected, "Incorrect staircase output for this hidden case."
