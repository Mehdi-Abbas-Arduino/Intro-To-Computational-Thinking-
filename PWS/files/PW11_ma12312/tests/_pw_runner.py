"""Call student functions in a persistent, isolated Python process.

Each invocation has a hard five-second deadline; the worker is terminated if it
hangs. The exact same runner and cases are used by students and instructors.
"""
import atexit
import json
import queue
import subprocess
import sys
import threading
from pathlib import Path
from types import SimpleNamespace


_ROOT = Path(__file__).resolve().parent.parent
_WORKER = Path(__file__).resolve().parent / '_pw_worker.py'
TIMEOUT_SECONDS = 5
_workers = {}
_timeouts = {}


def _start_worker(question):
    process = subprocess.Popen(
        [sys.executable, '-u', str(_WORKER)],
        stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL,
        text=True, bufsize=1, encoding='utf-8', errors='replace', cwd=str(_ROOT),
    )
    responses = queue.Queue()

    def reader():
        for line in process.stdout:
            responses.put(line)
        responses.put(None)

    threading.Thread(target=reader, daemon=True).start()
    _workers[question] = (process, responses)
    return process, responses


def _stop_worker(question):
    item = _workers.pop(question, None)
    if item is not None:
        process, _ = item
        if process.poll() is None:
            process.kill()
        try:
            process.wait(timeout=1)
        except subprocess.TimeoutExpired:
            pass


def _close_all():
    for question in list(_workers):
        _stop_worker(question)


atexit.register(_close_all)


def run_solution(question, function, *args):
    assert question not in _timeouts, _timeouts.get(question)
    process, responses = _workers.get(question) or _start_worker(question)
    payload = json.dumps({'question': question, 'function': function, 'args': args})
    try:
        process.stdin.write(payload + '\n')
        process.stdin.flush()
        response = responses.get(timeout=TIMEOUT_SECONDS)
    except queue.Empty:
        message = (f'q{question}.{function}() exceeded {TIMEOUT_SECONDS} seconds. '
                   'Check for missing base cases or infinite loops.')
        _timeouts[question] = message
        _stop_worker(question)
        raise AssertionError(message) from None
    except (OSError, BrokenPipeError, ValueError) as exc:
        _stop_worker(question)
        raise AssertionError(f'Test worker stopped unexpectedly: {exc}') from None
    if response is None:
        _stop_worker(question)
        raise AssertionError(f'q{question}.{function}() terminated unexpectedly.')
    try:
        data = json.loads(response)
    except json.JSONDecodeError:
        _stop_worker(question)
        raise AssertionError(f'Invalid output from test worker for q{question}.{function}().') from None
    # Under -s, debug prints are visible immediately. Without -s, pytest
    # captures them and includes them when the corresponding test fails.
    if data.get('stdout'):
        print(f"[q{question}.{function} debugging output]\n"
              + data['stdout']
              + ('\n[Output truncated at 4000 characters]' if len(data['stdout']) >= 4000 else ''),
              end='' if data['stdout'].endswith('\n') else '\n')
    assert data['ok'], (
        f"q{question}.{function}() raised {data['error_type']}: {data['error']}\n"
        + data.get('traceback', ''))
    return SimpleNamespace(value=data['result'], result_type=data['type'],
                           arguments_after=data['args_after'],
                           recursion_executed=data['recursive'])
