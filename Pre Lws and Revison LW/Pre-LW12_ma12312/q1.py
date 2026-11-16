def count_words(text):
    # WRITE YOUR CODE HERE
    text = text.lower()
    text = text.split()
    text = sorted(text)

    freq = {}
    lst = []
    
    var = '!@#$%^&*()+=-_{}[];:"\'|/?><.,'
    for i in range(len(text)):
        string = ''
        for j in range(len(text[i])):
            if text[i][j] not in var:
                string += text[i][j]
        if string != '':
            lst.append(string)

    lst = sorted(lst)


    for i in range(len(lst)):
        if lst[i] not in freq:
            freq[lst[i]] = 1
        else:
            freq[lst[i]] += 1

    for key,value in freq.items():
        print(f"{key} = {value}")

# -----------------------------------------#
# TESTING YOUR CODE                        #
# -----------------------------------------#
# The code below runs only when this file is executed directly.
if __name__ == "__main__":

    # ----------------------------------------------#
    # TESTING YOUR CODE ON VISIBLE TEST CASES       #
    # Run this file and manually check whether      #
    # your function produces the expected output.   #
    # ----------------------------------------------#

    count_words('The high-level language Python (1991) is fun, and C++ is fun too! The end.')
    # Should print:
    # 1991 = 1
    # and = 1
    # c = 1
    # end = 1
    # fun = 2
    # highlevel = 1
    # is = 2
    # language = 1
    # python = 1
    # the = 2
    # too = 1

    print()

    count_words('-- !!!')
    # Should print nothing.

    print()

    count_words(
        'Python is a widely used high-level programming language for general-purpose '
        'programming, created by Guido van Rossum and first released in 1991. An '
        'interpreted language, Python has a design philosophy that emphasizes code '
        'readability (notably using whitespace indentation to delimit code blocks '
        'rather than curly brackets or keywords), and a syntax that allows '
        'programmers to express concepts in fewer lines of code than might be used '
        'in languages such as C++ or Java. It provides constructs that enable clear '
        'programming on both small and large scales.'
    )
    # Should print:
    # 1991 = 1
    # a = 3
    # allows = 1
    # an = 1
    # and = 3
    # as = 1
    # be = 1
    # blocks = 1
    # both = 1
    # brackets = 1
    # by = 1
    # c = 1
    # clear = 1
    # code = 3
    # concepts = 1
    # constructs = 1
    # created = 1
    # curly = 1
    # delimit = 1
    # design = 1
    # emphasizes = 1
    # enable = 1
    # express = 1
    # fewer = 1
    # first = 1
    # for = 1
    # generalpurpose = 1
    # guido = 1
    # has = 1
    # highlevel = 1
    # in = 3
    # indentation = 1
    # interpreted = 1
    # is = 1
    # it = 1
    # java = 1
    # keywords = 1
    # language = 2
    # languages = 1
    # large = 1
    # lines = 1
    # might = 1
    # notably = 1
    # of = 1
    # on = 1
    # or = 2
    # philosophy = 1
    # programmers = 1
    # programming = 3
    # provides = 1
    # python = 2
    # rather = 1
    # readability = 1
    # released = 1
    # rossum = 1
    # scales = 1
    # small = 1
    # such = 1
    # syntax = 1
    # than = 2
    # that = 3
    # to = 2
    # used = 2
    # using = 1
    # van = 1
    # whitespace = 1
    # widely = 1

    print()

    count_words(
        'The goal of this book is to teach you to think like a computer scientist. '
        'This way of thinking combines some of the best features of mathematics, '
        'engineering, and natural science. Like mathematicians, computer scientists '
        'use formal languages to denote ideas (specifically computations). Like '
        'engineers, they design things, assembling components into systems and '
        'evaluating tradeoffs among alternatives. Like scientists, they observe the '
        'behavior of complex systems, form hypotheses, and test predictions.'
    )
    # Should print:
    # a = 1
    # alternatives = 1
    # among = 1
    # and = 3
    # assembling = 1
    # behavior = 1
    # best = 1
    # book = 1
    # combines = 1
    # complex = 1
    # components = 1
    # computations = 1
    # computer = 2
    # denote = 1
    # design = 1
    # engineering = 1
    # engineers = 1
    # evaluating = 1
    # features = 1
    # form = 1
    # formal = 1
    # goal = 1
    # hypotheses = 1
    # ideas = 1
    # into = 1
    # is = 1
    # languages = 1
    # like = 4
    # mathematicians = 1
    # mathematics = 1
    # natural = 1
    # observe = 1
    # of = 5
    # predictions = 1
    # science = 1
    # scientist = 1
    # scientists = 2
    # some = 1
    # specifically = 1
    # systems = 2
    # teach = 1
    # test = 1
    # the = 3
    # they = 2
    # things = 1
    # think = 1
    # thinking = 1
    # this = 2
    # to = 3
    # tradeoffs = 1
    # use = 1
    # way = 1
    # you = 1

    print()

    count_words(
        'The single most important skill for a computer scientist is problem '
        'solving. Problem solving means the ability to formulate problems, think '
        'creatively about solutions, and express a solution clearly and accurately. '
        'As it turns out, the process of learning to program is an excellent '
        "opportunity to practice problem-solving skills. That's why this chapter is "
        'called, "The way of the program".'
    )
    # Should print:
    # a = 2
    # ability = 1
    # about = 1
    # accurately = 1
    # an = 1
    # and = 2
    # as = 1
    # called = 1
    # chapter = 1
    # clearly = 1
    # computer = 1
    # creatively = 1
    # excellent = 1
    # express = 1
    # for = 1
    # formulate = 1
    # important = 1
    # is = 3
    # it = 1
    # learning = 1
    # means = 1
    # most = 1
    # of = 2
    # opportunity = 1
    # out = 1
    # practice = 1
    # problem = 2
    # problems = 1
    # problemsolving = 1
    # process = 1
    # program = 2
    # scientist = 1
    # single = 1
    # skill = 1
    # skills = 1
    # solution = 1
    # solutions = 1
    # solving = 2
    # thats = 1
    # the = 5
    # think = 1
    # this = 1
    # to = 3
    # turns = 1
    # way = 1
    # why = 1

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#



# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your function, type one of the following commands in the terminal:
# python -m pytest tests/test_q1.py
# python3 -m pytest tests/test_q1.py