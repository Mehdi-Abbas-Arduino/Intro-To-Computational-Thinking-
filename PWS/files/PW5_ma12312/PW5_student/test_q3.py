import pytest
import hashlib
import inspect
import ast
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from q3 import print_led_channels


def normalize_output(output):
    return "\n".join(line.rstrip() for line in output.rstrip("\n").splitlines())


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


q3_testcases = [
    (3, '1\n2 3 4\n5 6 7 8 9', True),
    (1, '1', True),
    (6, '1\n2 3 4\n5 6 7 8 9\n10 11 12 13 14 15 16\n17 18 19 20 21 22 23 24 25\n26 27 28 29 30 31 32 33 34 35 36', True),
    (2, '92aafdd4e975af3998a5b8b64862ef56bf8e106fc4a314701deea4b62242dd74', False),
    (4, 'eba984601ee7db796058d8e661bb311b2ad416e6798b5cd350a6d526bd6e5fc6', False),
    (5, '746e80a7e341229327784f49102cb83a9b693a833fa5c24cd26f8c3dcc417584', False),
    (7, '82d03efd5306f6e40da924970f699cff0c0365b630ff95e9394239b3ce9d5a96', False),
    (8, '0a31f442e0d1c224dffb7d231ed97ba9165f3c86368a60de97dc043cbf3997e0', False),
    (9, 'f607fc70c3e91a17a6e48ce3a635a85016a7008d2d9a6ad4ebc2df56f5309129', False),
    (10, 'd33d01de3b68e52d4c2cb956af88242e5fe3f92fb94527cf26fa86585f19a6ba', False),
    (12, '27c6f24134b5abe538d5840e1524e225928514be5b46a467ed83eae5ca3d4818', False),
    (15, 'eef3ec180d4f4504f4d28f11d30dfd037a3094f51412e910963bb6d8d8ab1ea4', False),
    (20, '8a0bf6d57d401b42b33ac4d7df52f25b6e9842f09ee83c5d09222fd68d244950', False),
    (25, 'b1d4362db132515dd94464a94b1f902d610ea248ca943b0b1667305b0c2adce1', False),
    (30, '3a13e069428559b49fa54105b10b798f779e1d1437ac216477202a3ec2ee4ad3', False),
]


@pytest.mark.parametrize("row_count, result, visible", q3_testcases)
def test_q3(capsys, row_count, result, visible):
    print_led_channels(row_count)
    actual = normalize_output(capsys.readouterr().out)
    if visible:
        assert actual == result
    else:
        assert hashcode(actual) == result


def test_q3_uses_nested_iteration():
    assert _has_nested_iteration(print_led_channels), \
        "print_led_channels must use nested iteration."
