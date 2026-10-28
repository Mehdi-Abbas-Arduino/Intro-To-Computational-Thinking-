# -----------------------------------------#
# FUNCTION DEFINITIONS                     #
# -----------------------------------------#


def matrixReshape(mat, r, c):
    rows = len(mat)
    cols = len(mat[0])

    if rows * cols != r * c:
        return mat

    lst = []

    for i in range(rows):
        for j in range(cols):
            lst.append(mat[i][j])

    result = []
    index = 0

    for i in range(r):
        temp = []
        for j in range(c):
            temp.append(lst[index])
            index += 1
        result.append(temp)

    return result

 
def main():
    rows, cols, r, c = map(int, input().split())

    mat = []

    for i in range(rows):
        row = list(map(int, input().split(",")))
        mat.append(row)

    print(matrixReshape(mat, r, c))

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
    # [ Input -> 2 2 1 4 ]
    # [ Input -> 1,2 ]
    # [ Input -> 3,4 ]
    # Should print: [[1, 2, 3, 4]]

    main()
    # [ Input -> 2 2 2 4 ]
    # [ Input -> 1,2 ]
    # [ Input -> 3,4 ]
    # Should print: [[1, 2], [3, 4]]

    main()
    # [ Input -> 2 3 3 2 ]
    # [ Input -> 1,2,3 ]
    # [ Input -> 4,5,6 ]
    # Should print: [[1, 2], [3, 4], [5, 6]]

    main()
    # [ Input -> 2 2 2 3 ]
    # [ Input -> 1,2 ]
    # [ Input -> 3,4 ]
    # Should print: [[1, 2], [3, 4]]

    main()
    # [ Input -> 1 5 5 1 ]
    # [ Input -> 1,2,3,4,5 ]
    # Should print: [[1], [2], [3], [4], [5]]

    main()
    # [ Input -> 4 1 1 4 ]
    # [ Input -> 1 ]
    # [ Input -> 2 ]
    # [ Input -> 3 ]
    # [ Input -> 4 ]
    # Should print: [[1, 2, 3, 4]]

    main()
    # [ Input -> 3 4 2 6 ]
    # [ Input -> 1,2,3,4 ]
    # [ Input -> 5,6,7,8 ]
    # [ Input -> 9,10,11,12 ]
    # Should print: [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12]]

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#



# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your functions, type one of the following commands in the terminal:
# python -m pytest tests/test_q8.py
# python3 -m pytest tests/test_q8.py
