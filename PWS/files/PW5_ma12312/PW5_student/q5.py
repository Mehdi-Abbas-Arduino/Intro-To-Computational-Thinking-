# -----------------------------------------#
# FUNCTION DEFINITION                      #
# -----------------------------------------#

def print_inverted_number_triangle(row_count):
    # WRITE YOUR CODE HERE
    for i in range(row_count,0,-1):
        for k in range(row_count-i):
            print(" ",end='')
        for j in range(i):
            print(i,end=' ')
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

    print_inverted_number_triangle(5)
    ''' Should print:
    5 5 5 5 5
     4 4 4 4
      3 3 3
       2 2
        1
    '''

    print_inverted_number_triangle(3)
    ''' Should print:
    3 3 3
     2 2
      1
    '''

    print_inverted_number_triangle(1)
    ''' Should print:
    1
    '''

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#



# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your function, type the following command in the terminal:
# pytest tests/test_q5.py
