# -----------------------------------------#
# FUNCTION DEFINITION                      #
# -----------------------------------------#
def helper(step_count, symbol, temp=1):
    if temp == step_count:
        print((" ") * (step_count - temp) + symbol * temp)
        return
    print((" ") * (step_count - temp) + symbol * temp)
    helper(step_count,symbol,temp+1)
def print_staircase(step_count, symbol):
    # WRITE YOUR CODE HERE
    helper(step_count,symbol)


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

    print_staircase(1, '#')
    # Should print:
    # #

    print_staircase(2, '*')
    # Should print:
    #  *
    # **

    print_staircase(4, '$')
    # Should print:
    #    $
    #   $$
    #  $$$
    # $$$$

    print_staircase(7, '@')
    # Should print:
    #       @
    #      @@
    #     @@@
    #    @@@@
    #   @@@@@
    #  @@@@@@
    # @@@@@@@

    print_staircase(5, '+')
    # Should print:
    #     +
    #    ++
    #   +++
    #  ++++
    # +++++

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#


# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your function, type one of the following commands in the terminal:
# python -m pytest tests/test_q2.py
# python3 -m pytest tests/test_q2.py
