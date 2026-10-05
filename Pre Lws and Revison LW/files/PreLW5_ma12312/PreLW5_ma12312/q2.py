# -----------------------------------------#
# FUNCTION DEFINITION                      #
# -----------------------------------------#

def rectangle_pattern(height, width):
    for i in range(1,height+1):
        for j in range(1,width+1):
            print('*',end='')
        print()


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

    rectangle_pattern(3, 5)
    ''' Should print:
    *****
    *****
    *****
    '''

    rectangle_pattern(1, 4)
    ''' Should print:
    ****
    '''

    rectangle_pattern(4, 1)
    ''' Should print:
    *
    *
    *
    *
    '''


    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#



# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your function, type the following command in the terminal:
# pytest tests/test_q2.py
