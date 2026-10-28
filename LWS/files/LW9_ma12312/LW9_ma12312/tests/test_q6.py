import builtins
import hashlib
import io
import os
import sys
from copy import deepcopy

import pytest
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

import q6


def hashcode(value):
    return hashlib.sha256(str(value).encode("utf-8")).hexdigest()


def expected_number(hall_layout, expected, visible):
    if visible:
        return expected
    max_count = sum(cell == 'I' for row in hall_layout for cell in row)
    for value in range(max_count + 1):
        if hashcode(value) == expected:
            return value
    raise AssertionError("Invalid hidden expected hash in test data.")


def silent_input(prompt=""):
    line = sys.stdin.readline()
    if line == "":
        raise EOFError("EOF when reading a line")
    return line.rstrip("\r\n")

q6_testcases = [
    ([['I', 'E', 'E', 'E'], ['E', 'E', 'I', 'E'], ['E', 'I', 'E', 'E']], 3, True),
    ([['I', 'I', 'E', 'E'], ['E', 'E', 'I', 'E'], ['E', 'E', 'E', 'I']], 2, True),
    ([['I', 'I', 'E'], ['I', 'I', 'E'], ['E', 'E', 'E']], 0, True),
    ([['I', 'E', 'E'], ['E', 'E', 'I'], ['E', 'I', 'E']], 3, True),
    ([['I', 'E', 'I'], ['E', 'I', 'E'], ['I', 'E', 'E']], 1, True),
    ([['E', 'E', 'E'], ['E', 'E', 'E']], 0, True),
    ([['I', 'E', 'E', 'E'], ['E', 'E', 'I', 'E'], ['E', 'I', 'E', 'E'], ['E', 'E', 'E', 'I']], 4, True),
    ([['I']], 1, True),
    ([['I', 'E'], ['I', 'E'], ['E', 'I']], 1, True),
    ([['I', 'I', 'I', 'I', 'I']], 0, True),
    ([['E']], '5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9', False),
    ([['E', 'E', 'I', 'E']], '6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b', False),
    ([['E'], ['I'], ['E'], ['I']], '5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9', False),
    ([['I', 'E', 'E', 'E'], ['E', 'I', 'E', 'E'], ['E', 'E', 'E', 'E'], ['I', 'E', 'E', 'I']], '6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b', False),
    ([['E', 'I', 'E', 'E', 'E'], ['I', 'E', 'E', 'E', 'E'], ['E', 'E', 'I', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'I', 'I']], '4e07408562bedb8b60ce05c1decfe3ad16b72230967de01f640b7e4729b49fce', False)
]


@pytest.mark.parametrize("hall_layout, expected, visible", q6_testcases)
def test_q6_main(hall_layout, expected, visible, monkeypatch, capsys):
    rows, columns = len(hall_layout), len(hall_layout[0])
    input_lines = [f"{rows} {columns}"] + [" ".join(row) for row in hall_layout]
    input_text = "\n".join(input_lines) + "\n"

    monkeypatch.setattr(builtins, "input", silent_input)
    original_helper = q6.count_solo_invigilators
    received_grids = []
    marker_result = 987654321

    def fake_helper(grid):
        received_grids.append(deepcopy(grid))
        return marker_result

    monkeypatch.setattr(q6, "count_solo_invigilators", fake_helper)
    supplied_input = io.StringIO(input_text)
    monkeypatch.setattr(sys, "stdin", supplied_input)
    q6.main()
    actual_print = capsys.readouterr().out.strip()

    assert supplied_input.tell() == len(input_text), (
        "main() must read the dimensions and all grid rows from input."
    )
    assert received_grids == [hall_layout], (
        "main() must construct the exact 2D list of 'I'/'E' strings "
        "and pass it once to count_solo_invigilators()."
    )
    assert actual_print == str(marker_result), (
        f"{actual_print} != {marker_result} (main() must print the helper's return value)"
    )

    def real_helper_checked(grid):
        count = original_helper(grid)
        assert type(count) is int, (
            "count_solo_invigilators() must return an integer."
        )
        return count

    monkeypatch.setattr(q6, "count_solo_invigilators", real_helper_checked)
    supplied_input = io.StringIO(input_text)
    monkeypatch.setattr(sys, "stdin", supplied_input)
    q6.main()
    printed_count = capsys.readouterr().out.strip()

    assert supplied_input.tell() == len(input_text), (
        "main() must read the dimensions and all grid rows from input."
    )
    correct_count = expected_number(hall_layout, expected, visible)
    if visible:
        assert printed_count == str(expected), f"{printed_count} != {expected}"
    else:
        assert hashcode(printed_count) == expected, f"{printed_count} != {correct_count}"