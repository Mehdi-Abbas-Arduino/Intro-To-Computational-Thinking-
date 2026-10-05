# -----------------------------------------#
# FUNCTION DEFINITION                      #
# -----------------------------------------#

def half_diamond(height):
    # WRITE YOUR CODE HERE
    for i in range(1,height+1):
        
        for j in range(1,i+1):
            print('*',end='')
        print()
    for i in range(height,1,-1):
        for j in range(i,1,-1):
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

    half_diamond(4)
    ''' Should print:
    *
    **
    ***
    ****
    ***
    **
    *
    '''

    half_diamond(1)
    ''' Should print:
    *
    '''

    half_diamond(2)
    ''' Should print:
    *
    **
    *
    '''


    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#



# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your function, type the following command in the terminal:
# pytest tests/test_q4.py
