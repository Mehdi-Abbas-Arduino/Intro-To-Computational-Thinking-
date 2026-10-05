# -----------------------------------------#
# FUNCTION DEFINITION                      #
# -----------------------------------------#

def print_scoreboard_alignment(max_number):
    # WRITE YOUR CODE HERE
    for i in range(max_number+1,1,-1):
      # if max_number - i == 0:
      #   print("  ", end='')
      for k in range(max_number-i+1):
        print("  ",end='')
      for j in range(i):
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

    print_scoreboard_alignment(5)
    ''' Should print:
    0 1 2 3 4 5
      0 1 2 3 4
        0 1 2 3
          0 1 2
            0 1
    '''

    print_scoreboard_alignment(1)
    ''' Should print:
    0 1
    '''

    print_scoreboard_alignment(2)
    ''' Should print:
    0 1 2
      0 1
    '''

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#



# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your function, type the following command in the terminal:
# pytest tests/test_q4.py
