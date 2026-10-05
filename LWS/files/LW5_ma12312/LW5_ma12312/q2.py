# -----------------------------------------#
# FUNCTION DEFINITION                      #
# -----------------------------------------#

def print_odd_staircase(row_count):
    # WRITE YOUR CODE HERE
    odd=1
    for i in range(1,row_count+1):
        for j in range(i):
            print(odd,end=' ')
            odd += 2
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

    print_odd_staircase(2)
    ''' Should print:
    1
    3 5
    '''

    print_odd_staircase(3)
    ''' Should print:
    1
    3 5
    7 9 11
    '''

    print_odd_staircase(5)
    ''' Should print:
    1
    3 5
    7 9 11
    13 15 17 19
    21 23 25 27 29
    '''

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#



# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your function, type the following command in the terminal:
# pytest tests/test_q2.py