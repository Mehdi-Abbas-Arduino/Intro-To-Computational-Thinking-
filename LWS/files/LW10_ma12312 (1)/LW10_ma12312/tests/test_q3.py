import ast
import hashlib
import inspect
import os
import sys

import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import q3


CASES = [
    ('banana', 'na', 2, True),
    ('ban', 'na', -1, True),
    ('banana', 'ban', 0, True),
    ('aaaa', 'aa', 0, True),
    ('', 'a', -1, True),
    ('banana', 'no', '1bad6b8cf97131fceab8543e81f7757195fbb1d36b376ee994ad1cf17699c464', False),
    ('banana', 'a', '6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b', False),
    ('post operation', 'st op', 'd4735e3a265e16eee03f59718b9b5d03019c07d8b6c51f90da3a666eec13ab35', False),
    ('hello world', 'xorld', '1bad6b8cf97131fceab8543e81f7757195fbb1d36b376ee994ad1cf17699c464', False),
    ('banana', 'banana', '5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9', False),
    ('banana', 'nana', 'd4735e3a265e16eee03f59718b9b5d03019c07d8b6c51f90da3a666eec13ab35', False),
    ('ban', 'banana', '1bad6b8cf97131fceab8543e81f7757195fbb1d36b376ee994ad1cf17699c464', False),
    ('BaNaNa', 'na', '1bad6b8cf97131fceab8543e81f7757195fbb1d36b376ee994ad1cf17699c464', False),
    ('post operation', 'ration', '2c624232cdd221771294dfbb310aca000a0df6ac8b66b696d90ef06fdefb64a3', False),
    ('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxend', 'end', 'dcb5d6e69e4ded78464ae2843f509daf65c9ca09dfdc9b5ad69166341963a877', False),
]


FORBIDDEN_METHODS = {
    "find", "rfind", "index", "rindex", "count", "startswith", "endswith",
    "replace", "split", "rsplit", "partition", "rpartition", "strip",
    "lstrip", "rstrip", "lower", "upper", "casefold", "removeprefix",
    "removesuffix",
}
FORBIDDEN_NODES = (
    ast.For, ast.AsyncFor, ast.While,
    ast.ListComp, ast.SetComp, ast.DictComp, ast.GeneratorExp,
    ast.In, ast.NotIn,
)


def direct_calls(function):
    """Collect calls from a function body, excluding bodies of nested helpers."""
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
    tree = ast.parse(inspect.getsource(q3))
    functions = [
        node for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)
    ]
    entries = [node for node in functions if node.name == "my_find"]
    assert len(entries) == 1, "Define my_find(notes, keyword) exactly once."
    entry = entries[0]
    assert [arg.arg for arg in entry.args.args] == ["notes", "keyword"], (
        "my_find() must have parameters notes and keyword."
    )
    assert not (entry.args.defaults or entry.args.kw_defaults or
                entry.args.vararg or entry.args.kwarg or
                entry.args.kwonlyargs or entry.args.posonlyargs), (
        "my_find() must take exactly the two required parameters."
    )

    for node in ast.walk(tree):
        assert not isinstance(node, FORBIDDEN_NODES + (ast.Global, ast.Nonlocal)), (
            "Use recursion: loops, comprehensions, global variables and 'in' are forbidden."
        )
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
            assert node.func.attr not in FORBIDDEN_METHODS, (
                "String searching or string-processing methods are not allowed."
            )
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            module = (node.module or "") if isinstance(node, ast.ImportFrom) else ""
            imports = [module] if isinstance(node, ast.ImportFrom) else [a.name for a in node.names]
            assert all(item.split(".")[0] not in {"re", "regex"} for item in imports), (
                "Regular-expression searching is not allowed."
            )

    helpers = [fn for fn in functions if fn.name != "my_find"]
    assert helpers, "Define a recursive helper called by my_find()."
    entry_calls = direct_calls(entry)
    assert any(helper.name in entry_calls and helper.name in direct_calls(helper)
               for helper in helpers), (
        "my_find() must call a recursive helper; any valid helper name is allowed."
    )


@pytest.mark.parametrize(
    "notes, keyword, expected, visible",
    CASES,
    ids=[f"{'visible' if c[3] else 'hidden'}-{i:02d}" for i, c in enumerate(CASES, 1)],
)
def test_q3(capsys, notes, keyword, expected, visible):
    check_constraints()
    returned = q3.my_find(notes, keyword)
    assert returned is None, "my_find() must print the index, not return it."

    printed = capsys.readouterr().out
    if printed.endswith("\n"):
        printed = printed[:-1]
    assert "\n" not in printed and "\r" not in printed, (
        "Print just one integer on one line."
    )

    if visible:
        assert printed == str(expected), (
            f"Expected {expected!r}, but printed {printed!r}."
        )
    else:
        digest = hashlib.sha256(printed.encode("utf-8")).hexdigest()
        assert digest == expected, "Incorrect first-occurrence index for this hidden case."
