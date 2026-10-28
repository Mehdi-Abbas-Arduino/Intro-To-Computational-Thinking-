# -----------------------------------------#
# FUNCTION DEFINITIONS                     #
# -----------------------------------------#
def helper(number_of_rows, index=1, string=''):
    if index > number_of_rows:
        return
    else:
        string += str(index) + ' '
        print(string)
        helper(number_of_rows, index + 1, string)


def print_number(number_of_rows):
    helper(number_of_rows)

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

    print_number(4)
    # Should print:
    # 1
    # 1 2
    # 1 2 3
    # 1 2 3 4

    print_number(1)
    # Should print:
    # 1

    print_number(5)
    # Should print:
    # 1
    # 1 2
    # 1 2 3
    # 1 2 3 4
    # 1 2 3 4 5

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#


# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your function, type one of the following commands:
# python -m pytest tests/test_q5.py
# python3 -m pytest tests/test_q5.py
