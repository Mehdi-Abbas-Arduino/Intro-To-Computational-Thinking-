# -----------------------------------------#
# FUNCTION DEFINITIONS                     #
# -----------------------------------------#

def sum_lst(lst):
    # WRITE YOUR CODE HERE
    return sum(lst)


def main():
    # WRITE YOUR CODE HERE
    x = list(map(int, input().split()))
    z = sum_lst(x)
    print(z)


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

    main()
    # [ Input -> 10 20 30 40 50]
    # Should print: 150

    print()

    main()
    # [ Input -> 1 2]
    # Should print: 3

    print()

    main()
    # [ Input -> 5 15 25 35]
    # Should print: 80

    print()

    main()
    # [ Input -> 99]
    # Should print: 99

    print()

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#



# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your function, type the following command in the terminal:
# python -m pytest tests/test_q2.py
# python3 -m pytest tests/test_q2.py