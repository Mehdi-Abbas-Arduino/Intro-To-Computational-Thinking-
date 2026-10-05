import pytest
import hashlib
import inspect
import ast
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from q7 import *


def hashcode(value):
    return hashlib.sha256(str(value).encode("utf-8")).hexdigest()


q7_testcases = [
    # Visible Testcases
    (4, 2, 231, True),
    (1, 10, 55, True),
    (2, 6, 231, True),
    (4, 1, 1, True),

    # Hidden Testcases
    (3, 2, "6f4b6612125fb3a0daecd2799dfd6c9c299424fd920f9b308110a2c1fbd8f443", False),
    (1, 7, "59e19706d51d39f66711c2653cd7eb1291c94d9b55eb14bda74ce4dc636d015a", False),
    (2, 5, "2abaca4911e68fa9bfbf3482ee797fd5b9045b841fdff7253557c5fe15de6477", False),
    (4, 3, "3a421447cd6807ebd01e0f976ebcae5b59c8fc36e8a2f9e7b7b446b347be2937", False),
    (1, 1, "6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b", False),
    (2, 2, "e7f6c011776e8db7cd330b54174fd76f7d0216b612387a5ffcfb81e6f0919683", False),
    (3, 3, "138d9e809e386a7b800791d1f664f56d1c55f3d1ba411b950862729bc486c5ce", False),
    (2, 4, "02d20bbd7e394ad5999a4cebabac9619732c343a4cac99470c03e23ba2bdc2bc", False),
]


@pytest.mark.parametrize("boost_count, starting_score, result, testcase", q7_testcases)
def test_q7(boost_count, starting_score, result, testcase):
    actual = boost_score(boost_count, starting_score)
    if testcase:
        assert actual == result
    else:
        assert hashcode(actual) == result


def test_q7_uses_nested_iteration():
    tree = ast.parse(inspect.getsource(boost_score))
    loops = (ast.For, ast.While)

    has_nested_loop = any(
        isinstance(node, loops)
        and any(
            isinstance(child, loops)
            for child in ast.walk(node)
            if child is not node
        )
        for node in ast.walk(tree)
    )

    assert has_nested_loop, \
        "boost_score must use nested iteration."


def test_q7_does_not_use_sum_or_equivalent_shortcuts():
    source = inspect.getsource(boost_score)
    tree = ast.parse(source)

    forbidden_calls = {
        "sum",
        "pow",
        "eval",
        "exec",
        "__import__",
        "reduce",
        "accumulate",
        "comb",
        "factorial",
        "prod",
        "fsum",
    }

    forbidden_attributes = {
        "sum",
        "fsum",
        "reduce",
        "accumulate",
        "comb",
        "factorial",
        "prod",
    }

    for node in ast.walk(tree):
        if isinstance(node, (ast.ListComp, ast.SetComp, ast.DictComp, ast.GeneratorExp)):
            pytest.fail(
                "Do not use comprehensions or generator expressions as a shortcut. "
                "Perform the summation using nested iteration."
            )

        if isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name) and node.func.id in forbidden_calls:
                pytest.fail(
                    f"Do not use {node.func.id}() as a shortcut. "
                    "Perform the summation using nested iteration."
                )

            if isinstance(node.func, ast.Attribute) and node.func.attr in forbidden_attributes:
                pytest.fail(
                    f"Do not use {node.func.attr}() as a shortcut. "
                    "Perform the summation using nested iteration."
                )


def test_q7_no_direct_summation_formula():
    source = inspect.getsource(boost_score)
    tree = ast.parse(source)

    forbidden_operators = (
        ast.Mult,
        ast.Div,
        ast.FloorDiv,
        ast.Pow,
        ast.LShift,
        ast.RShift,
    )

    for node in ast.walk(tree):
        if isinstance(node, ast.BinOp) and isinstance(node.op, forbidden_operators):
            pytest.fail(
                "Do not use a direct mathematical formula or arithmetic shortcut "
                "for the summation. Perform it using nested iteration."
            )
