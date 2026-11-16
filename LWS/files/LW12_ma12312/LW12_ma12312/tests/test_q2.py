import hashlib
import os
import sys

import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from q2 import most_prolific_authors


def hashcode(text):
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


q2_testcases = [
    ([{'title': 'C++ How to Program', 'author': 'Harvey Deitel', 'year': 1994},
 {'title': 'Introduction to Algorithms', 'author': 'Charles E. Leiserson', 'year': 1989},
 {'title': 'C# for Programmers', 'author': 'Harvey Deitel', 'year': 2008},
 {'title': 'Code Complete', 'author': 'Steve McConnell', 'year': 1993}],
     'Harvey Deitel', True),
    ([{'title': 'Advanced Research in VLSI', 'author': 'Charles E. Leiserson', 'year': 1986},
 {'title': 'C++ How to Program', 'author': 'Harvey Deitel', 'year': 1994},
 {'title': 'Introduction to Algorithms', 'author': 'Charles E. Leiserson', 'year': 1989},
 {'title': 'C# for Programmers', 'author': 'Harvey Deitel', 'year': 2008},
 {'title': 'Code Complete', 'author': 'Steve McConnell', 'year': 1993}],
     'Charles E. Leiserson, Harvey Deitel', True),
    ([{'title': 'C++ How to Program', 'author': 'Harvey Deitel', 'year': 1994},
 {'title': 'Introduction to Algorithms', 'author': 'Charles E. Leiserson', 'year': 1989},
 {'title': 'Code Complete', 'author': 'Steve McConnell', 'year': 1993},
 {'title': 'Python Code Complete', 'author': 'Steve McConnell', 'year': 1998},
 {'title': 'JavaScript for Programmers', 'author': 'Harvey Deitel', 'year': 2009},
 {'title': 'Advanced Research in VLSI', 'author': 'Charles E. Leiserson', 'year': 1986}],
     'f709fcbfa93dcddc0ead30375f7c1464b949300915c4981920936b23839b43b1', False),
    ([{'title': 'Book 1', 'author': 'Zara Malik', 'year': 2024}],
     'd3e9ad2202b55d45f3cc04ca9a8b130f6c375747368cf5f1aa06c1daf097b919', False),
    ([{'title': 'Book 1', 'author': 'Ayesha Khan', 'year': 1990},
 {'title': 'Book 2', 'author': 'Ayesha Khan', 'year': 2001},
 {'title': 'Book 3', 'author': 'Ayesha Khan', 'year': 2015},
 {'title': 'Book 4', 'author': 'Ayesha Khan', 'year': 2026}],
     '3ef1b3d3148b9b57aded86e151367725ece04c0219f76de67b5aab048bcbb9d5', False),
    ([{'title': 'Book 1', 'author': 'Zoya', 'year': 2010},
 {'title': 'Book 2', 'author': 'Ali', 'year': 2011},
 {'title': 'Book 3', 'author': 'Bilal', 'year': 2012},
 {'title': 'Book 4', 'author': 'Hira', 'year': 2013}],
     'da4fe81c5b44f56e7b300b721663a97bea98d1da4104adb2df8de71d5f50b905', False),
    ([{'title': 'Book 1', 'author': 'Mina', 'year': 2001},
 {'title': 'Book 2', 'author': 'Zara', 'year': 2002},
 {'title': 'Book 3', 'author': 'Mina', 'year': 2003},
 {'title': 'Book 4', 'author': 'Zara', 'year': 2004},
 {'title': 'Book 5', 'author': 'Sana', 'year': 2005},
 {'title': 'Book 6', 'author': 'Sana', 'year': 2006},
 {'title': 'Book 7', 'author': 'Mina', 'year': 2007},
 {'title': 'Book 8', 'author': 'Zara', 'year': 2008},
 {'title': 'Book 9', 'author': 'Rida', 'year': 2009}],
     'dd3788ae4a86aee5b832dc19d149b3436df5c3545df8a02a7fa3d7af008ae453', False),
    ([{'title': 'Book 1', 'author': 'Ali', 'year': 2020},
 {'title': 'Book 2', 'author': 'ali', 'year': 2021},
 {'title': 'Book 3', 'author': 'ALI', 'year': 2022},
 {'title': 'Book 4', 'author': 'ali', 'year': 2023},
 {'title': 'Book 5', 'author': 'Ali', 'year': 2024}],
     '3ed641381327649afd5f13aa9156014b9281ccc096fe1d324410c9528f43635b', False),
    ([{'title': 'Book 1', 'author': 'Dr. Z', 'year': 1901},
 {'title': 'Book 2', 'author': 'Anne-Marie', 'year': 2020},
 {'title': 'Book 3', 'author': 'A. Khan', 'year': 2000},
 {'title': 'Book 4', 'author': 'Anne-Marie', 'year': 2020},
 {'title': 'Book 5', 'author': 'A. Khan', 'year': 1999},
 {'title': 'Book 6', 'author': 'Dr. Z', 'year': 2025}],
     'e3c16c62f49c6caa8365f8b200e48c63d6a3f5e75a096d6565215dcbc9125386', False),
    ([{'title': 'Same Title', 'author': 'Nida', 'year': 2000},
 {'title': 'Same Title', 'author': 'Nida', 'year': 2000},
 {'title': 'Different Title', 'author': 'Hadi', 'year': 2005}],
     'a39838f326d62bb7b8337cd7be7c358af400bcaad844842382b7259260c013fe', False),
    ([{'title': 'Book 1', 'author': 'R', 'year': 2012},
 {'title': 'Book 2', 'author': 'Q', 'year': 2013},
 {'title': 'Book 3', 'author': 'P', 'year': 2014},
 {'title': 'Book 4', 'author': 'Q', 'year': 2015},
 {'title': 'Book 5', 'author': 'P', 'year': 2016},
 {'title': 'Book 6', 'author': 'R', 'year': 2017},
 {'title': 'Book 7', 'author': 'P', 'year': 2018},
 {'title': 'Book 8', 'author': 'Q', 'year': 2019},
 {'title': 'Book 9', 'author': 'R', 'year': 2020},
 {'title': 'Book 10', 'author': 'S', 'year': 2021}],
     'a2a8bfff6d1b973f8412bb797b4da907d5d98538619891e54e5d099c79bcf8a2', False),
    ([{'title': 'Book 1', 'author': 'B', 'year': 2021},
 {'title': 'Book 2', 'author': 'b', 'year': 2021},
 {'title': 'Book 3', 'author': 'B', 'year': 2021},
 {'title': 'Book 4', 'author': 'b', 'year': 2021},
 {'title': 'Book 5', 'author': 'A', 'year': 2021},
 {'title': 'Book 6', 'author': 'a', 'year': 2021},
 {'title': 'Book 7', 'author': 'A', 'year': 2021}],
     '94ea04e268390b9abd34096d9cbc5140adb81b0ad27c14833025d2c2a4c20dec', False),
    ([{'title': 'Book 1', 'author': 'Fahad', 'year': 2026},
 {'title': 'Book 2', 'author': 'Sara', 'year': 2024},
 {'title': 'Book 3', 'author': 'Fahad', 'year': 2023},
 {'title': 'Book 4', 'author': 'Sara', 'year': 2021},
 {'title': 'Book 5', 'author': 'Sara', 'year': 2020},
 {'title': 'Book 6', 'author': 'Fahad', 'year': 2019},
 {'title': 'Book 7', 'author': 'Amina', 'year': 2018},
 {'title': 'Book 8', 'author': 'Sara', 'year': 2017},
 {'title': 'Book 9', 'author': 'Amina', 'year': 2016},
 {'title': 'Book 10', 'author': 'Sara', 'year': 2015}],
     '53b1fb446230b347c3f6406cca4b1ddbac60905ba4ab1977179f44b8fb134447', False),
    ([{'title': 'Book 1', 'author': 'Zaid', 'year': 2010},
 {'title': 'Book 2', 'author': 'Anas', 'year': 2011},
 {'title': 'Book 3', 'author': 'Zaid', 'year': 2012},
 {'title': 'Book 4', 'author': 'Anas', 'year': 2013},
 {'title': 'Book 5', 'author': 'Hiba', 'year': 2014}],
     'd2910a2f3b8ec2c93f95eec21ae29ce1b7f85b6c2380e59064476b79fe1cbc4f', False),
    ([{'title': 'Book 1', 'author': 'Hana', 'year': 2010},
 {'title': 'Book 2', 'author': 'Hana', 'year': 2011},
 {'title': 'Book 3', 'author': 'Hana', 'year': 2012},
 {'title': 'Book 4', 'author': 'Rafi', 'year': 2013},
 {'title': 'Book 5', 'author': 'Rafi', 'year': 2014},
 {'title': 'Book 6', 'author': 'Zain', 'year': 2015}],
     '78b5b5558f2c83de7c6e3986ec7b948b7d2a973360c5ac8b5870f4dd702b8fa8', False),
]


@pytest.mark.parametrize("books, expected, visible", q2_testcases)
def test_q2(books, expected, visible):
    result = most_prolific_authors(books)
    if visible:
        assert result == expected
    else:
        assert hashcode(str(result)) == expected
