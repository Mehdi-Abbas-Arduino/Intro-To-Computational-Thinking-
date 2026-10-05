# -----------------------------------------#
# FUNCTION DEFINITION                      #
# -----------------------------------------#

def hollow_square(size):
    # WRITE YOUR CODE HERE
    for i in range(1,size+1):
        if i == 1 or i == size:
            for j in range(1,size+1):
                print('*',end='')
        else:
            # n = size-2
            for z in range(1,size+1):
                if z==1 or z == size:
                    print('*',end='')
                else:
                    print(' ',end='')
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

    hollow_square(5)
    ''' Should print:
    *****
    *   *
    *   *
    *   *
    *****
    '''

    hollow_square(1)
    ''' Should print:
    *
    '''

    hollow_square(3)
    ''' Should print:
    ***
    * *
    ***
    '''


    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#



# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your function, type the following command in the terminal:
# pytest tests/test_q5.py
