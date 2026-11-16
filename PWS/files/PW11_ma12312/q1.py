def gcd(a, b):
    # WRITE YOUR CODE HERE
    if a == 0:
        return b
    if b == 0:
        return a
    else:
        first = b
        quotient = a // b
        remainder = a % b
        return gcd(first,remainder)


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

    print(gcd(2322, 654))
    # Should print: 6

    print(gcd(12, 8))
    # Should print: 4

    print(gcd(287, 175))
    # Should print: 7

    print(gcd(175, 287))
    # Should print: 7

    print(gcd(98, 56))
    # Should print: 14

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#


# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your function, type one of the following commands in the terminal:
# python -m pytest tests/test_q1.py
# python3 -m pytest tests/test_q1.py
