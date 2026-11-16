def minmax(temperatures):
    if len(temperatures) == 1:
        return [temperatures[0],temperatures[0]]
    if len(temperatures) == 1:
        return [result[0],result[1]]
    result = minmax(temperatures[1:])
    if temperatures[0] < result[0]:
        result[0] = temperatures[0]

    if temperatures[0] > result[1]:
        result[1] = temperatures[0]

    return result



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

    print(minmax([1]))
    # Should print: [1, 1]

    print(minmax([0, -3, 6, 4, 9, 1]))
    # Should print: [-3, 9]

    print(minmax([9, 1]))
    # Should print: [1, 9]

    print(minmax([-7, -2, -9, -2]))
    # Should print: [-9, -2]

    print(minmax([2, 2, 2, 2]))
    # Should print: [2, 2]

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#


# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your function, type one of the following commands in the terminal:
# python -m pytest tests/test_q6.py
# python3 -m pytest tests/test_q6.py
