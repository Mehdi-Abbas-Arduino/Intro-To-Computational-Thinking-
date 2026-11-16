"""Rule checks for the worksheet. Student solutions belong in q1.py, q2.py, ...

Add one entry to _NAMES and _NUM_ARGS for every new question, then add the
question-specific rules in validate_rules().
"""
import ast
from pathlib import Path
import sys


_NAMES = {
    1: ('gcd',),
    2: ('add_check_digit', 'verify_check_digit'),
    3: ('diamond',),
    4: ('chickens_needed',),
    5: ('dot',),
    6: ('minmax',),
    7: ('check_types',),
    8: ('pop_bubbles',),
    9: ('create_scroll',),
    10: ('word_distance',),
}
# Number of required positional arguments of each required function.
_NUM_ARGS = {1: 2, 2: 1, 3: 1, 4: 4, 5: 2, 6: 1, 7: 1, 8: 2, 9: 2, 10: 2}
_FORBIDDEN_LOOPS = (ast.For, ast.AsyncFor, ast.While, ast.ListComp, ast.SetComp,
                    ast.DictComp, ast.GeneratorExp)
_HIDDEN_ITERATION = {'map', 'filter', 'sum', 'any', 'all', 'iter', 'next', 'reduce',
                     'sorted', 'enumerate', 'zip', 'eval', 'exec', 'compile',
                     '__import__', 'getattr', 'globals', 'locals', 'vars'}
_STRING_CONVERSION = {'str', 'repr', 'ascii', 'format', 'bin', 'hex', 'oct',
                      'join', '__str__', '__repr__', '__format__'}


def _is_main_guard(node):
    # Ignore manual demonstrations guarded by if __name__ == '__main__'.
    # Those statements do not execute when pytest imports the solution.
    if not isinstance(node, ast.If) or not isinstance(node.test, ast.Compare):
        return False
    test = node.test
    return (len(test.ops) == 1 and isinstance(test.ops[0], ast.Eq)
            and len(test.comparators) == 1
            and ((isinstance(test.left, ast.Name) and test.left.id == '__name__'
                  and isinstance(test.comparators[0], ast.Constant)
                  and test.comparators[0].value == '__main__')
                 or (isinstance(test.comparators[0], ast.Name)
                     and test.comparators[0].id == '__name__'
                     and isinstance(test.left, ast.Constant)
                     and test.left.value == '__main__')))


def _student_tree(module):
    tree = ast.parse(Path(module.__file__).read_text(encoding='utf8'))
    tree.body = [node for node in tree.body if not _is_main_guard(node)]
    return tree


def _called_name(node):
    if isinstance(node.func, ast.Name):
        return node.func.id
    if isinstance(node.func, ast.Attribute):
        return node.func.attr
    return ''


def _function_nodes(tree):
    return [node for node in ast.walk(tree)
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.Lambda))]


# Python does not carry variable types in its syntax tree. Methods unique
# to strings can be rejected directly; shared methods (e.g., .count() and
# .index()) are rejected only when the receiver is provably a string.
_STRING_METHODS = {name for name in dir(str) if not name.startswith('__')}
_STRING_ONLY_METHODS = _STRING_METHODS - set(dir(list)) - set(dir(tuple)) - set(dir(dict))


def _function_body_nodes(function):
    """Visit code executed by one function, excluding nested function bodies."""
    pending = list(function.body)
    while pending:
        node = pending.pop()
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.Lambda)):
            continue
        yield node
        pending.extend(ast.iter_child_nodes(node))


def _known_string(expr, names, string_returns=()):
    """Whether an expression is known to have a string value."""
    if isinstance(expr, ast.Constant):
        return isinstance(expr.value, str)
    if isinstance(expr, ast.JoinedStr):
        return True
    if isinstance(expr, ast.Name):
        return expr.id in names
    if isinstance(expr, ast.Subscript):
        return _known_string(expr.value, names, string_returns)
    if isinstance(expr, ast.BinOp):
        if isinstance(expr.op, (ast.Add, ast.Mult)):
            return (_known_string(expr.left, names, string_returns)
                    or _known_string(expr.right, names, string_returns))
    if isinstance(expr, ast.Call):
        if isinstance(expr.func, ast.Name):
            return expr.func.id == 'str' or expr.func.id in string_returns
        if isinstance(expr.func, ast.Attribute):
            return (expr.func.attr in {'lower', 'upper', 'strip', 'lstrip',
                                      'rstrip', 'replace', 'join', 'capitalize',
                                      'casefold', 'swapcase', 'title', 'center',
                                      'ljust', 'rjust', 'zfill'}
                    and _known_string(expr.func.value, names, string_returns))
    if isinstance(expr, ast.IfExp):
        return (_known_string(expr.body, names, string_returns)
                and _known_string(expr.orelse, names, string_returns))
    return False


def _string_names_for_function(function, seeded=(), string_returns=()):
    """Conservatively infer string-valued locals and parameters."""
    known = set(seeded)
    assignments = {}
    for node in _function_body_nodes(function):
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name):
                    assignments.setdefault(target.id, []).append(node.value)
        elif isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name):
            if node.value is not None:
                assignments.setdefault(node.target.id, []).append(node.value)
        elif isinstance(node, ast.AugAssign) and isinstance(node.target, ast.Name):
            assignments.setdefault(node.target.id, []).append(node.value)

    # If a parameter is assigned a value of unknown type, avoid assuming
    # that a subsequent list method on the same name is a string method.
    for name in tuple(known):
        if name in assignments and not all(
                _known_string(expr, known, string_returns)
                for expr in assignments[name]):
            known.remove(name)
    for _ in range(len(assignments) + 1):
        updated = {name for name, values in assignments.items()
                   if values and all(_known_string(expr, known, string_returns)
                                     for expr in values)}
        if not (updated - known):
            break
        known.update(updated)
    return known


def _infer_string_names(tree, question):
    """Propagate known string types through helper arguments and return values.

    This catches e.g. scan(s, ...) where pop_bubbles() passes its string
    bubbles to scan(), and squeeze(s) called from create_scroll().  Unknown
    and demonstrably list-valued receivers remain exempt from checks for
    method names that strings share with lists (e.g. .count or .index).
    """
    funcs = {node.name: node for node in ast.walk(tree)
             if isinstance(node, ast.FunctionDef)}
    parameters = {name: set() for name in funcs}
    entry = 'pop_bubbles' if question == 8 else 'create_scroll'
    entry_arg_count = 1 if question == 8 else 2
    if entry in funcs:
        parameters[entry].update(
            arg.arg for arg in funcs[entry].args.args[:entry_arg_count])
    string_returns = set()

    for _ in range(100):
        local = {name: _string_names_for_function(function, parameters[name],
                                                  string_returns)
                 for name, function in funcs.items()}
        changed = False
        for name, function in funcs.items():
            for node in _function_body_nodes(function):
                if (isinstance(node, ast.Return) and node.value is not None
                        and _known_string(node.value, local[name], string_returns)
                        and name not in string_returns):
                    string_returns.add(name)
                    changed = True
                if not (isinstance(node, ast.Call) and isinstance(node.func, ast.Name)
                        and node.func.id in funcs):
                    continue
                destination = node.func.id
                param_names = [arg.arg for arg in funcs[destination].args.args]
                for param, expr in zip(param_names, node.args):
                    if (_known_string(expr, local[name], string_returns)
                            and param not in parameters[destination]):
                        parameters[destination].add(param)
                        changed = True
                for keyword in node.keywords:
                    if (keyword.arg in param_names
                            and _known_string(keyword.value, local[name], string_returns)
                            and keyword.arg not in parameters[destination]):
                        parameters[destination].add(keyword.arg)
                        changed = True
        if not changed:
            break

    return {name: _string_names_for_function(function, parameters[name],
                                             string_returns)
            for name, function in funcs.items()}, funcs, string_returns


def _check_string_methods(function, question):
    # Q3's existing within-function check stays unchanged; Q8 and Q9 use
    # the interprocedural version below.
    known = _string_names_for_function(function)
    for node in _function_body_nodes(function):
        if not (isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute)):
            continue
        method = node.func.attr
        if method in _STRING_METHODS and _known_string(node.func.value, known):
            if question != 9 or method != 'lower':
                raise AssertionError(
                    f'String method .{method}() is not allowed in Q{question}.')


def _check_string_methods_through_helpers(tree, question):
    local_names, funcs, string_returns = _infer_string_names(tree, question)
    for name, function in funcs.items():
        for node in _function_body_nodes(function):
            if not (isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute)):
                continue
            method = node.func.attr
            if (method in _STRING_METHODS
                    and _known_string(node.func.value, local_names[name], string_returns)
                    and (question != 9 or method != 'lower')):
                raise AssertionError(
                    f'String method .{method}() is not allowed in Q{question} '
                    f'(inside {name}()).')


def _assert_helpers_recursive(tree, required):
    required_ids = set(map(id, required))
    for helper in (node for node in ast.walk(tree)
                   if isinstance(node, ast.FunctionDef) and id(node) not in required_ids):
        assert any(isinstance(node, ast.Call)
                   and isinstance(node.func, ast.Name) and node.func.id == helper.name
                   for node in ast.walk(helper)), (
            f'Helper function {helper.name}() must be recursive: it must call itself.')


def _assert_no_lambdas(tree):
    # A lambda cannot satisfy the worksheet's requirement that every helper
    # function directly calls itself by its own name.
    assert not any(isinstance(node, ast.Lambda) for node in ast.walk(tree)), (
        'All helper functions must be named recursive functions.')


def _assert_no_hidden_iteration(tree):
    for function in (node for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)):
        for node in ast.walk(function):
            if isinstance(node, ast.Call):
                assert _called_name(node) not in _HIDDEN_ITERATION, (
                    'Hidden iteration and dynamic workarounds are not permitted; use recursion.')


def validate_rules(module, question):
    names = _NAMES[question]
    tree = _student_tree(module)
    count = _NUM_ARGS[question]

    # Every required function: defined exactly once, with the right signature.
    required = []
    for name in names:
        roots = [node for node in tree.body
                 if isinstance(node, ast.FunctionDef) and node.name == name]
        assert len(roots) == 1, f'Define exactly one {name}() in q{question}.py.'
        root = roots[0]
        args = root.args
        assert not (args.vararg or args.kwarg or args.kwonlyargs or args.posonlyargs), (
            f'{name}() must take {count} required positional argument(s).')
        assert len(args.args) == count and not args.defaults, (
            f'{name}() must take exactly {count} required positional argument(s) '
            'and no default parameters. Parameter names are your choice.')
        required.append(root)

    # Only the required entry-point functions have fixed signatures.
    # The worksheet allows helper functions to take whatever parameters they
    # need, including optional/default parameters.

    # Rules shared by every question.
    if question in (2, 3, 4, 7, 8, 9, 10):
        assert not any(isinstance(node, ast.Global) for node in ast.walk(tree)), (
            'Global variables are not permitted.')
    # A nonlocal name belongs to an enclosing helper, not global scope.
    # Module-level assignments are forbidden. The demonstrations under
    # `if __name__ == "__main__":` are intentionally exempt.
    if question in (2, 3, 4, 7, 8, 9, 10):
        assert not any(isinstance(node, (ast.Assign, ast.AnnAssign, ast.AugAssign, ast.NamedExpr))
                       for node in tree.body), 'Module-level global variables are not permitted.'
    if question != 10:
        assert not any(isinstance(node, _FORBIDDEN_LOOPS) for node in ast.walk(tree)), (
            'Loops and comprehensions are not permitted; use recursion.')
    assert not any(isinstance(node, ast.AsyncFunctionDef) for node in ast.walk(tree)), (
        'Use ordinary recursive functions, not async functions.')

    if question == 1:
        # gcd(): one function only, direct recursion, no imports, no built-ins.
        root = required[0]
        assert len(_function_nodes(tree)) == 1, (
            'Helper functions (including nested functions) are not permitted.')
        assert any(isinstance(node, ast.Call)
                   and isinstance(node.func, ast.Name) and node.func.id == root.name
                   for node in ast.walk(root)), f'{root.name}() must call itself recursively.'
        assert not any(isinstance(node, (ast.Import, ast.ImportFrom)) for node in ast.walk(tree)), (
            'Modules may not be imported in this question.')
        for node in ast.walk(root):
            if isinstance(node, ast.Call):
                assert isinstance(node.func, ast.Name) and node.func.id == root.name, (
                    'Built-in functions and methods are not permitted; '
                    'only the recursive call to gcd() is allowed.')

    if question == 2:
        # Helpers are allowed, but every helper must call itself.
        _assert_no_lambdas(tree)
        _assert_helpers_recursive(tree, required)
        # No conversion of numeric IDs to strings and no hidden iteration.
        for function in (node for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)):
            for node in ast.walk(function):
                if isinstance(node, ast.JoinedStr):
                    raise AssertionError('f-strings are not permitted: do not convert idnum to a string.')
                if (isinstance(node, ast.BinOp) and isinstance(node.op, ast.Mod)
                        and isinstance(node.left, ast.Constant)
                        and isinstance(node.left.value, str)):
                    raise AssertionError('Do not use % formatting to convert idnum to a string.')
                if isinstance(node, ast.Call):
                    method = _called_name(node)
                    assert method not in _STRING_CONVERSION, (
                        'Do not convert idnum to a string.')
                    assert method not in _HIDDEN_ITERATION, (
                        'Hidden iteration and dynamic workarounds are not permitted; use recursion.')


    if question == 3:
        # diamond(): recursive helpers allowed; no string methods or formatting.
        _assert_no_lambdas(tree)
        _assert_helpers_recursive(tree, required)
        _assert_no_hidden_iteration(tree)
        for function in (node for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)):
            for node in ast.walk(function):
                assert not isinstance(node, ast.JoinedStr), (
                    'f-strings are not permitted: do not use string formatting.')
                if (isinstance(node, ast.BinOp) and isinstance(node.op, ast.Mod)
                        and isinstance(node.left, (ast.Constant, ast.JoinedStr))
                        and isinstance(getattr(node.left, 'value', ''), str)):
                    raise AssertionError('The % operator is not permitted for formatting strings.')
                if isinstance(node, ast.Call):
                    method = _called_name(node)
                    if isinstance(node.func, ast.Attribute):
                        assert method not in _STRING_ONLY_METHODS and not method.startswith('__'), (
                            f'String methods (such as {method}) are not permitted.')
                    assert method not in ('format', 'ascii', 'repr'), (
                        'String formatting is not permitted.')
        for function in (node for node in ast.walk(tree)
                         if isinstance(node, ast.FunctionDef)):
            _check_string_methods(function, 3)


    if question == 4:
        # chickens_needed(): exactly one directly recursive function.
        # No built-ins, imported modules, or the power operator.
        root = required[0]
        assert len(_function_nodes(tree)) == 1, (
            'Helper functions (including nested functions) are not permitted.')
        assert any(isinstance(node, ast.Call)
                   and isinstance(node.func, ast.Name) and node.func.id == root.name
                   for node in ast.walk(root)), (
            f'{root.name}() must call itself recursively.')
        assert not any(isinstance(node, (ast.Import, ast.ImportFrom)) for node in ast.walk(tree)), (
            'Modules may not be imported in this question.')
        for node in ast.walk(root):
            if isinstance(node, ast.Call):
                assert isinstance(node.func, ast.Name) and node.func.id == root.name, (
                    'Built-in functions, methods, and helper functions are not permitted; '
                    'only recursive calls to chickens_needed() are allowed.')
            if isinstance(node, (ast.BinOp, ast.AugAssign)) and isinstance(node.op, ast.Pow):
                raise AssertionError('The exponentiation operator ** is not permitted.')


    if question == 5:
        # dot(): directly recursive, no helpers, imports or built-ins except len().
        root = required[0]
        assert len(_function_nodes(tree)) == 1, (
            'Helper functions (including nested functions) are not permitted.')
        assert any(isinstance(node, ast.Call)
                   and isinstance(node.func, ast.Name) and node.func.id == root.name
                   for node in ast.walk(root)), (
            f'{root.name}() must call itself recursively.')
        assert not any(isinstance(node, (ast.Import, ast.ImportFrom)) for node in ast.walk(tree)), (
            'Modules may not be imported in this question.')
        for node in ast.walk(root):
            if isinstance(node, ast.Call):
                assert isinstance(node.func, ast.Name) and node.func.id in (root.name, 'len'), (
                    'Only len() and recursive calls to dot() are allowed; '
                    'all other built-ins, methods, and functions are prohibited.')


    if question == 6:
        # minmax(): one directly recursive function, no helper functions.
        # Built-in calls are limited to len(); no list methods or imports.
        root = required[0]
        assert len(_function_nodes(tree)) == 1, (
            'Helper functions (including nested functions) are not permitted.')
        assert any(isinstance(node, ast.Call)
                   and isinstance(node.func, ast.Name) and node.func.id == root.name
                   for node in ast.walk(root)), (
            f'{root.name}() must call itself recursively.')
        assert not any(isinstance(node, (ast.Import, ast.ImportFrom))
                       for node in ast.walk(tree)), (
            'Modules may not be imported in this question.')
        for node in ast.walk(root):
            if isinstance(node, ast.Call):
                assert isinstance(node.func, ast.Name) and node.func.id in (root.name, 'len'), (
                    'Only len() and recursive calls to minmax() are allowed; '
                    'list methods, other built-ins, and other functions are prohibited.')


    if question == 7:
        # Q7 permits recursive helper functions. check_types() may delegate
        # recursion to a helper instead of calling itself directly.
        # The supplied get_data_type() is the sole nonrecursive exemption.
        provided = [node for node in tree.body
                    if isinstance(node, ast.FunctionDef) and node.name == 'get_data_type']
        assert len(provided) == 1, 'Keep the provided get_data_type(e) function.'
        _assert_no_lambdas(tree)
        _assert_helpers_recursive(tree, required + provided)
        assert not any(isinstance(node, (ast.Import, ast.ImportFrom))
                       for node in ast.walk(tree)), (
            'Modules may not be imported in this question.')
        _assert_no_hidden_iteration(tree)
        permitted_names = {function.name for function in _function_nodes(tree)}
        permitted_names.update(('len', 'type', 'isinstance'))
        # List methods and membership operators are permitted by the PDF.
        # Student-defined named functions must nevertheless be recursive.
        for function in (node for node in ast.walk(tree)
                         if isinstance(node, ast.FunctionDef)):
            for node in ast.walk(function):
                if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
                    assert node.func.id in permitted_names, (
                        'Only recursive helpers, check_types(), get_data_type(), '
                        'len(), type(), and isinstance() may be called as functions.')


    if question == 8:
        # pop_bubbles() and every student-defined helper must recurse.
        root = required[0]
        _assert_no_lambdas(tree)
        _assert_helpers_recursive(tree, required)
        # pop_bubbles may delegate to a recursively defined helper.
        # Actual recursive execution is tested separately.
        assert not any(isinstance(node, (ast.Import, ast.ImportFrom))
                       for node in ast.walk(tree)), (
            'Modules may not be imported in this question.')
        _assert_no_hidden_iteration(tree)
        for node in ast.walk(tree):
            if isinstance(node, (ast.Set, ast.SetComp)):
                raise AssertionError('The set data structure is not permitted.')
            if isinstance(node, ast.Compare):
                assert not any(isinstance(op, (ast.In, ast.NotIn)) for op in node.ops), (
                    'The in and not in operators are not permitted.')
            if isinstance(node, ast.List) and any(
                    isinstance(el, ast.Starred) for el in node.elts):
                raise AssertionError('Unpacking a string into a list is not permitted.')
        for function in (node for node in ast.walk(tree)
                         if isinstance(node, ast.FunctionDef)):
            for node in ast.walk(function):
                if isinstance(node, ast.Call):
                    called = _called_name(node)
                    assert called not in ('set', 'frozenset'), (
                        'The set data structure is not permitted.')
                    if isinstance(node.func, ast.Attribute):
                        assert called not in _STRING_ONLY_METHODS and not called.startswith('__'), (
                            'String methods are not permitted.')
                    if called == 'list':
                        assert not node.args and not node.keywords, (
                            'Do not convert strings into lists.')
        _check_string_methods_through_helpers(tree, 8)


    if question == 9:
        # Every helper must recurse; create_scroll may delegate to them.
        # No iteration, modules, global state, or string methods except lower().
        _assert_no_lambdas(tree)
        _assert_helpers_recursive(tree, required)
        _assert_no_hidden_iteration(tree)
        assert not any(isinstance(node, (ast.Import, ast.ImportFrom))
                       for node in ast.walk(tree)), (
            'Modules may not be imported in this question.')
        for node in ast.walk(tree):
            if isinstance(node, ast.List) and any(
                    isinstance(el, ast.Starred) for el in node.elts):
                raise AssertionError('Do not convert strings into lists.')
            if isinstance(node, ast.Call):
                called = _called_name(node)
                if called == 'list':
                    assert not node.args and not node.keywords, (
                        'Do not convert strings into lists using list().')
                if called == 'split':
                    raise AssertionError('Do not convert strings into lists using split().')
                if isinstance(node.func, ast.Attribute):
                    assert called == 'lower' or called not in _STRING_ONLY_METHODS, (
                        'String methods other than lower() are not permitted.')
        _check_string_methods_through_helpers(tree, 9)




def assert_recursion_executed(module, func, args):
    from _pw_runner import run_solution
    name = func.__name__
    question = int(module.__name__.lstrip('q'))
    observed = run_solution(question, name, *args)
    assert observed.recursion_executed, (
        'Recursion must actually execute on a representative valid input; '
        'an unreachable recursive call or unused helper does not count.')
