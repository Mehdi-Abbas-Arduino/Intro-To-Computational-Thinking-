# -----------------------------------------#
# FUNCTION DEFINITION                      #
# -----------------------------------------#

def visit(clues, position):
    if clues[position] is None:
        return
    next_position = clues[position]
    clues[position] = None
    visit(clues, next_position)


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

    clues = [2, 3, 4, 0, 1]
    visit(clues, 3)
    print(clues)
    # Should print: [None, None, None, None, None]

    clues = [2, 0, 1, 4, 3]
    visit(clues, 4)
    print(clues)
    # Should print: [2, 0, 1, None, None]

    clues = [0]
    visit(clues, 0)
    print(clues)
    # Should print: [None]

    clues = [2, 0, 1]
    visit(clues, 0)
    print(clues)
    # Should print: [None, None, None]

    clues = [2, 0, 1, 0, 1]
    visit(clues, 2)
    print(clues)
    # Should print: [None, None, None, 0, 1]

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#


# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your function, type one of the following commands in the terminal:
# python -m pytest tests/test_q6.py
# python3 -m pytest tests/test_q6.py
