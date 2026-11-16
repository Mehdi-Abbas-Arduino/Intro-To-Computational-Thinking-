import hashlib
import os
import sys

import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from q3 import merge_by_value
from helper_for_formatting_dont_delete import dictFormatting


def hashcode(text):
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


q3_testcases = [
    ({101: 'Python Basics', 102: 'Data Structures', 103: 'Python Basics'},
     {201: 'Data Structures', 202: 'Algorithms', 203: 'Python Basics'},
     {'Algorithms': [202], 'Data Structures': [102, 201], 'Python Basics': [101, 103, 203]}, True),
    ({1101: 'Python Basics', 1102: 'Database Systems', 1103: 'Algorithms'},
     {2201: 'Algorithms', 2202: 'Python Basics', 2203: 'Database Systems'},
     {'Algorithms': [1103, 2201], 'Database Systems': [1102, 2203], 'Python Basics': [1101, 2202]}, True),
    ({1104: 'Physics Fundamentals', 1105: 'World History', 1106: 'Calculus I'},
     {2204: 'Physics Fundamentals'},
     {'Calculus I': [1106], 'Physics Fundamentals': [1104, 2204], 'World History': [1105]}, True),
    ({1107: 'Modern Literature', 1108: 'Biology Essentials', 1109: 'Modern Literature'},
     {},
     {'Biology Essentials': [1108], 'Modern Literature': [1107, 1109]}, True),
    ({1110: 'Discrete Mathematics', 1111: 'Organic Chemistry'},
     {2210: 'Art History', 2211: 'Computer Networks'},
     {'Art History': [2210], 'Computer Networks': [2211], 'Discrete Mathematics': [1110], 'Organic Chemistry': [1111]}, True),
    ({},
     {},
     {}, True),
    ({1112: 'Introduction to Python', 1113: 'Data Structures', 1114: 'Introduction to Python'},
     {2212: 'Data Structures', 2213: 'Introduction to Python', 2214: 'Data Structures'},
     {'Data Structures': [1113, 2212, 2214], 'Introduction to Python': [1112, 1114, 2213]}, True),
    ({},
     {2220: 'Poetry Collection', 2222: 'Poetry Collection', 2221: 'Drama Anthology'},
     '282a2fe4f07330b87dfd49af7eac27e12f3c9817b76f10dfed5e80850a36c54e', False),
    ({1120: 'Artificial Intelligence'},
     {},
     'ce6ff20f7f9b232c7f48b7e7519f9455731ccca1aa13e2f43a74c9551862303f', False),
    ({1121: 'Data Science', 1123: 'Data Science', 1122: 'Machine Learning'},
     {2223: 'Machine Learning', 2221: 'Data Science', 2222: 'Machine Learning'},
     'f002cb26d0dd7f9a97060dc35315128a000354b6908b641ab822152b2bdf99a9', False),
    ({1124: 'Python Basics', 1125: 'Advanced Python'},
     {2224: 'Python Basics', 2225: 'Python for Data Analysis'},
     '43a8670b36eabf6ba22cbb50da59fd7f25c05eaa05384b1b4524de2b55ec25ed', False),
    ({1126: 'C++ Primer', 1127: 'Python 3'},
     {2226: 'C++ Primer', 2227: 'Python 3'},
     'dbb02a0b808c186487250f7c89ff5501e7f58fe165597669f94655090369d97e', False),
    ({1180: 'World History', 1160: 'Calculus I', 1170: 'Computer Networks'},
     {2280: 'Computer Networks', 2260: 'World History', 2270: 'Calculus I'},
     'b099d3c83aa6677a929f24b1b9c38e5abc268d8920ae7a3897356aa9d6c9b526', False),
    ({1130: 'Chemistry Essentials', 1131: 'Chemistry Essentials'},
     {2230: 'Chemistry Essentials', 2231: 'Chemistry Essentials'},
     'b5e065d6dcaa88a2043f0ee89ec82e68f09beb7e0be856f4111200b8a404a261', False),
    ({1300: 'Biology Essentials', 1301: 'Applied Statistics', 1302: 'Modern Literature', 1303: 'Physics Fundamentals', 1304: 'Biology Essentials', 1305: 'Applied Statistics', 1306: 'Modern Literature', 1307: 'Physics Fundamentals', 1308: 'Biology Essentials', 1309: 'Applied Statistics', 1310: 'Modern Literature', 1311: 'Physics Fundamentals', 1312: 'Biology Essentials', 1313: 'Applied Statistics', 1314: 'Modern Literature', 1315: 'Physics Fundamentals'},
     {2300: 'Biology Essentials', 2301: 'Modern Literature', 2302: 'Database Systems', 2303: 'Biology Essentials', 2304: 'Modern Literature', 2305: 'Database Systems', 2306: 'Biology Essentials', 2307: 'Modern Literature', 2308: 'Database Systems', 2309: 'Biology Essentials', 2310: 'Modern Literature', 2311: 'Database Systems'},
     'bcd7899b7f4dd7cee082410871ea05f7bc2dfd8c47b757730841d27f8bfc640e', False),

]


@pytest.mark.parametrize("north_branch, south_branch, expected, visible", q3_testcases)
def test_q3(north_branch, south_branch, expected, visible):
    result = merge_by_value(north_branch, south_branch)
    assert isinstance(result, dict), "The function must return a dictionary."
    assert all(isinstance(barcodes, list) for barcodes in result.values()), "Each value must be a list."
    result = dictFormatting(result)
    if visible or isinstance(expected, dict):
        assert result == expected
    else:
        assert hashcode(str(result)) == expected
