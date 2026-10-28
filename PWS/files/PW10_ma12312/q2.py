# -----------------------------------------#
# FUNCTION DEFINITIONS                     #
# -----------------------------------------#
def helper(number_of_rows,index=1):
    if type(number_of_rows) != int or number_of_rows < 0:
        print("Invalid input")
        return
    if number_of_rows == 0:
        return
    if number_of_rows > 50:
        print("Program can't handle this input")
        return
    if index > number_of_rows:
        return
    else:
        print("  " * (number_of_rows - index) + ' *' * index)
        helper(number_of_rows,index+1)

def pattern(number_of_rows):
    # WRITE YOUR CODE HERE
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

    pattern(2)
    # Should print:
    #   *
    # * *

    pattern(4)
    # Should print:
    #       *
    #     * *
    #   * * *
    # * * * *

    pattern(-5)
    # Should print:
    # Invalid input

    pattern(3000000)
    # Should print:
    # Program can't handle this input

    pattern(0)
    # Should print nothing.

    pattern('Hello')
    # Should print:
    # Invalid input

    pattern(1)
    # Should print:
    # *

    pattern(-2)
    # Should print:
    # Invalid input

    pattern('four')
    # Should print:
    # Invalid input

    pattern(51)
    # Should print:
    # Program can't handle this input

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#


# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your function, type one of the following commands:
# python -m pytest tests/test_q2.py
# python3 -m pytest tests/test_q2.py
