# -----------------------------------------#
# FUNCTION DEFINITION                      #
# -----------------------------------------#

def diagonal_difference(net_changes):

    # WRITE YOUR CODE HERE
    primary = 0
    secondary = 0
    for row in range(len(net_changes)):
        for col in range(len(net_changes[row])):
            if row == col:
                primary += net_changes[row][col]

    for row in range(len(net_changes)):
        for col in range(len(net_changes[row])):
            if row + col == len(net_changes) - 1:
                secondary += net_changes[row][col]

    return abs(primary - secondary)


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

    print(diagonal_difference(
        [
            [11, 2, 4], 
            [4, 5, 6], 
            [10, 8, -12] 
        ]))
    # Should print: 15

    print(diagonal_difference(
        [
            [1, 2], 
            [3, 10] 
        ]))
    # Should print: 6

    print(diagonal_difference(
        [
            [-5]
        ]))
    # Should print: 0

    print(diagonal_difference(
        [
            [2]
        ]))
    # Should print: 0

    print(diagonal_difference(
        [
            [1, 2], 
            [3, 4]
        ]))
    # Should print: 0

    print(diagonal_difference(
        [
            [3, 5, 7], 
            [1, 4, 9], 
            [2, 8, 6]
        ]))
    # Should print: 0

    print(diagonal_difference(
        [
            [10, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16]
        ]))
    # Should print: 9

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#



# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your function, type one of the following commands in the terminal:
# python -m pytest tests/test_q2.py
# python3 -m pytest tests/test_q2.py