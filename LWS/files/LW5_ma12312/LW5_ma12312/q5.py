# -----------------------------------------#
# FUNCTION DEFINITION                      #
# -----------------------------------------#

def stage_light_display(size):
    for i in range(size):
        for j in range(size- i -1):
            print(" ",end='')
        for z in range(2*i+1):
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

    stage_light_display(5)
    ''' Should print:
        *
       ***
      *****
     *******
    *********
    '''

    stage_light_display(4)
    ''' Should print:
       *
      ***
     *****
    *******
    '''

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#



# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your function, type the following command in the terminal:
# pytest tests/test_q5.py