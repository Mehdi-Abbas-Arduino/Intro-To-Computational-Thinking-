# -----------------------------------------#
# FUNCTION DEFINITION                      #
# -----------------------------------------#

def print_power_levels(row_count):
    # WRITE YOUR CODE HERE
    for i in range(row_count):
        for j in range(i+1,0,-1):
                print(2**(j-1),end=' ')
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

    print_power_levels(3)
    ''' Should print:
    1
    2 1
    4 2 1
    '''

    print_power_levels(1)
    ''' Should print:
    1
    '''

    print_power_levels(2)
    ''' Should print:
    1
    2 1
    '''

    print_power_levels(6)
    ''' Should print:
    1
    2 1
    4 2 1
    8 4 2 1
    16 8 4 2 1
    32 16 8 4 2 1
    '''

    print_power_levels(8)
    ''' Should print:
    1
    2 1
    4 2 1
    8 4 2 1
    16 8 4 2 1
    32 16 8 4 2 1
    64 32 16 8 4 2 1
    128 64 32 16 8 4 2 1
    '''

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#



# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your function, type the following command in the terminal:
# pytest tests/test_q2.py
