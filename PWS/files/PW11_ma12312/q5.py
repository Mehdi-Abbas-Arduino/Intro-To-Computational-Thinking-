def dot(A, B):
    # WRITE YOUR CODE HERE
    if len(A) != len(B):
        return
    if A == [] and B == []:
        return 0
    else:
        return (A[0] * B[0]) + dot(A[1:],B[1:])


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

    print(dot([1], [3]))
    # Should print: 3

    print(dot([0, -3, 6], [4, 9, 1]))
    # Should print: -21

    print(dot([-2, 3], [4, -5]))
    # Should print: -23

    print(dot([0, 0], [999, -999]))
    # Should print: 0

    print(dot([1, -2, 3, -4], [5, 6, 7, 8]))
    # Should print: -18

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#


# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your function, type one of the following commands in the terminal:
# python -m pytest tests/test_q5.py
# python3 -m pytest tests/test_q5.py
