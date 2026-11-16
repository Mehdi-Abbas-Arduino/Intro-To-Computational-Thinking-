def chickens_needed(starting_chickens, multiplier, bonus, level):
    # WRITE YOUR CODE HERE
    if level == 1:
        return starting_chickens
    else:
        compute = starting_chickens * multiplier + bonus
        return chickens_needed(compute,multiplier,bonus,level-1)
    


# -----------------------------------------#
# TESTING YOUR CODE                        #
# -----------------------------------------#
# The code below runs only when this file is executed directly.
if __name__ == "__main__":

    # ----------------------------------------------#
    # TESTING YOUR CODE ON SAMPLE TEST CASES        #
    # Run this file and manually check whether      #
    # your function produces the expected output.   #
    # ----------------------------------------------#

    print(chickens_needed(2, 3, 5, 6))
    # Should print: 1091

    print(chickens_needed(1, 2, 0, 10))
    # Should print: 512

    print(chickens_needed(1, 2, 1, 8))
    # Should print: 255

    print(chickens_needed(3, 4, 2, 4))
    # Should print: 234

    print(chickens_needed(9, 15, 7, 1))
    # Should print: 9

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#


# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your function, type one of the following commands in the terminal:
# python -m pytest tests/test_q4.py
# python3 -m pytest tests/test_q4.py
