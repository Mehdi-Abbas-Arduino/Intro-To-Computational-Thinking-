# -----------------------------------------#
# FUNCTION DEFINITION                      #
# -----------------------------------------#

def max_equal_guests(juice_boxes, snack_bars):
    # WRITE YOUR CODE HERE
    # while (snack_bars):
    #     x,y = juice_boxes , juice_boxes%snack_bars

    # print(x)
    minimum = min(juice_boxes,snack_bars)
    highest = 0
    for i in range(minimum,0,-1):

        if snack_bars%i == 0 and juice_boxes%i == 0:
            return i 


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

    print(max_equal_guests(12, 18))
    # Should print: 6

    print(max_equal_guests(9, 9))
    # Should print: 9

    print(max_equal_guests(16, 17))
    # Should print: 1

    print(max_equal_guests(32, 52))
    # Should print: 4

    print(max_equal_guests(256, 128))
    # Should print: 128

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#



# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your function, type the following command in the terminal:
# pytest tests/test_q2.py