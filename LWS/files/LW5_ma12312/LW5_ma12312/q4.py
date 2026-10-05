# -----------------------------------------#
# FUNCTION DEFINITION                      #
# -----------------------------------------#

def countdown_pattern(start_value):
    for i in range(start_value,0,-1):
      for k in range(start_value-i):
        print('  ',end='')
      for j in range(i,0,-1):
        print(str(j),end=' ')
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

    countdown_pattern(5)
    ''' Should print:
    5 4 3 2 1
      4 3 2 1
        3 2 1
          2 1
            1
    '''

    countdown_pattern(1)
    ''' Should print:
    1
    '''

    countdown_pattern(2)
    ''' Should print:
    2 1
      1
    '''

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#



# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your function, type the following command in the terminal:
# pytest tests/test_q4.py