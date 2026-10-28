# -----------------------------------------#
# FUNCTION DEFINITION                      #
# -----------------------------------------#

def reverse_slice(t, start, stop):
    # WRITE YOUR CODE HERE
    lis = []
    lis = t[start:stop]
    lis = lis[::-1]
    t[start:stop] = lis
     


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

    t = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(reverse_slice(t, 3, 7))
    # Should print: None
    print(t)
    # Should print: [0, 1, 2, 6, 5, 4, 3, 7, 8, 9]

    t = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(reverse_slice(t, 2, -4))
    # Should print: None
    print(t)
    # Should print: [0, 1, 5, 4, 3, 2, 6, 7, 8, 9]

    t = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(reverse_slice(t, 0, 10))
    # Should print: None
    print(t)
    # Should print: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

    t = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(reverse_slice(t, 0, -1))
    # Should print: None
    print(t)
    # Should print: [8, 7, 6, 5, 4, 3, 2, 1, 0, 9]

    t = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(reverse_slice(t, 20, 30))
    # Should print: None
    print(t)
    # Should print: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    t = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(reverse_slice(t, -20, -10))
    # Should print: None
    print(t)
    # Should print: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


    t = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]
    print(reverse_slice(t, 2, 6))
    # Should print: None
    print(t)
    # Should print: [2, 3, 13, 11, 7, 5, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#



# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your function, type the following command in the terminal:
# python -m pytest tests/test_q3.py
# python3 -m pytest tests/test_q3.py