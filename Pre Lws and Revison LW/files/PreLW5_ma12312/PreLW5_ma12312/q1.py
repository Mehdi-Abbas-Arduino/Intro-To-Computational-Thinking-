# -----------------------------------------#
# FUNCTION DEFINITION                      #
# -----------------------------------------#

def square_pattern(size):
    for i in range(1,size+1):
        for j in range(1,size+1):
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

    square_pattern(4)
    ''' Should print:
    ****
    ****
    ****
    ****
    '''

    square_pattern(1)
    ''' Should print:
    *
    '''

    square_pattern(3)
    ''' Should print:
    ***
    ***
    ***
    '''


    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#



# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your function, type the following command in the terminal:
# pytest tests/test_q1.py
