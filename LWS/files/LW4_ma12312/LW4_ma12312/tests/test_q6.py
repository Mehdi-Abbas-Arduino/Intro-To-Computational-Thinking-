import pytest
import hashlib
import ast
import inspect
import textwrap
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

import q6


q6_testcases = [
    # Visible Testcases
    (3, 6, [3, 4, 4, 5, 5, 7, 5, 2, 5], "12", True),
    (2, 6, [3, 6, 8, 5, 4, 9], "No Board", True),
    (2, 8, [3, 8, 8, 5, 5, 6], "25", True),
    (3, 15, [2, 6, 16, 3, 6, 19, 5, 4, 33], "No Board", True),

    # Hidden Testcases
    (1, 10, [7, 8, 10], "7688b6ef52555962d008fff894223582c484517cea7da49ee67800adc7fc8866", False),
    (1, 10, [7, 8, 11], "ce42713fba1007256bfb7a334a0e762e6b0bef6edc378f70fd3de94e6a4eebcc", False),
    (4, 100, [10, 10, 100, 9, 12, 99, 20, 3, 50, 6, 18, 70], "9537f32ec7599e1ae953af6c9f929fe747ff9dadf79a9beff1f304c550173011", False),
    (4, 20, [2, 30, 20, 10, 5, 19, 8, 8, 21, 7, 7, 5], "39fa9ec190eee7b6f4dff1100d6343e10918d044c75eac8f9e9a2596173f80c9", False),
    (3, 50, [100, 100, 51, 2, 40, 50, 9, 9, 49], "5316ca1c5ddca8e6ceccfce58f3b8540e540ee22f6180fb89492904051b3d531", False),
    (2, 1, [100, 100, 1, 99, 99, 1], "39e5b4830d4d9c14db7368a95b65d5463ea3d09520373723430c03a5a453b5df", False),
    (4, 60, [5, 5, 10, 6, 6, 20, 7, 7, 30, 8, 8, 60], "a68b412c4282555f15546cf6e1fc42893b7e07f271557ceb021821098dd66c1b", False),
    (3, 30, [10, 4, 30, 8, 5, 30, 6, 7, 31], "d59eced1ded07f84c145592f65bdf854358e009c5cd705f5215bf18697fed103", False),
    (2, 100, [100, 100, 100, 99, 100, 99], "39e5b4830d4d9c14db7368a95b65d5463ea3d09520373723430c03a5a453b5df", False),
    (4, 15, [1, 1, 15, 2, 2, 14, 3, 3, 16, 4, 4, 13], "b17ef6d19c7a5b1ee83b907c595526dcb1eb06db8227d650d5dda0a9f4ce8cd9", False),
    (3, 25, [9, 9, 24, 10, 8, 25, 100, 1, 26], "5316ca1c5ddca8e6ceccfce58f3b8540e540ee22f6180fb89492904051b3d531", False)
]


def hashcode(n) -> str:
    return hashlib.sha256(str(n).encode("utf-8")).hexdigest()


@pytest.mark.parametrize(
    "board_count, weight_limit, inputs, result, testcase",
    q6_testcases
)
def test_q6(
    monkeypatch,
    capsys,
    board_count,
    weight_limit,
    inputs,
    result,
    testcase
):
    user_inputs = iter(inputs)

    monkeypatch.setattr(
        "builtins.input",
        lambda *args: str(next(user_inputs))
    )

    q6.best_choice(board_count, weight_limit)

    captured, err = capsys.readouterr()
    captured = captured.strip()

    if testcase:
        assert captured == result
    else:
        assert hashcode(captured) == result


def test_area_calculator_exists():
    assert hasattr(q6, "area_calculator"), (
        "You must define the required area_calculator() helper function."
    )


def test_area_calculator_parameters():
    assert hasattr(q6, "area_calculator"), (
        "You must define the required area_calculator() helper function."
    )

    signature = inspect.signature(q6.area_calculator)
    parameters = list(signature.parameters.values())

    assert len(parameters) == 2, (
        "area_calculator() must take exactly two parameters."
    )


def test_area_calculator_result():
    assert hasattr(q6, "area_calculator"), (
        "You must define the required area_calculator() helper function."
    )

    assert q6.area_calculator(3, 4) == 12
    assert q6.area_calculator(5, 5) == 25
    assert q6.area_calculator(10, 2) == 20


def test_area_calculator_does_not_read_input():
    assert hasattr(q6, "area_calculator"), (
        "You must define the required area_calculator() helper function."
    )

    source = inspect.getsource(q6.area_calculator)
    source = textwrap.dedent(source)
    tree = ast.parse(source)

    for node in ast.walk(tree):
        if (
            isinstance(node, ast.Call)
            and isinstance(node.func, ast.Name)
            and node.func.id == "input"
        ):
            pytest.fail(
                "area_calculator() must use its two parameters "
                "and must not read input."
            )


def test_best_choice_reads_input():
    source = inspect.getsource(q6.best_choice)
    source = textwrap.dedent(source)
    tree = ast.parse(source)

    input_calls = []

    for node in ast.walk(tree):
        if (
            isinstance(node, ast.Call)
            and isinstance(node.func, ast.Name)
            and node.func.id == "input"
        ):
            input_calls.append(node)

    assert len(input_calls) > 0, (
        "Board information must be read inside best_choice() "
        "using input()."
    )


def test_best_choice_reads_exact_inputs(monkeypatch, capsys):
    values = ["3", "4", "4", "5", "5", "5"]
    input_count = 0

    def fake_input(*args):
        nonlocal input_count

        if input_count >= len(values):
            pytest.fail(
                "best_choice() attempted to read more than "
                "3 * board_count input values."
            )

        value = values[input_count]
        input_count += 1
        return value

    monkeypatch.setattr("builtins.input", fake_input)

    q6.best_choice(2, 10)

    capsys.readouterr()

    assert input_count == 6, (
        "best_choice() must read exactly "
        "3 * board_count input values."
    )


def test_best_choice_calls_area_calculator(monkeypatch, capsys):
    assert hasattr(q6, "area_calculator"), (
        "You must define the required area_calculator() helper function."
    )

    calls = []

    def fake_area_calculator(value1, value2):
        calls.append((value1, value2))
        return 999

    monkeypatch.setattr(
        q6,
        "area_calculator",
        fake_area_calculator
    )

    inputs = iter(["3", "4", "5"])

    monkeypatch.setattr(
        "builtins.input",
        lambda *args: next(inputs)
    )

    q6.best_choice(1, 10)

    capsys.readouterr()

    assert len(calls) > 0, (
        "best_choice() must call area_calculator()."
    )

    assert calls[0] in [(3, 4), (4, 3)], (
        "best_choice() must pass the board's length and width "
        "to area_calculator()."
    )