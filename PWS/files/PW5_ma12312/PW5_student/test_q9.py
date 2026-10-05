import pytest
import hashlib
import inspect
import ast
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

import q9


def hashcode(value):
    return hashlib.sha256(str(value).encode("utf-8")).hexdigest()


def _has_nested_iteration(function):
    tree = ast.parse(inspect.getsource(function))
    loops = (ast.For, ast.While)
    return any(
        isinstance(node, loops)
        and any(
            isinstance(child, loops)
            for child in ast.walk(node)
            if child is not node
        )
        for node in ast.walk(tree)
    )


def normalize_output(output):
    return output.rstrip()


q9_testcases = [
    (1, 10, '2, 3, 5, 7', True),
    (3, 5, '3, 5', True),
    (20, 30, '23, 29', True),
    (14, 16, '', True),
    (0, 2, 'd4735e3a265e16eee03f59718b9b5d03019c07d8b6c51f90da3a666eec13ab35', False),
    (0, 1, 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855', False),
    (2, 2, 'd4735e3a265e16eee03f59718b9b5d03019c07d8b6c51f90da3a666eec13ab35', False),
    (90, 110, '408c83c37272b83a0d1eea05f579cc06c4ce86815f5b198b4befad8f90aff0ac', False),
    (100, 150, '5ddc6665c3d9f0005244c353b3a394f965c45a9ce68dc42377df6f96a6e69b4d', False),
    (997, 1030, 'e04826c1d4ee76d7db37963788877879b2357e1bdd3c6a022c82abaf4aa0ceb6', False),
    (500, 550, '467efe7ece1aa68f3cb65ae57e9d09c74a4ee58613dfb479e85da1d5f525df53', False),
    (1000, 1060, '6cdd015f071721bfb01a8269245410a521d2bdda81dfc6aaf72a7b13cb1b6b48', False),
    (10000, 10100, '7f65b7240e0c947f56f719d9de547f5579f7d49f87fba767d71f550392700864', False),
    (99900, 100000, '8b986fc4ffff39a3baf4080f14caef23834aef31e44bcb829f68a2c3459a92ab', False),
    (50, 50, 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855', False),
]


@pytest.mark.parametrize("start_id, end_id, result, visible", q9_testcases)
def test_q9(capsys, start_id, end_id, result, visible):
    q9.print_prime_ids(start_id, end_id)
    actual = normalize_output(capsys.readouterr().out)
    if visible:
        assert actual == result
    else:
        assert hashcode(actual) == result


def test_q9_uses_nested_iteration():
    assert _has_nested_iteration(q9.print_prime_ids), \
        "print_prime_ids must use nested iteration."


def test_q9_no_prime_library_shortcuts():
    tree = ast.parse(inspect.getsource(q9))
    forbidden = {"isprime", "primerange", "primes", "nextprime", "prevprime"}
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name) and node.func.id.lower() in forbidden:
                pytest.fail("Do not use a library function that directly determines or generates prime numbers.")
            if isinstance(node.func, ast.Attribute) and node.func.attr.lower() in forbidden:
                pytest.fail("Do not use a library function that directly determines or generates prime numbers.")
