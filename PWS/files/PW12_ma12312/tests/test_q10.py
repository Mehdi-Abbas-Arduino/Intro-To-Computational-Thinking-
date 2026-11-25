import copy
import hashlib
import os
import sys

import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
sys.path.insert(0, os.path.dirname(__file__))

from q10 import find_file


def hashcode(value):
    return hashlib.sha256(str(value).encode("utf-8")).hexdigest()


q10_testcases = [({'name': 'HU Drive',
   'files': ['welcome.txt'],
   'subfolders': [{'name': 'Courses',
                   'files': ['schedule.pdf'],
                   'subfolders': [{'name': 'CS101', 'files': ['lab1.py', 'notes.pdf'], 'subfolders': []},
                                  {'name': 'CS102', 'files': ['quiz.py'], 'subfolders': []}]},
                  {'name': 'Events', 'files': ['poster.png'], 'subfolders': []}]},
  'lab1.py',
  ['HU Drive', 'Courses', 'CS101', 'lab1.py'],
  True),
 ({'name': 'HU Drive',
   'files': ['welcome.txt'],
   'subfolders': [{'name': 'Courses',
                   'files': ['schedule.pdf'],
                   'subfolders': [{'name': 'CS101', 'files': ['lab1.py', 'notes.pdf'], 'subfolders': []},
                                  {'name': 'CS102', 'files': ['quiz.py'], 'subfolders': []}]},
                  {'name': 'Events', 'files': ['poster.png'], 'subfolders': []}]},
  'schedule.pdf',
  ['HU Drive', 'Courses', 'schedule.pdf'],
  True),
 ({'name': 'HU Drive',
   'files': ['welcome.txt'],
   'subfolders': [{'name': 'Courses',
                   'files': ['schedule.pdf'],
                   'subfolders': [{'name': 'CS101', 'files': ['lab1.py', 'notes.pdf'], 'subfolders': []},
                                  {'name': 'CS102', 'files': ['quiz.py'], 'subfolders': []}]},
                  {'name': 'Events', 'files': ['poster.png'], 'subfolders': []}]},
  'welcome.txt',
  ['HU Drive', 'welcome.txt'],
  True),
 ({'name': 'HU Drive',
   'files': ['welcome.txt'],
   'subfolders': [{'name': 'Courses',
                   'files': ['schedule.pdf'],
                   'subfolders': [{'name': 'CS101', 'files': ['lab1.py', 'notes.pdf'], 'subfolders': []},
                                  {'name': 'CS102', 'files': ['quiz.py'], 'subfolders': []}]},
                  {'name': 'Events', 'files': ['poster.png'], 'subfolders': []}]},
  'poster.png',
  ['HU Drive', 'Events', 'poster.png'],
  True),
 ({'name': 'HU Drive',
   'files': ['welcome.txt'],
   'subfolders': [{'name': 'Courses',
                   'files': ['schedule.pdf'],
                   'subfolders': [{'name': 'CS101', 'files': ['lab1.py', 'notes.pdf'], 'subfolders': []},
                                  {'name': 'CS102', 'files': ['quiz.py'], 'subfolders': []}]},
                  {'name': 'Events', 'files': ['poster.png'], 'subfolders': []}]},
  'assignment.pdf',
  [],
  True),
 ({'name': 'Courses',
   'files': ['schedule.pdf'],
   'subfolders': [{'name': 'CS101', 'files': ['lab1.py', 'notes.pdf'], 'subfolders': []},
                  {'name': 'CS102', 'files': ['quiz.py'], 'subfolders': []}]},
  'quiz.py',
  ['Courses', 'CS102', 'quiz.py'],
  True),
 ({'name': 'Empty Folder', 'files': [], 'subfolders': []}, 'notes.pdf', [], True),
 ({'name': 'Course', 'files': ['exam.pdf', 'project.py'], 'subfolders': []},
  'exam.pdf',
  'f59bf94c70bbccbc197a7332b935cd6745b768e212e27ef17e28bff318a38e57',
  False),
 ({'name': 'L1',
   'files': [],
   'subfolders': [{'name': 'L2',
                   'files': [],
                   'subfolders': [{'name': 'L3',
                                   'files': [],
                                   'subfolders': [{'name': 'L4',
                                                   'files': [],
                                                   'subfolders': [{'name': 'L5',
                                                                   'files': ['final.py'],
                                                                   'subfolders': []}]}]}]}]},
  'final.py',
  '26e15168e8be121b2a700adf6d18409338fba6b1e3f98996042e270cf79de96f',
  False),
 ({'name': 'Root',
   'files': [],
   'subfolders': [{'name': 'L',
                   'files': [],
                   'subfolders': [{'name': 'M', 'files': ['exists.txt'], 'subfolders': []}]}]},
  'missing.txt',
  '4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945',
  False),
 ({'name': 'Main',
   'files': [],
   'subfolders': [{'name': 'Section0', 'files': ['filler0.txt'], 'subfolders': []},
                  {'name': 'Section1', 'files': ['filler1.txt'], 'subfolders': []},
                  {'name': 'Section2', 'files': ['filler2.txt'], 'subfolders': []},
                  {'name': 'Section3', 'files': ['filler3.txt'], 'subfolders': []},
                  {'name': 'Section4', 'files': ['filler4.txt'], 'subfolders': []},
                  {'name': 'Section5', 'files': ['filler5.txt'], 'subfolders': []},
                  {'name': 'Section6', 'files': ['filler6.txt'], 'subfolders': []},
                  {'name': 'Section7', 'files': ['filler7.txt'], 'subfolders': []},
                  {'name': 'Section8', 'files': ['filler8.txt'], 'subfolders': []},
                  {'name': 'Section9', 'files': ['filler9.txt'], 'subfolders': []},
                  {'name': 'Section10', 'files': ['filler10.txt'], 'subfolders': []},
                  {'name': 'Section11', 'files': ['filler11.txt'], 'subfolders': []},
                  {'name': 'Last', 'files': ['found.xlsx'], 'subfolders': []}]},
  'found.xlsx',
  '7694c11b8690f688192a69267c3f245e8c141b494b5704df624f08418a462d12',
  False),
 ({'name': 'Root',
   'files': [],
   'subfolders': [{'name': 'Notes', 'files': ['first.txt'], 'subfolders': []},
                  {'name': 'Notes', 'files': ['second.txt'], 'subfolders': []}]},
  'second.txt',
  'dbaebf4b59c20beb8b0b3b09731f483ad1d3cce364544b74bc322326ab1a6bcb',
  False),
 ({'name': 'Case Folder',
   'files': ['Notes.PDF'],
   'subfolders': [{'name': 'Child', 'files': ['notes.pdf'], 'subfolders': []}]},
  'NOTES.PDF',
  '4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945',
  False),
 ({'name': 'Drive',
   'files': [],
   'subfolders': [{'name': 'Empty', 'files': [], 'subfolders': []},
                  {'name': 'Nested',
                   'files': [],
                   'subfolders': [{'name': 'Deep', 'files': ['file.txt'], 'subfolders': []}]}]},
  'file.txt',
  '42980492039e7d5e8065506645a16d1be743d25875d91a6e4d41e9498a85eb79',
  False),
 ({'name': 'Root',
   'files': ['z.txt'],
   'subfolders': [{'name': 'A', 'files': ['a.txt'], 'subfolders': []},
                  {'name': 'B', 'files': [], 'subfolders': [{'name': 'C', 'files': ['c.txt'], 'subfolders': []}]}]},
  'a.txt',
  '748802a2ecb32156ef45e14922714af9cc475b0713eea63a4e3c56579bf82a0d',
  False)]


@pytest.mark.parametrize("folder,filename,expected,is_visible", q10_testcases)
def test_q10(folder, filename, expected, is_visible):
    original = copy.deepcopy(folder)
    working_folder = copy.deepcopy(folder)
    result = find_file(working_folder, filename)
    assert type(result) is list
    assert all(type(entry) is str for entry in result)
    assert working_folder == original
    if is_visible:
        assert result == expected
    else:
        assert hashcode(result) == expected
