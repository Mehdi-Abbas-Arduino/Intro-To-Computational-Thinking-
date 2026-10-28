# -----------------------------------------#
# FUNCTION DEFINITION                      #
# -----------------------------------------#


def remove_all(t, v):
    count = 0
    while v in t:
        t.remove(v)
        count += 1
    return count


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

    t = [8, 6, 6, 7, 5, 3, 7, 0, 7, 7, 9, 7]
    print(remove_all(t, 2))
    # Should print: 0
    print(t)
    # Should print: [8, 6, 6, 7, 5, 3, 7, 0, 7, 7, 9, 7]

    print()

    t = [8, 6, 6, 7, 5, 3, 7, 0, 7, 7, 9, 7]
    print(remove_all(t, 5))
    # Should print: 1
    print(t)
    # Should print: [8, 6, 6, 7, 3, 7, 0, 7, 7, 9, 7]

    print()

    t = [8, 6, 6, 7, 3, 7, 0, 7, 7, 9, 7]
    print(remove_all(t, 7))
    # Should print: 5
    print(t)
    # Should print: [8, 6, 6, 3, 0, 9]

    print()

    t = [2, 2, 2, 2]
    print(remove_all(t, 2))
    # Should print: 4
    print(t)
    # Should print: []

    print()

    t = []
    print(remove_all(t, 2))
    # Should print: 0
    print(t)
    # Should print: []

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#



# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your function, type one of the following commands in the terminal:
# python -m pytest tests/test_q2.py
# python3 -m pytest tests/test_q2.py