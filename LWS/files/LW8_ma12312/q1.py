# -----------------------------------------#
# FUNCTION DEFINITION                      #
# -----------------------------------------#

def read_integer_list(count):
    # WRITE YOUR CODE HERE
    empty_list = []
    for i in range(count):
        x = int(input())
        empty_list.append(x)
    return empty_list


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

    # Note: Inputs to be entered are labelled as [ Input -> X ] where X is the input.

    print(read_integer_list(3))
    # [ Input -> 5]
    # [ Input -> 10]
    # [ Input -> 15]
    # Should print: [5, 10, 15]

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#



# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your function, type the following command in the terminal:
# python -m pytest tests/test_q1.py
# python3 -m pytest tests/test_q1.py