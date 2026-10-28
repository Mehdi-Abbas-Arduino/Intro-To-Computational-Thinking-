# -----------------------------------------#
# FUNCTION DEFINITION                      #
# -----------------------------------------#


def catalan(j, k):
    lst = [1]

    for n in range(1, k):
        add = 0

        for i in range(n):
            add += lst[i] * lst[n - 1 - i]

        lst.append(add)

    return lst[j:k]


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

    print(catalan(0, 1))
    # Should print: [1]

    print(catalan(2, 8))
    # Should print: [2, 5, 14, 42, 132, 429]

    print(catalan(0, 8))
    # Should print: [1, 1, 2, 5, 14, 42, 132, 429]

    print(catalan(3, 6))
    # Should print: [5, 14, 42]

    print(catalan(5, 10))
    # Should print: [42, 132, 429, 1430, 4862]

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#



# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your function, type one of the following commands in the terminal:
# python -m pytest tests/test_q7.py
# python3 -m pytest tests/test_q7.py