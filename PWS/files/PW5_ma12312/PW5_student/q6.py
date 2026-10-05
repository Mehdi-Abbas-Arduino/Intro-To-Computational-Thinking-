# -----------------------------------------#
# FUNCTION DEFINITION                      #
# -----------------------------------------#

def print_upper_diamond(size):
        # WRITE YOUR CODE HERE
        for i in range(size):
            for k in range(size-i-1):
                print(" ",end='')
            for j in range(2*i+1):
                print('*',end='')
            print()
def print_lower_diamond(size):
        for i in range(size-2,-1,-1):
                for k in range(size-i-1):
                    print(" ",end='')
                for j in range(2*i+1):
                    print('*',end='')
                print()
                

def print_diamond(size):
    print_upper_diamond(size)
    print_lower_diamond(size)

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

    print_diamond(5)
    ''' Should print:
        *
       ***
      *****
     *******
    *********
     *******
      *****
       ***
        *
    '''

    print_diamond(4)
    ''' Should print:
       *
      ***
     *****
    *******
     *****
      ***
       *
    '''

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#



# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your function, type the following command in the terminal:
# pytest tests/test_q6.py
