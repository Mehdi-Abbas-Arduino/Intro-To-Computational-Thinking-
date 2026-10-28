import ast
import hashlib
import inspect

import os
import sys

import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import q6


q6_testcases = [
    # Visible testcases
    ([('L', 'Masala Chai'), ('M', 'Iced Matcha Latte')], 'Enter drink size (L/M/S):\nChoose from one of the following flavors:\n--Iced Matcha Latte\n--Boba Tea\n--French Vanilla\n--Peppermint\n--Masala Chai\nFlavor:\nOrder 1: Large Masala Chai --- 225\n\nEnter drink size (L/M/S):\nChoose from one of the following flavors:\n--Iced Matcha Latte\n--Cappuccino\n--Flat White\n--Espresso\n--Black Coffee\n--Pumpkin Spice Latte\nFlavor:\nOrder 2: Medium Iced Matcha Latte --- 145\n\n', True),
    ([('S', 'Vanilla Latte')], 'Enter drink size (L/M/S):\nChoose from one of the following flavors:\n--Iced Matcha Latte\n--Caramel Latte\n--Vanilla Latte\n--Americano\n--Frappe\n--Ristretto\n--Turkish Coffee\nFlavor:\nOrder 1: Small Vanilla Latte --- 160\n\n', True),
    ([('M', 'Iced Matcha Latte'), ('S', 'Iced Matcha Latte'), ('L', 'Iced Matcha Latte')], 'Enter drink size (L/M/S):\nChoose from one of the following flavors:\n--Iced Matcha Latte\n--Cappuccino\n--Flat White\n--Espresso\n--Black Coffee\n--Pumpkin Spice Latte\nFlavor:\nOrder 1: Medium Iced Matcha Latte --- 145\n\nEnter drink size (L/M/S):\nChoose from one of the following flavors:\n--Iced Matcha Latte\n--Caramel Latte\n--Vanilla Latte\n--Americano\n--Frappe\n--Ristretto\n--Turkish Coffee\nFlavor:\nOrder 2: Small Iced Matcha Latte --- 110\n\nEnter drink size (L/M/S):\nChoose from one of the following flavors:\n--Iced Matcha Latte\n--Boba Tea\n--French Vanilla\n--Peppermint\n--Masala Chai\nFlavor:\nOrder 3: Large Iced Matcha Latte --- 175\n\n', True),

    # Hidden testcases
    ([('L', 'Boba Tea')], 'bff1493f4ac54666e7e9721b442699989a150e9416c28d6adb7ba2234547e513', False),
    ([('M', 'Cappuccino')], '8b794c87f0cfeddcde3d95172d29c17db1a9dca2f9c2fa2ec199daf174f3bedc', False),
    ([('S', 'Iced Matcha Latte')], '2cab0b7ea112cc682e07cac67e85cc33ddcdb61768e79d7462e4860b26a57baf', False),
    ([('L', 'Iced Matcha Latte')], 'ae824c65cdd7e7a612c777aab15afdef2652a8e2ee3e6d0834bd7cb5ac0275b3', False),
    ([('S', 'Turkish Coffee')], '2091bdc00497f8c1b07a0c7c55acb9945b4bab75389f48aa4b0c0930eb0be29e', False),
    ([('M', 'Espresso'), ('L', 'Masala Chai')], 'e8b4cef52053b9fb4d5ae942a61cd8dfcbe51c38406676192f3ca714943739b7', False),
    ([('S', 'Caramel Latte'), ('M', 'Black Coffee')], 'aee4fa93b776103c129861b27d7a736a1b888c2ad13b2557aec3afd09cae9322', False),
    ([('L', 'Peppermint'), ('S', 'Americano'), ('M', 'Flat White')], '7955cb2fe7765e4e75ad2583a06d6e676426c03eb67f6adb425e830878d0702f', False),
    ([('L', 'French Vanilla'), ('M', 'Pumpkin Spice Latte'), ('S', 'Frappe'), ('L', 'Iced Matcha Latte')], '0fcd9534d0f0d4e73d84a12e6494b676440723ba4143d083e1fde61c248d7b76', False),
    ([('M', 'Iced Matcha Latte'), ('L', 'Boba Tea'), ('S', 'Ristretto'), ('M', 'Cappuccino'), ('S', 'Vanilla Latte')], 'aa3ee30aa23248b6202a8aa158299096403d9c3af39e8d4913e851b1a847a8af', False),
    ([('S', 'Iced Matcha Latte'), ('L', 'Masala Chai'), ('M', 'Espresso'), ('L', 'Boba Tea'), ('S', 'Turkish Coffee'), ('M', 'Black Coffee'), ('L', 'French Vanilla'), ('S', 'Americano')], '36517858f890d4525634a6dbf6f817fec28c437f928ee7d84c3888b801ea954d', False),
    ([('L', 'Iced Matcha Latte'), ('S', 'Vanilla Latte'), ('M', 'Cappuccino'), ('L', 'Boba Tea'), ('S', 'Frappe'), ('M', 'Flat White'), ('L', 'Peppermint'), ('S', 'Ristretto'), ('M', 'Espresso'), ('L', 'Masala Chai'), ('S', 'Americano'), ('M', 'Black Coffee'), ('L', 'French Vanilla'), ('S', 'Caramel Latte'), ('M', 'Pumpkin Spice Latte'), ('L', 'Iced Matcha Latte'), ('S', 'Turkish Coffee'), ('M', 'Iced Matcha Latte'), ('L', 'Boba Tea'), ('S', 'Iced Matcha Latte')], '0db702ba0e6d6bf5ee36ff5a5efd151c8818a1430bd8f25570d721970826b53a', False),
]


def hashcode(value):
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def verify_recursion_rules():
    source = inspect.getsource(q6)
    tree = ast.parse(source)
    functions = [node for node in ast.walk(tree) if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))]
    caffeine_functions = [node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name == "caffeine"]
    assert len(caffeine_functions) == 1, "Define a function named caffeine()."
    main = caffeine_functions[0]
    assert len(functions) == 1, (
        "Helper functions are not allowed. Define only caffeine()."
    )
    assert not any(isinstance(node, ast.Lambda) for node in ast.walk(tree)), (
        "Helper functions are not allowed."
    )
    assert len(main.args.posonlyargs) + len(main.args.args) == 1 and not (
        main.args.kwonlyargs or main.args.vararg or main.args.kwarg or main.args.defaults
    ), "caffeine() must accept exactly one argument: number_of_orders."

    banned = (ast.For, ast.AsyncFor, ast.While, ast.ListComp,
              ast.SetComp, ast.DictComp, ast.GeneratorExp, ast.Global)
    for node in ast.walk(tree):
        assert not isinstance(node, banned), (
            "Loops, comprehensions, and global variables are not allowed."
        )
    for node in tree.body:
        assert isinstance(node, (ast.FunctionDef, ast.Import, ast.ImportFrom)) or (
            isinstance(node, ast.If) and isinstance(node.test, ast.Compare)
            and isinstance(node.test.left, ast.Name)
            and node.test.left.id == "__name__"
        ), "Do not define global variables or execute test calls outside the main guard."

    assert any(
        isinstance(child, ast.Call)
        and isinstance(child.func, ast.Name)
        and child.func.id == "caffeine"
        for child in ast.walk(main)
    ), "You must use direct recursion within caffeine()."


@pytest.mark.parametrize("orders, expected, visible", q6_testcases)
def test_q6(orders, expected, visible, monkeypatch, capsys):
    verify_recursion_rules()
    answer_iter = iter([item for size, drink in orders for item in (size, drink)])
    supplied_count = [0]

    def fake_input(prompt=""):
        # Show prompts without echoing typed answers (inputs are not output).
        if prompt:
            print(prompt.rstrip())
        supplied_count[0] += 1
        try:
            return next(answer_iter)
        except StopIteration:
            pytest.fail("The function requested more input than the number of orders allows.")

    monkeypatch.setattr("builtins.input", fake_input)
    result = q6.caffeine(len(orders))
    actual = capsys.readouterr().out

    assert result is None, "caffeine() must print the output and return nothing."
    assert supplied_count[0] == 2 * len(orders), (
        "Read one size and one flavor for each order."
    )
    if visible:
        assert actual == expected
    else:
        assert hashcode(actual) == expected, "Incorrect order transcript."