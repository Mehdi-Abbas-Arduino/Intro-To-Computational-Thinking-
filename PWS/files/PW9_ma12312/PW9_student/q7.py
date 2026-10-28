# -----------------------------------------#
# FUNCTION DEFINITIONS                     #
# -----------------------------------------#

def rectangular_distance(grid):
    # WRITE YOUR CODE HERE
    lst = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                lst.append([i,j])
    row = 0
    col = 0 
    sum = 0
    for i in range(len(lst)-1):
        row += abs(lst[i][0] - lst[i+1][0])
        col += abs(lst[i][1] - lst[i+1][1])

    sum = row + col
    return sum

def main():
    row, col = input().split()
    row = int(row)
    col = int(col)

    matrix = []

    for i in range(row):
        line = input().strip()
        lst = []

        for j in range(col):
            lst.append(int(line[j]))

        matrix.append(lst)

    x = rectangular_distance(matrix)
    print(x)



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

    # Note: Inputs to be entered are labelled as [ Input -> X ] where X is the input.

    main()
    # [ Input -> 6 4 ]
    # [ Input -> 0000 ]
    # [ Input -> 0001 ]
    # [ Input -> 0000 ]
    # [ Input -> 0000 ]
    # [ Input -> 0100 ]
    # [ Input -> 0000 ]
    # Should print: 5

    main()
    # [ Input -> 5 5 ]
    # [ Input -> 10000 ]
    # [ Input -> 00000 ]
    # [ Input -> 00000 ]
    # [ Input -> 00000 ]
    # [ Input -> 00001 ]
    # Should print: 8

    main()
    # [ Input -> 2 2 ]
    # [ Input -> 01 ]
    # [ Input -> 01 ]
    # Should print: 1

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#



# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your functions, type one of the following commands in the terminal:
# python -m pytest tests/test_q7.py
# python3 -m pytest tests/test_q7.py
