import pprint

def create_lughat(text):
    # WRITE YOUR CODE HERE
    lughat = {}
    for i in range(26):
        character = chr(97 + i) 
        lughat[character] = []
        
    text = text.lower()
    text = text.split()
    text = sorted(text)
    for word in text:
        word = word.strip('.,!?";:()')
        if word:
            first_letter = word[0]
            if first_letter in lughat:
                if word not in lughat[first_letter]:    
                    lughat[first_letter].append(word)

    for key in lughat:
        lughat[key].sort()
    return lughat
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

    pprint.pprint(create_lughat('Python is fun, and a Python is easy 2024!'))
    # Should print:
    # {'a': ['a', 'and'],
    #  'b': [],
    #  'c': [],
    #  'd': [],
    #  'e': ['easy'],
    #  'f': ['fun'],
    #  'g': [],
    #  'h': [],
    #  'i': ['is'],
    #  'j': [],
    #  'k': [],
    #  'l': [],
    #  'm': [],
    #  'n': [],
    #  'o': [],
    #  'p': ['python'],
    #  'q': [],
    #  'r': [],
    #  's': [],
    #  't': [],
    #  'u': [],
    #  'v': [],
    #  'w': [],
    #  'x': [],
    #  'y': [],
    #  'z': []}

    pprint.pprint(create_lughat(
        'Python is a widely used high level programming language for general purpose '
        'programming, created by Guido van Rossum and first released in 1991. An '
        'interpreted language, Python has a design philosophy that emphasizes code '
        'readability (notably using whitespace indentation to delimit code blocks '
        'rather than curly brackets or keywords), and a syntax that allows '
        'programmers to express concepts in fewer lines of code than might be used '
        'in languages such as Fortran or Java. It provides constructs that enable '
        'clear programming on both small and large scales.'
    ))
    # Should print:
    # {'a': ['a', 'allows', 'an', 'and', 'as'],
    #  'b': ['be', 'blocks', 'both', 'brackets', 'by'],
    #  'c': ['clear', 'code', 'concepts', 'constructs', 'created', 'curly'],
    #  'd': ['delimit', 'design'],
    #  'e': ['emphasizes', 'enable', 'express'],
    #  'f': ['fewer', 'first', 'for', 'fortran'],
    #  'g': ['general', 'guido'],
    #  'h': ['has', 'high'],
    #  'i': ['in', 'indentation', 'interpreted', 'is', 'it'],
    #  'j': ['java'],
    #  'k': ['keywords'],
    #  'l': ['language', 'languages', 'large', 'level', 'lines'],
    #  'm': ['might'],
    #  'n': ['notably'],
    #  'o': ['of', 'on', 'or'],
    #  'p': ['philosophy', 'programmers', 'programming', 'provides', 'purpose', 'python'],
    #  'q': [],
    #  'r': ['rather', 'readability', 'released', 'rossum'],
    #  's': ['scales', 'small', 'such', 'syntax'],
    #  't': ['than', 'that', 'to'],
    #  'u': ['used', 'using'],
    #  'v': ['van'],
    #  'w': ['whitespace', 'widely'],
    #  'x': [],
    #  'y': [],
    #  'z': []}

    pprint.pprint(create_lughat(
        'The goal of this book is to teach you to think like a computer scientist. '
        'This way of thinking combines some of the best features of mathematics, '
        'engineering, and natural science. Like mathematicians, computer scientists '
        'use formal languages to denote ideas (specifically computations). Like '
        'engineers, they design things, assembling components into systems and '
        'evaluating tradeoffs among alternatives. Like scientists, they observe the '
        'behavior of complex systems, form hypotheses, and test predictions.'
    ))
    # Should print:
    # {'a': ['a', 'alternatives', 'among', 'and', 'assembling'],
    #  'b': ['behavior', 'best', 'book'],
    #  'c': ['combines', 'complex', 'components', 'computations', 'computer'],
    #  'd': ['denote', 'design'],
    #  'e': ['engineering', 'engineers', 'evaluating'],
    #  'f': ['features', 'form', 'formal'],
    #  'g': ['goal'],
    #  'h': ['hypotheses'],
    #  'i': ['ideas', 'into', 'is'],
    #  'j': [],
    #  'k': [],
    #  'l': ['languages', 'like'],
    #  'm': ['mathematicians', 'mathematics'],
    #  'n': ['natural'],
    #  'o': ['observe', 'of'],
    #  'p': ['predictions'],
    #  'q': [],
    #  'r': [],
    #  's': ['science', 'scientist', 'scientists', 'some', 'specifically', 'systems'],
    #  't': ['teach',
    #        'test',
    #        'the',
    #        'they',
    #        'things',
    #        'think',
    #        'thinking',
    #        'this',
    #        'to',
    #        'tradeoffs'],
    #  'u': ['use'],
    #  'v': [],
    #  'w': ['way'],
    #  'x': [],
    #  'y': ['you'],
    #  'z': []}

    pprint.pprint(create_lughat(
        'The single most important skill for a computer scientist is problem '
        'solving. Problem solving means the ability to formulate problems, think '
        'creatively about solutions, and express a solution clearly and accurately. '
        'As it turns out, the process of learning to program is an excellent '
        'opportunity to practice problem solving skills. That is why this chapter is '
        'called, "The way of the program".'
    ))
    # Should print:
    # {'a': ['a', 'ability', 'about', 'accurately', 'an', 'and', 'as'],
    #  'b': [],
    #  'c': ['called', 'chapter', 'clearly', 'computer', 'creatively'],
    #  'd': [],
    #  'e': ['excellent', 'express'],
    #  'f': ['for', 'formulate'],
    #  'g': [],
    #  'h': [],
    #  'i': ['important', 'is', 'it'],
    #  'j': [],
    #  'k': [],
    #  'l': ['learning'],
    #  'm': ['means', 'most'],
    #  'n': [],
    #  'o': ['of', 'opportunity', 'out'],
    #  'p': ['practice', 'problem', 'problems', 'process', 'program'],
    #  'q': [],
    #  'r': [],
    #  's': ['scientist', 'single', 'skill', 'skills', 'solution', 'solutions', 'solving'],
    #  't': ['that', 'the', 'think', 'this', 'to', 'turns'],
    #  'u': [],
    #  'v': [],
    #  'w': ['way', 'why'],
    #  'x': [],
    #  'y': [],
    #  'z': []}

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#



# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your function, type one of the following commands in the terminal:
# python -m pytest tests/test_q2.py
# python3 -m pytest tests/test_q2.py