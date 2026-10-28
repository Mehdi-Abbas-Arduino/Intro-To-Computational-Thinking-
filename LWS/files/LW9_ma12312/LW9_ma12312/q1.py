# -----------------------------------------#
# FUNCTION DEFINITION                      #
# -----------------------------------------#

def crossword_positions(crossword):
    # WRITE YOUR CODE HERE
    lst = []
    crossword = crossword.split()
    for i in range(len(crossword)):
        row = i
        for j in range(len(crossword[i])):
            col = j
            if crossword[i][j] == '\n':
                print()
            lst.append([crossword[i][j],row,col])
    return lst 
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

    print(crossword_positions('CHAI\nQUIZ\nBUNK\nLATE'))
    # Should print:
    # [['C', 0, 0], ['H', 0, 1], ['A', 0, 2], ['I', 0, 3],
    #  ['Q', 1, 0], ['U', 1, 1], ['I', 1, 2], ['Z', 1, 3],
    #  ['B', 2, 0], ['U', 2, 1], ['N', 2, 2], ['K', 2, 3],
    #  ['L', 3, 0], ['A', 3, 1], ['T', 3, 2], ['E', 3, 3]]

    print(crossword_positions('DS\nAL\nGO'))
    # Should print:
    # [['D', 0, 0], ['S', 0, 1], ['A', 1, 0],
    #  ['L', 1, 1], ['G', 2, 0], ['O', 2, 1]]

    print(crossword_positions('CHAI'))
    # Should print: [['C', 0, 0], ['H', 0, 1], ['A', 0, 2], ['I', 0, 3]]

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#



# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your function, type one of the following commands in the terminal:
# python -m pytest tests/test_q1.py
# python3 -m pytest tests/test_q1.py