import ast
import hashlib
import io
import os
import re
import sys
from copy import deepcopy

import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import q6


CASES = [
    (
        'waqar, jamal, umair, shahid', 
        '20, 22, 19, 18', 
        ['shahid', 'umair', 'waqar', 'jamal'], True),
    
    (
        'Ayesha, Bilal, Sara, Hamza, Zoya, Omar',
        '22, 25, 21, 20, 22, 21',
        ['Hamza', 'Sara', 'Omar', 'Ayesha', 'Zoya', 'Bilal'], True), 
    
    (
        'pakistan, china, south korea, singapore, india, sri lanka',
        '70, 4000, 69, 42, 70, 69',
        '89d72706e5f5f7cbe814810e1d490aaee4602254ea0f62bf0423037d98cac362', False),
    (
        'pakistan', 
        '70', 
        '9af42f56d46fef03182d9cd7cfe08ef8b2c9389e12057222826a311bc6977396', False),

    (
        'Bathilda Bagshot, Regulus Black, Sirius Black, Colin Creevey',
        '160, 56, 58, 36',
        '377e0aa40f780c5871443e77cfc8d4cb0203d13b689b0e4a802c0076a7b6432d', False),
    
    (
        'Zara, Noor, Ahmed, Bilal',
        '19, 19, 19, 19',
        '49ae316a84e82128034b5eef3b7c05d4e4dab5bf87706100a78e7f484c55b029', False),
        
    (
        'Ali, Zoya, Ahmed, Bilal',
        '18, 21, 24, 30',
        'acdc75638ac048082e50fe1c83d21d2747f6bdfe77e835e9c9c7f1bee4192df6', False),
        
    (
        'Ali, Zoya, Ahmed, Bilal',
        '30, 24, 21, 18',
        '77bfb39062ceb546d29e502a7972e299642a64c6e199f48ac33a58b642a8d937', False),
        
    (
        'Sara Khan, Ali Raza, Omar Farooq, Hina Ali',
        '24, 20, 21, 20',
        '4409cfdc5fefdb7f2dd4adba1c815b16bbd113e18809dc3b884f2dfe6e75272c', False),
        
    (
        'Ayesha, Ayesha, Bilal, Ayesha',
        '22, 20, 22, 22',
        '7165e957ca1f4be136eb1c508250f1a109cd57a1d7e0144d1266d2e8c76a0f27', False),
    
    (
        'Farah, Hamza, Nida, Omer, Rida, Sameer, Talha, Wania, Yaseen, Zara',
        '31, 25, 25, 22, 31, 18, 22, 18, 25, 31',
        '9fa31a893db215d934069884372b0230090dd75d167dd23a1409783f395c02ea', False),
        
    (
        'A',
        '1',
        '7651b17ff0fbdd2848ec9526ab8c632e2f570ce5616ee1651adbea5683ec2f77', False),
        
    (
        'Fatima Noor, Syed Ali, Sana',
        '100, 99, 100',
        '49e0525521a1ea7535401e21ffac2bf6a2327889ed904633ecfe9638036f0f8a', False),
    (
        'Amal, Omar, Daniyal, Huda',
        '1000, 2, 1001, 1',
        '82f2b88357498b8c3cefd0e9414df0be5229678c28a38349b91cd9561d6b439f', False),
    (
        'Amina, Bilal  Khan, Shahid Ali, Rehan',
        '35, 35, 20, 20',
        '201f3ca4199ec6f8f928c2994fdd87518a10e815754287f19cee088875b0279a', False)
    ]


def _check_answer(actual, expected, visible):
    assert isinstance(actual, list), "Expected a list of sorted names."
    if visible:
        assert actual == expected
    else:
        actual_hash = hashlib.sha256(str(actual).encode("utf-8")).hexdigest()
        assert actual_hash == expected, "Incorrect result for a hidden case."


def _printed_list(stdout):
    match = re.search(r"(\[[^\[\]]*\])\s*$", stdout)
    assert match, "main() must print the returned list of names."
    try:
        return ast.literal_eval(match.group(1))
    except (SyntaxError, ValueError) as error:
        pytest.fail(f"main() did not print a valid Python list: {error}")


class _TwoLineInput(io.StringIO):
    def __init__(self, first, second):
        super().__init__(first + "\n" + second + "\n")
        self.read_count = 0

    def readline(self, *args, **kwargs):
        self.read_count += 1
        if self.read_count > 2:
            raise AssertionError("main() must read exactly two input lines.")
        return super().readline(*args, **kwargs)


def _run_main(monkeypatch, capsys, names_line, ages_line):
    stream = _TwoLineInput(names_line, ages_line)

    def compatible_input(prompt=""):
        # Supports input(), input('prompt'), and sys.stdin.readline().
        line = stream.readline()
        if line == "":
            raise EOFError("main() requested too many input lines.")
        return line.rstrip("\r\n")

    with monkeypatch.context() as patch:
        patch.setattr("builtins.input", compatible_input)
        patch.setattr(sys, "stdin", stream)
        q6.main()

    printed = capsys.readouterr().out
    assert stream.read_count == 2, "main() must read the two supplied lines."
    assert stream.read() == "", "main() did not read both input lines."
    return _printed_list(printed)


@pytest.mark.parametrize(
    "names_line, ages_line, expected, visible",
    CASES,
    ids=[f"{'visible' if case[3] else 'hidden'}-{i:02d}" for i, case in enumerate(CASES, 1)],
)
def test_q6(monkeypatch, capsys, names_line, ages_line, expected, visible):
    names = [name.strip() for name in names_line.split(",")]
    ages = [int(age.strip()) for age in ages_line.split(",")]

    names_before, ages_before = deepcopy(names), deepcopy(ages)
    result = q6.seniority(names, ages)
    _check_answer(result, expected, visible)
    assert names == names_before, "seniority() must not modify names."
    assert ages == ages_before, "seniority() must not modify ages."

    actual = _run_main(monkeypatch, capsys, names_line, ages_line)
    _check_answer(actual, expected, visible)

    calls = []
    sentinel = ["__seniority_test_return_value__"]

    def spy(actual_names, actual_ages):
        calls.append((deepcopy(actual_names), deepcopy(actual_ages)))
        return sentinel

    with monkeypatch.context() as patch:
        patch.setattr(q6, "seniority", spy)
        displayed = _run_main(patch, capsys, names_line, ages_line)

    assert calls == [(names_before, ages_before)], (
        "main() must pass the parsed names and integer ages to seniority() once."
    )
    assert displayed == sentinel, "main() must print seniority()'s returned list."