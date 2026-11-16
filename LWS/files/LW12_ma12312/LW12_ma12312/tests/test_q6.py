import hashlib
import json
import os
import sys

import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from q6 import create_lughat


def hashcode(dictionary):
    serialized = json.dumps(dictionary, sort_keys=True, separators=(',', ':'), ensure_ascii=True)
    return hashlib.sha256(serialized.encode('utf-8')).hexdigest()


q6_testcases = [
    (['Python is a widely used language for general purpose programming, created in 1991.',
 'The goal of this book is to think like a computer scientist.',
 'The single most important skill for a computer scientist is problem solving. Problem solving '
 'means the ability to formulate problems.'],
     {'a': {'p1': {'a': 1}, 'p2': {'a': 1}, 'p3': {'a': 1, 'ability': 1}},
 'b': {'p2': {'book': 1}},
 'c': {'p1': {'created': 1}, 'p2': {'computer': 1}, 'p3': {'computer': 1}},
 'f': {'p1': {'for': 1}, 'p3': {'for': 1, 'formulate': 1}},
 'g': {'p1': {'general': 1}, 'p2': {'goal': 1}},
 'i': {'p1': {'in': 1, 'is': 1}, 'p2': {'is': 1}, 'p3': {'important': 1, 'is': 1}},
 'l': {'p1': {'language': 1}, 'p2': {'like': 1}},
 'm': {'p3': {'means': 1, 'most': 1}},
 'o': {'p2': {'of': 1}},
 'p': {'p1': {'programming': 1, 'purpose': 1, 'python': 1}, 'p3': {'problem': 2, 'problems': 1}},
 's': {'p2': {'scientist': 1}, 'p3': {'scientist': 1, 'single': 1, 'skill': 1, 'solving': 2}},
 't': {'p2': {'the': 1, 'think': 1, 'this': 1, 'to': 1}, 'p3': {'the': 2, 'to': 1}},
 'u': {'p1': {'used': 1}},
 'w': {'p1': {'widely': 1}}}, True),
    ([],
     {}, True),
    (['', "Don't stop; well-known."],
     {'d': {'p2': {'don': 1}},
 'k': {'p2': {'known': 1}},
 's': {'p2': {'stop': 1}},
 't': {'p2': {'t': 1}},
 'w': {'p2': {'well': 1}}}, True),
    (['Python is a widely used high level programming language for general purpose programming, created '
 'by Guido van Rossum and first released in 1991. An interpreted language, Python has a design '
 'philosophy that emphasizes code readability (notably using whitespace indentation to delimit '
 'code blocks rather than curly brackets or keywords), and a syntax that allows programmers to '
 'express concepts in fewer lines of code than might be used in languages such as Fortran or Java. '
 'It provides constructs that enable clear programming on both small and large scales.',
 'The goal of this book is to teach you to think like a computer scientist. This way of thinking '
 'combines some of the best features of mathematics, engineering, and natural science. Like '
 'mathematicians, computer scientists use formal languages to denote ideas (specifically '
 'computations). Like engineers, they design things, assembling components into systems and '
 'evaluating tradeoffs among alternatives. Like scientists, they observe the behavior of complex '
 'systems, form hypotheses, and test predictions.',
 'The single most important skill for a computer scientist is problem solving. Problem solving '
 'means the ability to formulate problems, think creatively about solutions, and express a '
 'solution clearly and accurately. As it turns out, the process of learning to program is an '
 'excellent opportunity to practice problem solving skills. That is why this chapter is called, '
 '"The way of the program".'],
     {'a': {'p1': {'a': 3, 'allows': 1, 'an': 1, 'and': 3, 'as': 1},
       'p2': {'a': 1, 'alternatives': 1, 'among': 1, 'and': 3, 'assembling': 1},
       'p3': {'a': 2, 'ability': 1, 'about': 1, 'accurately': 1, 'an': 1, 'and': 2, 'as': 1}},
 'b': {'p1': {'be': 1, 'blocks': 1, 'both': 1, 'brackets': 1, 'by': 1},
       'p2': {'behavior': 1, 'best': 1, 'book': 1}},
 'c': {'p1': {'clear': 1, 'code': 3, 'concepts': 1, 'constructs': 1, 'created': 1, 'curly': 1},
       'p2': {'combines': 1, 'complex': 1, 'components': 1, 'computations': 1, 'computer': 2},
       'p3': {'called': 1, 'chapter': 1, 'clearly': 1, 'computer': 1, 'creatively': 1}},
 'd': {'p1': {'delimit': 1, 'design': 1}, 'p2': {'denote': 1, 'design': 1}},
 'e': {'p1': {'emphasizes': 1, 'enable': 1, 'express': 1},
       'p2': {'engineering': 1, 'engineers': 1, 'evaluating': 1},
       'p3': {'excellent': 1, 'express': 1}},
 'f': {'p1': {'fewer': 1, 'first': 1, 'for': 1, 'fortran': 1},
       'p2': {'features': 1, 'form': 1, 'formal': 1},
       'p3': {'for': 1, 'formulate': 1}},
 'g': {'p1': {'general': 1, 'guido': 1}, 'p2': {'goal': 1}},
 'h': {'p1': {'has': 1, 'high': 1}, 'p2': {'hypotheses': 1}},
 'i': {'p1': {'in': 3, 'indentation': 1, 'interpreted': 1, 'is': 1, 'it': 1},
       'p2': {'ideas': 1, 'into': 1, 'is': 1},
       'p3': {'important': 1, 'is': 4, 'it': 1}},
 'j': {'p1': {'java': 1}},
 'k': {'p1': {'keywords': 1}},
 'l': {'p1': {'language': 2, 'languages': 1, 'large': 1, 'level': 1, 'lines': 1},
       'p2': {'languages': 1, 'like': 4},
       'p3': {'learning': 1}},
 'm': {'p1': {'might': 1},
       'p2': {'mathematicians': 1, 'mathematics': 1},
       'p3': {'means': 1, 'most': 1}},
 'n': {'p1': {'notably': 1}, 'p2': {'natural': 1}},
 'o': {'p1': {'of': 1, 'on': 1, 'or': 2},
       'p2': {'observe': 1, 'of': 5},
       'p3': {'of': 2, 'opportunity': 1, 'out': 1}},
 'p': {'p1': {'philosophy': 1,
              'programmers': 1,
              'programming': 3,
              'provides': 1,
              'purpose': 1,
              'python': 2},
       'p2': {'predictions': 1},
       'p3': {'practice': 1, 'problem': 3, 'problems': 1, 'process': 1, 'program': 2}},
 'r': {'p1': {'rather': 1, 'readability': 1, 'released': 1, 'rossum': 1}},
 's': {'p1': {'scales': 1, 'small': 1, 'such': 1, 'syntax': 1},
       'p2': {'science': 1,
              'scientist': 1,
              'scientists': 2,
              'some': 1,
              'specifically': 1,
              'systems': 2},
       'p3': {'scientist': 1,
              'single': 1,
              'skill': 1,
              'skills': 1,
              'solution': 1,
              'solutions': 1,
              'solving': 3}},
 't': {'p1': {'than': 2, 'that': 3, 'to': 2},
       'p2': {'teach': 1,
              'test': 1,
              'the': 3,
              'they': 2,
              'things': 1,
              'think': 1,
              'thinking': 1,
              'this': 2,
              'to': 3,
              'tradeoffs': 1},
       'p3': {'that': 1, 'the': 5, 'think': 1, 'this': 1, 'to': 3, 'turns': 1}},
 'u': {'p1': {'used': 2, 'using': 1}, 'p2': {'use': 1}},
 'v': {'p1': {'van': 1}},
 'w': {'p1': {'whitespace': 1, 'widely': 1}, 'p2': {'way': 1}, 'p3': {'way': 1, 'why': 1}},
 'y': {'p2': {'you': 1}}}, True),
    ([''],
     '44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a', False),
    (['---', '12345', '!!!'],
     '44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a', False),
    (['Alpha beta alpha', 'beta ALPHA', 'alpha'],
     '52d7fb680e45cb023f8a32bd83aa97252edadbebb35062d8a024a30969bba1c2', False),
    (['', '2024', 'zebra!', '', 'zebra zebra'],
     '62ac9a1474d5617e56f8bc64910d40d538898dd1007508d2fc0dfffa3184d5de', False),
    (["Don't well-known e-mail 42C++"],
     '858bd596b978d325a004d7bf83fb0c290b6ad844e51810a13691f218ad85bea7', False),
    (['A a a A', 'a', 'B b', ''],
     '0f77d172756f1d83af809c6aaa43c1b0ead6f3088e55f4e04575cb9c1a20c82e', False),
    (['one1two 99B3C', 'one-two three_4_four'],
     '1459e6e17e06dc97c101c17d4c2c06f170568614e3b5c40f3ac55a0e26815e9c', False),
    (['\tPython\nPYTHON\t data', 'data\tDATA', 'Data science'],
     'bfb5bad5a9d79e55fa0a8d78cacb2a8afec5d27d35a2f6e6996293ee8884a303', False),
    (['', '', '', '', '', '', '', '', '', 'One ONE'],
     '49433e083ab30d7607b863cf04245dce1f68a723220bd25b3cdbdfa8aeea84e5', False),
    (['z Z y Y abc ABC', 'abcxyz abcxyz', 'zebra zebra'],
     '4b682631ef537861034f79b14fc3643511f1f855c47dad888adb4681b0db3fdd', False),
    (['a1b2c __top__ bottom', 'HELLO,world;hello', '123x456', ''],
     'c52d6fabd2b26b2202b1e7ba2443c2b0d6c84d4b0a6d769cbe2429439859d105', False),
]


@pytest.mark.parametrize("paragraphs, expected, visible", q6_testcases)
def test_q6(paragraphs, expected, visible):
    result = create_lughat(paragraphs)
    assert isinstance(result, dict), "The function must return a dictionary."
    for letter, paragraph_entries in result.items():
        assert isinstance(letter, str) and len(letter) == 1 and 'a' <= letter <= 'z'
        assert isinstance(paragraph_entries, dict) and paragraph_entries
        for paragraph_id, word_counts in paragraph_entries.items():
            assert isinstance(paragraph_id, str) and paragraph_id.startswith('p')
            assert isinstance(word_counts, dict) and word_counts
            for word, count in word_counts.items():
                assert isinstance(word, str) and word and word[0] == letter
                assert word.isascii() and word.isalpha() and word.islower()
                assert type(count) is int and count > 0
    if visible:
        assert result == expected
    else:
        assert hashcode(result) == expected
