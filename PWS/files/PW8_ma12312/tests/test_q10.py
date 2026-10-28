import hashlib
import os
import sys
import pytest

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
import q10
from q10 import *

q10_testcases = [
    # Visible Testcases
    ([3, 3, 1, 4, 4], [80, 73, 94, 62, 85], 2.91, True),
    ([2, 1, 1, 3, 1, 3, 4], [71, 60, 97, 86, 68, 66, 95], 3.1, True),
    ([1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [100, 95, 90, 85, 80, 75, 70, 67, 63, 60], 3.07, True),
    ([4, 3, 2, 1], [95, 85, 75, 60], 3.48, True),
    ([4], [100], 4.0, True),

    # Hidden Testcases
    ([4, 3, 3, 1, 3, 3, 3, 1, 2, 3, 4, 3, 2, 2, 1, 2, 2, 1, 3, 1], [59, 52, 11, 31, 93, 20, 3, 11, 3, 56, 69, 64, 11, 83, 48, 30, 93, 71, 87, 36], 'c851818da2c4baa901131d0263d782fe6a0439f636cbc559f2fb4f54ffa04c8a', False),
    ([1, 3, 2, 1, 1, 2, 3, 4, 2, 2, 3, 1], [71, 71, 93, 96, 62, 72, 58, 100, 97, 71, 83, 92], 'f28d896c899c2d04c226701c2eeb961c4e606fcbcd60bfb274199dd824c2e41a', False),
    ([2, 4, 2, 1, 2, 1, 3, 3, 2, 3, 3, 4, 3, 1, 1, 3], [89, 64, 57, 96, 100, 59, 60, 92, 76, 60, 76, 64, 71, 82, 93, 54], 'dee1989ca2c8fece12f4b355f63650ceedb0752387ca217c25f0c3c7de616c5b', False),
    ([1, 1, 1, 1, 1, 1, 1, 1, 1], [94, 89, 84, 79, 74, 69, 66, 62, 59], 'd20e3cb50b2f37eeec18fb79d8a0bb53133b87acf83fb3eac68a34917a494d8b', False),
    ([4, 1], [59, 90], '1e9d7c27c8bbc8ddf0055c93e064a62fa995d177fee28cc8fa949bc8a4db06f4', False),
    ([3, 3, 3], [90, 85, 80], 'ae9e8d4b40b609cc99c7857722888eb7683c6951cb5e5d2e5c725063cfc1f015', False),
    ([1, 2, 3], [60, 67, 70], '0814305f8cfb2f14744b7c7ce9da6768802df7bdd801d62be3e0d7caa0d84c81', False),
    ([2, 2, 2, 2], [59, 60, 89, 90], '980d4a2ae197444d6a4ade444cb4654a7af5152e1b573e3a6ea80f14487bc336', False),
    ([4, 4, 1], [75, 75, 100], 'bb0635f951bfd55419a47fc08a859192049b4d0949cf2d09a4d4d6b2cafafb94', False),
    ([1, 4, 2, 3], [63, 70, 85, 95], '70159003c3341c3776f60c4b5a50ba2e3b26295aa0f27a26ba248cb6fc7ef60d', False),
]

def hashcode(value):
    return hashlib.sha256(str(value).encode("utf-8")).hexdigest()

def capture_main_lists(monkeypatch,capsys,credits,scores):
    inputs=iter([
        " ".join(str(x) for x in credits),
        " ".join(str(x) for x in scores)
    ])
    monkeypatch.setattr("builtins.input", lambda: next(inputs))
    captured=[]
    sentinel=3.14159
    def fake_calculate_gpa(c,s):
        captured.append((c,s))
        return sentinel
    monkeypatch.setattr(q10,"calculate_gpa",fake_calculate_gpa)
    result=q10.main()
    output=capsys.readouterr().out.strip()
    assert captured, "main() must call calculate_gpa()."
    assert len(captured)==1
    assert output == str(sentinel)
    assert result is None
    return captured[0]

@pytest.mark.parametrize("credits,scores,expected,visible",q10_testcases)
def test_q10_main_calls_calculate_gpa(monkeypatch,capsys,credits,scores,expected,visible):
    c,s=capture_main_lists(monkeypatch,capsys,credits,scores)
    assert c == credits
    assert s == scores
    assert all(isinstance(x,int) for x in c)
    assert all(isinstance(x,int) for x in s)

@pytest.mark.parametrize("credits,scores,expected,visible",q10_testcases)
def test_q10_main_output(monkeypatch,capsys,credits,scores,expected,visible):
    inputs=iter([
        " ".join(str(x) for x in credits),
        " ".join(str(x) for x in scores)
    ])
    monkeypatch.setattr("builtins.input",lambda:next(inputs))
    result=q10.main()
    captured=capsys.readouterr().out.strip()
    assert result is None
    try:
        value=float(captured)
    except ValueError:
        raise AssertionError("main() should print the GPA.")
    if visible:
        assert value == expected
    else:
        assert hashcode(value) == expected

@pytest.mark.parametrize("credits,scores,expected,visible",q10_testcases)
def test_q10_calculate_gpa(credits,scores,expected,visible):
    result=calculate_gpa(credits,scores)
    assert isinstance(result,(int,float))
    if visible:
        assert result == expected
    else:
        assert hashcode(result) == expected
