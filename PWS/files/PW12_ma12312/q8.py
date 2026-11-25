def leading_letters(corpus):
    names = []
    lis = []
    m = {}
    for i in range(65, 91):
        names.append(chr(i))
    for i in range(len(names)):
        m[names[i]] = []
    split = corpus.split()
    for string in split:
        clean = string.strip(".,!?'-:;\"()[]{}")
        clean = clean.lower()
        clean = clean.replace("-", "")

        if clean not in lis:
            lis.append(clean)
            for char in string:
                if char.isalpha():
                    z = char.upper()
                    if z in m:
                        m[z].append(string)
                    break

    return m


# -----------------------------------------#
# TESTING YOUR CODE                        #
# -----------------------------------------#
# The code below runs only when this file is executed directly.
if __name__ == "__main__":
    import pprint

    # ----------------------------------------------#
    # TESTING YOUR CODE ON SAMPLE TEST CASES        #
    # Run this file and manually compare the output #
    # with the expected output below.                #
    # ----------------------------------------------#

    corpus = ("'Never again, never again shall I "
              "submit to superior force.'")
    pprint.pprint(leading_letters(corpus))
    # Should print:
    # {'A': ['again,'],
    #  'B': [],
    #  'C': [],
    #  'D': [],
    #  'E': [],
    #  'F': ["force.'"],
    #  'G': [],
    #  'H': [],
    #  'I': ['I'],
    #  'J': [],
    #  'K': [],
    #  'L': [],
    #  'M': [],
    #  'N': ["'Never"],
    #  'O': [],
    #  'P': [],
    #  'Q': [],
    #  'R': [],
    #  'S': ['shall', 'submit', 'superior'],
    #  'T': ['to'],
    #  'U': [],
    #  'V': [],
    #  'W': [],
    #  'X': [],
    #  'Y': [],
    #  'Z': []}

    result = leading_letters("!!! co-operate Cooperate CO-OPERATE ???")
    if result is not None:
        print(result["C"])
    # Should print: ['co-operate']

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#


# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your function, type one of the following commands in the terminal:
# python -m pytest tests/test_q8.py
# python3 -m pytest tests/test_q8.py
