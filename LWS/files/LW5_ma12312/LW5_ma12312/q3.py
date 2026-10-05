# -----------------------------------------#
# FUNCTION DEFINITION                      #
# -----------------------------------------#

def power_pyramid(row_count):
    # WRITE YOUR CODE HERE
    for i in range(1,row_count+1):
        for j in range(1,i):
            if j == 1 or j == 2:
                print(j ,end=' ')
            else:
                print(2**(j-1),end=' ')
        for z in range(i,0,-1):
            if z == 1 or z == 2:
                print(z,end=' ')
            else:
                print(2**(z-1),end=' ')
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

    power_pyramid(3)
    ''' Should print:
    1
    1 2 1
    1 2 4 2 1
    '''

    power_pyramid(1)
    ''' Should print:
    1
    '''

    power_pyramid(2)
    ''' Should print:
    1
    1 2 1
    '''

    power_pyramid(6)
    ''' Should print:
    1
    1 2 1
    1 2 4 2 1
    1 2 4 8 4 2 1
    1 2 4 8 16 8 4 2 1
    1 2 4 8 16 32 16 8 4 2 1
    '''

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#



# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your function, type the following command in the terminal:
# pytest tests/test_q3.py