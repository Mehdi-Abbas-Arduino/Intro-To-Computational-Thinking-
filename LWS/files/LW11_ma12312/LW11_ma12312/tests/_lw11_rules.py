import ast
from pathlib import Path
import sys


_NAMES = {
    1: 'remove_vowels', 2: 'to_binary', 3: 'find_ing_words',
    4: 'flatten_eidi', 5: 'is_winning_ticket', 6: 'hours_per_member',
}
_NUM_ARGS = {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 2}
_FORBIDDEN_LOOPS = (ast.For, ast.AsyncFor, ast.While, ast.ListComp, ast.SetComp,
                    ast.DictComp, ast.GeneratorExp)
_INDIRECTION = {'eval', 'exec', 'compile', '__import__', 'getattr', 'globals', 'locals', 'vars'}


def _student_tree(module):
    return ast.parse(Path(module.__file__).read_text(encoding='utf8'))


def _called_name(node):
    if isinstance(node.func, ast.Name):
        return node.func.id
    if isinstance(node.func, ast.Attribute):
        return node.func.attr
    return ''


def validate_rules(module, question):
    name = _NAMES[question]
    tree = _student_tree(module)
    roots = [node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name == name]
    assert len(roots) == 1, f'Define exactly one {name}() in q{question}.py.'
    root = roots[0]
    count = _NUM_ARGS[question]
    args = root.args
    assert not (args.vararg or args.kwarg or args.kwonlyargs or args.posonlyargs), (
        f'{name}() must take {count} required positional argument(s).')
    assert len(args.args) == count and not args.defaults, (
        f'{name}() must take exactly {count} required positional argument(s).'
        ' Parameter names are your choice.')

    if question in (1, 2, 3, 4):
        all_funcs = [node for node in ast.walk(tree)
                     if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))]
        assert len(all_funcs) == 1, 'Helper functions are not permitted for this question.'
        assert any(isinstance(node, ast.Call)
                   and isinstance(node.func, ast.Name) and node.func.id == name
                   for node in ast.walk(root)), f'{name}() must call itself recursively.'

    assert not any(isinstance(node, ast.Global) for node in ast.walk(tree)), (
        'Global variables are not permitted.')
    assert not any(isinstance(node, (ast.Assign, ast.AnnAssign, ast.AugAssign, ast.NamedExpr))
                   for node in tree.body), 'Module-level global variables are not permitted.'
    if question <= 4:
        assert not any(isinstance(node, ast.Nonlocal) for node in ast.walk(tree)), (
            'Nonlocal variables are not permitted.')

    if question == 4 or question == 5:
        assert not any(isinstance(node, (ast.Import, ast.ImportFrom))
                       for node in ast.walk(tree)), 'Imports are not permitted in this question.'

    assert not any(isinstance(node, _FORBIDDEN_LOOPS) for node in ast.walk(tree)), (
        'Loops and comprehensions are not permitted; use recursion.')
    assert not any(isinstance(node, ast.AsyncFunctionDef) for node in ast.walk(tree)), (
        'Use ordinary recursive functions, not async functions.')
    if question == 5:
        assert not any(isinstance(node, ast.JoinedStr) for node in ast.walk(tree)), (
            'Converting digits to strings is forbidden.')
    if question == 2:
        assert not any(isinstance(node, ast.JoinedStr) for node in ast.walk(tree)), (
            'Formatted strings may not be used for binary conversion.')

    root_nodes = set(map(id, ast.walk(root)))

    student_functions = {n.name for n in ast.walk(tree) if isinstance(n, ast.FunctionDef)}
    banned_q6_names = {'sum', 'map', 'filter', 'reduce', 'zip', 'enumerate', 'iter', 'next'}
    imported_iterative_aliases = set()
    if question == 6:
        for imported in ast.walk(tree):
            if isinstance(imported, ast.ImportFrom):
                for alias in imported.names:
                    if alias.name in banned_q6_names or alias.name == 'accumulate':
                        imported_iterative_aliases.add(alias.asname or alias.name)

    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            method = _called_name(node)
            if question == 1 and id(node) in root_nodes:
                if isinstance(node.func, ast.Attribute) and node.func.attr != 'lower':
                    raise AssertionError(
                        'Only the string method lower() is permitted in remove_vowels().')
            if question == 2 and method in {'bin', 'format', '__format__'}:
                raise AssertionError('Do not use bin() or format() for binary conversion.')
            if question == 3 and method in ({'filter', 'map', 'any', 'all', 'iter', 'next'} | _INDIRECTION):
                raise AssertionError('Hidden iteration and dynamic workarounds are not permitted.')
            if question == 3 and isinstance(node.func, ast.Attribute) and method in dir(str):
                raise AssertionError('String methods are not permitted.')
            if question == 5 and method in ({'str', 'repr', 'ascii', 'bin', 'format',
                                             '__str__', '__repr__', '__format__'} | _INDIRECTION):
                raise AssertionError('Do not convert ticket digits into strings.')
            if question == 6:
                if (method in (banned_q6_names | _INDIRECTION | imported_iterative_aliases)
                        or (method == 'accumulate' and
                            (isinstance(node.func, ast.Attribute) or
                             'accumulate' not in student_functions or
                             'accumulate' in imported_iterative_aliases))):
                    raise AssertionError(
                        'No sum(), hidden iteration, or dynamic workarounds; use recursion.')
            if question == 6 and method == 'slice' and len(node.args) >= 3:
                raise AssertionError('Slicing with a step is not allowed.')
        if question == 6 and isinstance(node, ast.Subscript) and isinstance(node.slice, ast.Slice):
            assert node.slice.step is None, 'Slicing with a step is not allowed.'
        if question == 6 and isinstance(node, ast.Name) and node.id in {'__builtins__'}:
            raise AssertionError('Accessing built-ins indirectly is not permitted.')


def assert_recursion_executed(module, func, args):
    file_path = str(Path(module.__file__).resolve())
    active = []
    observed = [False]
    prior = sys.getprofile()

    def profile(frame, event, arg):
        if event not in ('call', 'return'):
            return
        if frame.f_code.co_filename != file_path:
            return
        if event == 'call':
            code = frame.f_code
            if code in active:
                observed[0] = True
            active.append(code)
        else:
            if active:
                active.pop()

    try:
        sys.setprofile(profile)
        func(*args)
    finally:
        sys.setprofile(prior)
    assert observed[0], (
        'Recursion must actually execute on a representative valid input; '
        'an unreachable recursive call or unused helper does not count.')