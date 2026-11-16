import hashlib
import os
import sys

import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from q1 import count_words


def hashcode(text):
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


q1_testcases = [
    ('The high-level language Python (1991) is fun, and C++ is fun too! The end.',
     '1991 = 1\nand = 1\nc = 1\nend = 1\nfun = 2\nhighlevel = 1\nis = 2\nlanguage = 1\npython = 1\nthe = 2\ntoo = 1', True),
    ('-- !!!',
     '', True),
    ('Python is a widely used high-level programming language for general-purpose programming, created by Guido van Rossum and first released in 1991. An interpreted language, Python has a design philosophy that emphasizes code readability (notably using whitespace indentation to delimit code blocks rather than curly brackets or keywords), and a syntax that allows programmers to express concepts in fewer lines of code than might be used in languages such as C++ or Java. It provides constructs that enable clear programming on both small and large scales.',
     '1991 = 1\na = 3\nallows = 1\nan = 1\nand = 3\nas = 1\nbe = 1\nblocks = 1\nboth = 1\nbrackets = 1\nby = 1\nc = 1\nclear = 1\ncode = 3\nconcepts = 1\nconstructs = 1\ncreated = 1\ncurly = 1\ndelimit = 1\ndesign = 1\nemphasizes = 1\nenable = 1\nexpress = 1\nfewer = 1\nfirst = 1\nfor = 1\ngeneralpurpose = 1\nguido = 1\nhas = 1\nhighlevel = 1\nin = 3\nindentation = 1\ninterpreted = 1\nis = 1\nit = 1\njava = 1\nkeywords = 1\nlanguage = 2\nlanguages = 1\nlarge = 1\nlines = 1\nmight = 1\nnotably = 1\nof = 1\non = 1\nor = 2\nphilosophy = 1\nprogrammers = 1\nprogramming = 3\nprovides = 1\npython = 2\nrather = 1\nreadability = 1\nreleased = 1\nrossum = 1\nscales = 1\nsmall = 1\nsuch = 1\nsyntax = 1\nthan = 2\nthat = 3\nto = 2\nused = 2\nusing = 1\nvan = 1\nwhitespace = 1\nwidely = 1', True),
    ('The goal of this book is to teach you to think like a computer scientist. This way of thinking combines some of the best features of mathematics, engineering, and natural science. Like mathematicians, computer scientists use formal languages to denote ideas (specifically computations). Like engineers, they design things, assembling components into systems and evaluating tradeoffs among alternatives. Like scientists, they observe the behavior of complex systems, form hypotheses, and test predictions.',
     'a = 1\nalternatives = 1\namong = 1\nand = 3\nassembling = 1\nbehavior = 1\nbest = 1\nbook = 1\ncombines = 1\ncomplex = 1\ncomponents = 1\ncomputations = 1\ncomputer = 2\ndenote = 1\ndesign = 1\nengineering = 1\nengineers = 1\nevaluating = 1\nfeatures = 1\nform = 1\nformal = 1\ngoal = 1\nhypotheses = 1\nideas = 1\ninto = 1\nis = 1\nlanguages = 1\nlike = 4\nmathematicians = 1\nmathematics = 1\nnatural = 1\nobserve = 1\nof = 5\npredictions = 1\nscience = 1\nscientist = 1\nscientists = 2\nsome = 1\nspecifically = 1\nsystems = 2\nteach = 1\ntest = 1\nthe = 3\nthey = 2\nthings = 1\nthink = 1\nthinking = 1\nthis = 2\nto = 3\ntradeoffs = 1\nuse = 1\nway = 1\nyou = 1', True),
    ('The single most important skill for a computer scientist is problem solving. Problem solving means the ability to formulate problems, think creatively about solutions, and express a solution clearly and accurately. As it turns out, the process of learning to program is an excellent opportunity to practice problem-solving skills. That\'s why this chapter is called, "The way of the program".',
     'a = 2\nability = 1\nabout = 1\naccurately = 1\nan = 1\nand = 2\nas = 1\ncalled = 1\nchapter = 1\nclearly = 1\ncomputer = 1\ncreatively = 1\nexcellent = 1\nexpress = 1\nfor = 1\nformulate = 1\nimportant = 1\nis = 3\nit = 1\nlearning = 1\nmeans = 1\nmost = 1\nof = 2\nopportunity = 1\nout = 1\npractice = 1\nproblem = 2\nproblems = 1\nproblemsolving = 1\nprocess = 1\nprogram = 2\nscientist = 1\nsingle = 1\nskill = 1\nskills = 1\nsolution = 1\nsolutions = 1\nsolving = 2\nthats = 1\nthe = 5\nthink = 1\nthis = 1\nto = 3\nturns = 1\nway = 1\nwhy = 1', True),
    ('',
     'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855', False),
    ('Apple apple APPLE banana BANANA',
     '292327769ac048a047613377fc7c8c11fa788f99cc830dee41a5666848acb505', False),
    ('1991 2024 1991! x2 X2',
     'd0db3f301b9152bdefde4978dc989352cd4ed2ce711142055b0716ed066cb75f', False),
    ("well-known can't C++ e-mail",
     '835318f711870abc15f630802af509358bd73fb1589711b8bf4535863526630d', False),
    ('foo, foo! bar? Foo.',
     'f5ee39dbcd0f8a16d4743097cd04ab44a5e8e23642d764e23e83f4f325b047c2', False),
    ('z zebra 2 10 apple',
     '3fcecc6b57794c1ede57a5215c63f2995f57c0684404a63bc6b72be7d9f097dd', False),
    ('((Hello)) [world]! /hello/',
     '01c4cdeafc2945dd0cff5ec3cc07b220ac98d76c1431e187331950528d3a00c5', False),
    ('a-b c_d m/n',
     'fe4213653604b26dfe345a1a5e34c111fa2f4d3e553474dbf8b26f6e5cece8a3', False),
    ('one\ttwo\nONE  two',
     '212be269b8c86207c42cb8c7306d9e1e91b679eaf597d43427a3a1f4f817b5ff', False),
    ('#tag @tag code#1 code_1',
     '0b52d53e125ddc51f6f60d2dd545f487b4744061054db69d0669dba0e4d47e1f', False),
]


@pytest.mark.parametrize("text, expected, visible", q1_testcases)
def test_q1(capsys, text, expected, visible):
    count_words(text)
    captured = capsys.readouterr()

    if visible:
        assert captured.out == expected + ("\n" if expected else "")
    else:
        assert hashcode(captured.out) == expected