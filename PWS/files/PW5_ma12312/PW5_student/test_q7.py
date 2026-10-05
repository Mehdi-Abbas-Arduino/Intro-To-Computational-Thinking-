import pytest
import hashlib
import inspect
import ast
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

import q7


def normalize_output(output):
    lines = output.rstrip("\n").split("\n")
    return "\n".join(line.rstrip() for line in lines)


def hashcode(value):
    return hashlib.sha256(str(value).encode("utf-8")).hexdigest()


def _assert_no_string_multiplication(source):
    tree = ast.parse(source)
    string_names = set()

    changed = True
    while changed:
        changed = False
        for node in ast.walk(tree):
            if isinstance(node, (ast.Assign, ast.AnnAssign)):
                value = node.value
                targets = node.targets if isinstance(node, ast.Assign) else [node.target]
                is_string_value = (
                    isinstance(value, ast.Constant) and isinstance(value.value, str)
                ) or (
                    isinstance(value, ast.Name) and value.id in string_names
                )
                if is_string_value:
                    for target in targets:
                        if isinstance(target, ast.Name) and target.id not in string_names:
                            string_names.add(target.id)
                            changed = True

    def is_string_operand(node):
        return (
            isinstance(node, ast.Constant) and isinstance(node.value, str)
        ) or (
            isinstance(node, ast.Name) and node.id in string_names
        )

    for node in ast.walk(tree):
        if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Mult):
            if is_string_operand(node.left) or is_string_operand(node.right):
                pytest.fail("Do not use string multiplication to generate repeated output.")


q7_testcases = [
    (5, '    *\n   * *\n  * * *\n * * * *\n* * * * *', True),
    (3, '  *\n * *\n* * *', True),
    (1, '684888c0ebb17f374298b65ee2807526c066094c701bcc7ebbe1c1095f494fc1', False),
    (2, '470c30e3d0a5020a6c82276dd2687fde308a33c268bac3805353c4c9363b3e36', False),
    (4, '6d91329db4895160e3198b7a8adf4568ba8b3cb08659fbf7f562c6663c1ba366', False),
    (6, '6e3d1499f15ff0d5a932d246c98d55616faa32e922c197e13b9670c62af9dbbf', False),
    (7, 'a2c2513e90148f01d456a5fd79a69309271fcfb642840bd690d4749d2ad5b4b6', False),
    (8, '4e85fe3650b49343dd55baa78383488704aaaee677014aa4bbfce5279f6f28dd', False),
    (10, 'a63bff393b223307d2abc5e7fa9ae16570b319ab736b4b5ca43069db47bde5c5', False),
    (12, 'af50bc64e4334e9694bcecd67b95f03dd8901ad8c36d8ba35fb74a72b11a2b7f', False),
    (15, '1f9a7326126bf70e19de0c1b817066f44fa307cdb2f38ad5a2e9bd90d3e6a8bc', False),
    (20, 'a1982f79c89ae16b47efdd5661e22220e975e42fc4ee7348efe98e0aa8c28b1e', False),
    (25, '34aa99af8b3aa185de6a4eee231c03dbd0c80c948d929262236cb29889a45774', False),
    (30, '1b8cdb1925e2d751747323487c2f03733ad9943e393b402bf616ae3b3551a7fb', False),
    (40, '2747319326b9ca86f4f6565803e1f53e9e050f8066d3ffcd5cfaea8a5fd121fb', False),
]


@pytest.mark.parametrize("height, result, visible", q7_testcases)
def test_q7(capsys, height, result, visible):
    q7.print_pyramid(height)
    actual = normalize_output(capsys.readouterr().out)
    if visible:
        assert actual == result
    else:
        assert hashcode(actual) == result


def test_q7_function_names_and_parameters():
    assert hasattr(q7, "print_spaces")
    assert hasattr(q7, "print_stars")
    assert hasattr(q7, "print_pyramid")
    assert list(inspect.signature(q7.print_spaces).parameters) == ["space_count"]
    assert list(inspect.signature(q7.print_stars).parameters) == ["star_count"]
    assert list(inspect.signature(q7.print_pyramid).parameters) == ["height"]


def test_q7_preserves_helper_structure_and_iteration():
    pyramid_tree = ast.parse(inspect.getsource(q7.print_pyramid))
    helper_calls = {
        node.func.id
        for node in ast.walk(pyramid_tree)
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name)
    }
    assert "print_spaces" in helper_calls and "print_stars" in helper_calls, \
        "print_pyramid must use both provided helper functions."
    assert any(isinstance(node, (ast.For, ast.While)) for node in ast.walk(pyramid_tree)), \
        "print_pyramid must use iteration."

    for helper in (q7.print_spaces, q7.print_stars):
        helper_tree = ast.parse(inspect.getsource(helper))
        assert any(isinstance(node, (ast.For, ast.While)) for node in ast.walk(helper_tree)), \
            "The provided helper functions must use iteration."


def test_q7_no_string_multiplication():
    _assert_no_string_multiplication(inspect.getsource(q7))
