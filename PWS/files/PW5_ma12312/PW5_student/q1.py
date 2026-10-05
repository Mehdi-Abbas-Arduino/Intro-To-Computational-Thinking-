# -----------------------------------------#
# FUNCTION DEFINITION                      #
# -----------------------------------------#

def print_combo_multipliers(level_count):
    # WRITE YOUR CODE HERE
    for i in range(level_count,0,-1):
        for j in range(1,i+1):
            print(i**j,end=' ')
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

    print_combo_multipliers(5)
    ''' Should print:
    5 25 125 625 3125
    4 16 64 256
    3 9 27
    2 4
    1
    '''

    print_combo_multipliers(6)
    ''' Should print:
    6 36 216 1296 7776 46656
    5 25 125 625 3125
    4 16 64 256
    3 9 27
    2 4
    1
    '''

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#



# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your function, type the following command in the terminal:
# pytest tests/test_q1.py
