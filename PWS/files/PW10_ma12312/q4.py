# -----------------------------------------#
# FUNCTION DEFINITIONS                     #
# -----------------------------------------#
def helper(n, previous=0, current=1):
    if n <= 0:
        return

    print(current)
    helper(n - 1, current, previous + current)


def print_fibb(number_of_terms):
    helper(number_of_terms)
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

    print_fibb(3)
    # Should print:
    # 1
    # 1
    # 2

    print()

    print_fibb(5)
    # Should print:
    # 1
    # 1
    # 2
    # 3
    # 5

    print()

    print_fibb(1)
    # Should print:
    # 1

    print()

    print_fibb(7)
    # Should print:
    # 1
    # 1
    # 2
    # 3
    # 5
    # 8
    # 13

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#


# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your function, type one of the following commands:
# python -m pytest tests/test_q4.py
# python3 -m pytest tests/test_q4.py
