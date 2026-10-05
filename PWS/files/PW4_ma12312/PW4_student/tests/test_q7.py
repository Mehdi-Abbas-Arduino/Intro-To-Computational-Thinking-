import pytest
import hashlib
import inspect
import ast
import textwrap
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

import q7


q7_testcases = [
    # Visible Testcases
    (7, 11, 5, 15, 3, 2, (-2, 2, 1, 5, -6), "1 1", True),
    (8, 13, 6, 18, 4, 3, (3, -2, 2, 1, -4, -6, 2), "2 1", True),

    # Hidden Testcases
    (10, 15, 5, 20, 1, 1, (5, -5), "020a7c91e30725bb191818987340dec6040aff93923840de685e1e1d7b3d071a", False),
    (10, 15, 5, 20, 1, 1, (4, -4), "933305f987bcf5fb6c250018e35a6eee1528f06013807a4136ec13622909af97", False),
    (10, 15, 5, 20, 3, 3, (5, 10, 0, -5, -10, 0), "04412575067f0bdb6722e31a7ee45744cc1ecf2dfacec4cfbfa70cfd364bb7e2", False),
    (2, 4, 1, 5, 4, 4, (1, 2, 3, 4, -1, -2, -3, 0), "cd0cf807835179d73cad42fefc8c76827617958cf3e022ae2c8c454828e9cc38", False),
    (100, 200, 50, 250, 5, 5, (50, 100, 150, 151, -50, -50, -100, -150, -151, 0), "cd0cf807835179d73cad42fefc8c76827617958cf3e022ae2c8c454828e9cc38", False),
    (500, 600, 100, 900, 3, 3, (400, 450, 500, -300, -350, -400), "cd0cf807835179d73cad42fefc8c76827617958cf3e022ae2c8c454828e9cc38", False),
    (500, 600, 100, 900, 2, 2, (0, 399, 0, -299), "933305f987bcf5fb6c250018e35a6eee1528f06013807a4136ec13622909af97", False),
    (20, 30, 10, 40, 4, 3, (10, 11, 20, 21, -10, -11, -20), "cd0cf807835179d73cad42fefc8c76827617958cf3e022ae2c8c454828e9cc38", False),
    (20, 30, 10, 40, 2, 4, (0, 9, -9, -10, -20, -21), "545b97492c92b2df5f308b19bd5b280cb9a9bf77d2000b99791769eb724b7b6f", False),
    (20, 30, 10, 40, 4, 2, (9, 10, 20, 21, 0, -9), "1c9338eb9c4746e1c7c03aa4af28451b10f2187952635c0988479d940a05be55", False),
    (2, 3, 1, 4, 1, 1, (1, -1), "020a7c91e30725bb191818987340dec6040aff93923840de685e1e1d7b3d071a", False),
    (998, 999, 997, 1000, 2, 2, (1, 2, -1, -2), "04412575067f0bdb6722e31a7ee45744cc1ecf2dfacec4cfbfa70cfd364bb7e2", False),
    (7, 11, 5, 15, 3, 2, (2, 6, 1000, -3, -2), "1c9338eb9c4746e1c7c03aa4af28451b10f2187952635c0988479d940a05be55", False),
]

def hashcode(value):
    return hashlib.sha256(str(value).encode("utf-8")).hexdigest()

@pytest.mark.parametrize("house_start, house_end, apple_tree, orange_tree, total_apples, total_oranges, inputs, result, testcase", q7_testcases)
def test_q7(monkeypatch, capsys, house_start, house_end, apple_tree, orange_tree, total_apples, total_oranges, inputs, result, testcase):
    input_values = iter(inputs)

    monkeypatch.setattr(
        "builtins.input",
        lambda *args: str(next(input_values))
    )

    q7.fruits_in_house(
        house_start,
        house_end,
        apple_tree,
        orange_tree,
        total_apples,
        total_oranges
    )

    captured = capsys.readouterr().out.strip()

    if testcase:
        assert captured == result
    else:
        assert hashcode(captured) == result

def test_function_parameter_counts():

    assert len(inspect.signature(q7.apples_in_house).parameters) == 4, \
        "apples_in_house must take exactly 4 parameters."

    assert len(inspect.signature(q7.oranges_in_house).parameters) == 4, \
        "oranges_in_house must take exactly 4 parameters."

    assert len(inspect.signature(q7.fruits_in_house).parameters) == 6, \
        "fruits_in_house must take exactly 6 parameters."

def test_apples_in_house_input_and_return(monkeypatch, capsys):

    values = iter(["-2", "2", "1"])
    input_count = 0

    def fake_input(*args):
        nonlocal input_count
        input_count += 1
        return next(values)

    monkeypatch.setattr("builtins.input", fake_input)

    result = q7.apples_in_house(7, 11, 5, 3)

    captured = capsys.readouterr().out.strip()

    assert input_count == 3, \
        "apples_in_house must read exactly the required number of inputs."

    assert result == 1, \
        "apples_in_house must return the number of apples that land on the house."

    assert captured == "", \
        "apples_in_house must return the count, not print it."


def test_oranges_in_house_input_and_return(monkeypatch, capsys):

    values = iter(["5", "-6"])
    input_count = 0

    def fake_input(*args):
        nonlocal input_count
        input_count += 1
        return next(values)

    monkeypatch.setattr("builtins.input", fake_input)

    result = q7.oranges_in_house(7, 11, 15, 2)

    captured = capsys.readouterr().out.strip()

    assert input_count == 2, \
        "oranges_in_house must read exactly the required number of inputs."

    assert result == 1, \
        "oranges_in_house must return the number of oranges that land on the house."

    assert captured == "", \
        "oranges_in_house must return the count, not print it."

def contains_input_call(function):

    source = textwrap.dedent(inspect.getsource(function))
    tree = ast.parse(source)

    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name) and node.func.id == "input":
                return True

    return False

def test_input_location():

    assert contains_input_call(q7.apples_in_house), \
        "apples_in_house must read the apple inputs."

    assert contains_input_call(q7.oranges_in_house), \
        "oranges_in_house must read the orange inputs."

    assert not contains_input_call(q7.fruits_in_house), \
        "fruits_in_house must not read fruit inputs directly."

def test_fruits_in_house_calls_helpers_and_prints(monkeypatch, capsys):

    calls = []

    def fake_apples(*args):
        calls.append(("apples", args))
        return 2

    def fake_oranges(*args):
        calls.append(("oranges", args))
        return 3

    def fail_input(*args):
        pytest.fail("fruits_in_house must not call input() directly.")

    monkeypatch.setattr(q7, "apples_in_house", fake_apples)
    monkeypatch.setattr(q7, "oranges_in_house", fake_oranges)
    monkeypatch.setattr("builtins.input", fail_input)

    result = q7.fruits_in_house(7, 11, 5, 15, 4, 6)

    captured = capsys.readouterr().out.strip()

    assert calls == [
        ("apples", (7, 11, 5, 4)),
        ("oranges", (7, 11, 15, 6))
    ], "fruits_in_house must call both required helper functions with the correct arguments."

    assert captured == "2 3", \
        "fruits_in_house must print the apple count followed by the orange count."

    assert result is None, \
        "fruits_in_house must print the result rather than return it."