"""Persistent isolated execution worker for the shared student/instructor tests."""
import contextlib
import importlib
import io
import json
import sys
import traceback
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))


class _BoundedOutput(io.StringIO):
    MAX_CHARS = 4000

    def write(self, value):
        remaining = self.MAX_CHARS - len(self.getvalue())
        if remaining > 0:
            super().write(value[:remaining])
        return len(value)


def run_one(request):
    question = request['question']
    function_name = request['function']
    args = request['args']
    program_path = str((ROOT / ('q%d.py' % question)).resolve())
    active = []
    recursion_observed = [False]

    def trace(frame, event, arg):
        if event not in ('call', 'return') or frame.f_code.co_filename != program_path:
            return
        if event == 'call':
            code = frame.f_code
            if code in active:
                recursion_observed[0] = True
            active.append(code)
        elif active:
            active.pop()

    capture = _BoundedOutput()
    try:
        # Keep the subprocess protocol clean, while returning bounded debug
        # prints so students can see them with pytest -s or on failures.
        with contextlib.redirect_stdout(capture):
            module = importlib.import_module('q%d' % question)
            function = getattr(module, function_name)
            sys.setprofile(trace)
            try:
                value = function(*args)
            finally:
                sys.setprofile(None)
        return {
            'ok': True, 'result': value, 'type': type(value).__name__,
            'args_after': args, 'recursive': recursion_observed[0],
            'stdout': capture.getvalue(),
        }
    except BaseException as exc:
        sys.setprofile(None)
        return {
            'ok': False, 'error_type': type(exc).__name__,
            'error': str(exc), 'traceback': traceback.format_exc(limit=5),
            'stdout': capture.getvalue(),
        }


def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            response = run_one(json.loads(line))
            output = json.dumps(response, ensure_ascii=True)
        except BaseException as exc:
            output = json.dumps({'ok': False, 'error_type': type(exc).__name__,
                                 'error': str(exc), 'traceback': traceback.format_exc(limit=5)})
        sys.stdout.write(output + '\n')
        sys.stdout.flush()


if __name__ == '__main__':
    main()
