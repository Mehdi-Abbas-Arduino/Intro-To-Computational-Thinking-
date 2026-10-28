import pytest
import hashlib
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from q2 import *


def hashcode(value):
    return hashlib.sha256(str(value).encode("utf-8")).hexdigest()


q2_testcases = [
    ('10 20 30 40 50', [10, 20, 30, 40, 50], 150, True),
    ('1 2', [1, 2], 3, True),
    ('5 15 25 35', [5, 15, 25, 35], 80, True),
    ('99', [99], 99, True),
    ('-1 0 1', [-1, 0, 1], '5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9', False),
    ('100 200 300 400', [100, 200, 300, 400], '40510175845988f13f6162ed8526f0b09f73384467fa855e1e79b44a56562a58', False),
    ('-5 -10 -15', [-5, -10, -15], '4cbaf3fbc9b6ccc6d363e9cac9d51c6d3012fc8991a30cbe952c5e92c7927d92', False),
    ('3 6 9 12 15 18', [3, 6, 9, 12, 15, 18], 'da4ea2a5506f2693eae190d9360a1f31793c98a1adade51d93533a6f520ace1c', False),
    ('0', [0], '5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9', False),
    ('-100', [-100], 'b96b3036632771349308fbbe5d7a3f3f762c9e8f3eedd5785b13ff322e05fd9d', False),
    ('7 7 7 7 7', [7, 7, 7, 7, 7], '9f14025af0065b30e47e23ebb3b491d39ae8ed17d33739e5ff3827ffb3634953', False),
    ('1000000 -1000000 5', [1000000, -1000000, 5], 'ef2d127de37b942baad06145e54b0c619a1f22327b2ebbcfbec78f5564afe39d', False),
    ('12 -3 0 8 -17', [12, -3, 0, 8, -17], '5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9', False),
    ('-999 999', [-999, 999], '5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9', False),
    ('2 4 6 8 10 12 14 16', [2, 4, 6, 8, 10, 12, 14, 16], '8722616204217eddb39e7df969e0698aed8e599ba62ed2de1ce49b03ade0fede', False),
]


def capture_main_list(monkeypatch, input_string):
    monkeypatch.setattr("builtins.input", lambda prompt="": input_string)

    captured_list = []

    def fake_sum_lst(lst):
        captured_list.append(lst)
        return 0

    import q2
    monkeypatch.setattr(q2, "sum_lst", fake_sum_lst)

    q2.main()

    return captured_list[0]


@pytest.mark.parametrize("input_string, expected_list, expected_sum, visible", q2_testcases)
def test_q2_main_creates_integer_list(monkeypatch, capsys, input_string, expected_list, expected_sum, visible):
    actual_list = capture_main_list(monkeypatch, input_string)
    capsys.readouterr()

    assert isinstance(actual_list, list), "You had to create a list"
    assert all(isinstance(x, int) for x in actual_list), "You had to create a list of integers"
    assert actual_list == expected_list


@pytest.mark.parametrize("input_string, expected_list, expected_sum, visible", q2_testcases)
def test_q2_main_prints_sum(monkeypatch, capsys, input_string, expected_list, expected_sum, visible):
    monkeypatch.setattr("builtins.input", lambda prompt="": input_string)

    main()

    captured = capsys.readouterr().out.strip()

    if visible:
        assert int(captured) == expected_sum
    else:
        assert hashcode(int(captured)) == expected_sum


@pytest.mark.parametrize("input_string, expected_list, expected_sum, visible", q2_testcases)
def test_q2_sum_lst(input_string, expected_list, expected_sum, visible):
    if visible:
        assert sum_lst(expected_list) == expected_sum
    else:
        assert hashcode(sum_lst(expected_list)) == expected_sum