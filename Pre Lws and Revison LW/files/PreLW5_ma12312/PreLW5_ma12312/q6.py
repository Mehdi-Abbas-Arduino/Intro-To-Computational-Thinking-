# -----------------------------------------#
# FUNCTION DEFINITION                      #
# -----------------------------------------#

def chessboard_pattern(rows, columns):
    # WRITE YOUR CODE HERE
    for i in range(1,rows+1):
        
        if i%2 != 0:
             for j in range(1,columns+1):
                         if j%2 == 0:
                             print('O',end='')
                         else:
                             print('X',end='') 
        else:
            for j in range(1,columns+1):
                        if j%2 == 0:
                            print('X',end='')
                        else:
                            print('O',end='')
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

    chessboard_pattern(5, 5)
    ''' Should print:
    XOXOX
    OXOXO
    XOXOX
    OXOXO
    XOXOX
    '''

    chessboard_pattern(2, 4)
    ''' Should print:
    XOXO
    OXOX
    '''

    chessboard_pattern(1, 1)
    ''' Should print:
    X
    '''


    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#



# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your function, type the following command in the terminal:
# pytest tests/test_q6.py
