import pytest
import hashlib
import inspect
import ast
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

import q6


def hashcode(value):
    return hashlib.sha256(str(value).encode("utf-8")).hexdigest()


def normalized_codes(output):
    body = output.rstrip()

    assert "\n" not in body, "All codes must be printed on one line."

    if not body:
        return ""

    parts = body.split(" ")

    assert all(parts), \
        "Codes must be separated by exactly one space and must not begin with a space."

    assert len(parts) == len(set(parts)), \
        "Every valid code must appear exactly once."

    return " ".join(sorted(parts))


q6_testcases = [
    # Visible Testcases
    ("code", "cdeo cdoe cedo ceod code coed dceo dcoe deco deoc doce doec ecdo ecod edco edoc eocd eodc ocde oced odce odec oecd oedc", True),
    ("music", "cims cimu cism cisu cium cius cmis cmiu cmsi cmsu cmui cmus csim csiu csmi csmu csui csum cuim cuis cumi cums cusi cusm icms icmu icsm icsu icum icus imcs imcu imsc imsu imuc imus iscm iscu ismc ismu isuc isum iucm iucs iumc iums iusc iusm mcis mciu mcsi mcsu mcui mcus mics micu misc misu miuc mius msci mscu msic msiu msuc msui muci mucs muic muis musc musi scim sciu scmi scmu scui scum sicm sicu simc simu siuc sium smci smcu smic smiu smuc smui suci sucm suic suim sumc sumi ucim ucis ucmi ucms ucsi ucsm uicm uics uimc uims uisc uism umci umcs umic umis umsc umsi usci uscm usic usim usmc usmi", True),

    # Hidden Testcases
    ("abcd", "9f23fda5fe04dbb6b0d389c11c4fd659e2a1e62be19a8aba0037b6d3ffc4d6e9", False),
    ("tire", "57d7824d61c68bc0faa7ab05d448c7da209fcdd1f59d5f1873e89dc81b1c8404", False),
    ("campus", "5dd1e24dc2d2fbcec0d3c2d87a58b083f51e54393770fb6ccc3e572cd6dfdee2", False),
    ("python", "79fbd51889bef25b79cca5ab229f9d97e696cb365c21f5c28f930f976f0a2bd4", False),
    ("education", "974aec9aab57dc311675d1f686e0abcc390a37d60dd402e04d443208519ee7e8", False),
    ("abcdefg", "6e4e844bd3241bab9550cc6acab968cac20685f11cb7096cac3959d009f7f75d", False),
]


@pytest.mark.parametrize("letters, result, testcase", q6_testcases)
def test_q6(capsys, letters, result, testcase):
    q6.print_four_letter_codes(letters)
    actual = normalized_codes(capsys.readouterr().out)
    if testcase:
        assert actual == result
    else:
        assert hashcode(actual) == result


def test_q6_no_imports():
    tree = ast.parse(inspect.getsource(q6))
    assert not any(
        isinstance(node, (ast.Import, ast.ImportFrom))
        for node in ast.walk(tree)
    ), "Do not import any modules. Generate the codes using nested iteration."


def test_q6_uses_nested_iteration():
    tree = ast.parse(inspect.getsource(q6.print_four_letter_codes))
    loops = (ast.For, ast.While)

    has_nested_loop = any(
        isinstance(node, loops)
        and any(
            isinstance(child, loops)
            for child in ast.walk(node)
            if child is not node
        )
        for node in ast.walk(tree)
    )

    assert has_nested_loop, \
        "print_four_letter_codes must use nested iteration."


def test_q6_no_permutation_or_generation_shortcuts():
    source = inspect.getsource(q6.print_four_letter_codes)
    tree = ast.parse(source)

    forbidden_calls = {
        "__import__",
        "eval",
        "exec",
        "permutations",
        "permutation",
        "product",
        "combinations",
        "combinations_with_replacement",
        "multiset_permutations",
        "distinct_permutations",
        "perm",
    }

    forbidden_attributes = {
        "permutations",
        "permutation",
        "product",
        "combinations",
        "combinations_with_replacement",
        "multiset_permutations",
        "distinct_permutations",
        "perm",
    }

    for node in ast.walk(tree):
        if isinstance(node, (ast.ListComp, ast.SetComp, ast.DictComp, ast.GeneratorExp)):
            pytest.fail(
                "Do not use comprehensions or generator expressions as a shortcut. "
                "Generate the codes using explicit nested iteration."
            )

        if isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name) and node.func.id in forbidden_calls:
                pytest.fail(
                    f"Do not use {node.func.id}() as a shortcut. "
                    "Generate the codes using nested iteration."
                )

            if isinstance(node.func, ast.Attribute) and node.func.attr in forbidden_attributes:
                pytest.fail(
                    f"Do not use {node.func.attr}() as a shortcut. "
                    "Generate the codes using nested iteration."
                )
