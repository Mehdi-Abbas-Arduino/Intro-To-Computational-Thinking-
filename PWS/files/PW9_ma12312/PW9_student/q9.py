# -----------------------------------------#
# FUNCTION DEFINITIONS                     #
# -----------------------------------------#


def entryTime(digits_to_type, keypad):
    grid = []
    for i in range(0, 9, 3):
        row = []
        for j in range(i, i + 3):
            row.append(keypad[j])
        grid.append(row)

    total = 0

    for i in range(len(digits_to_type) - 1):
        current = digits_to_type[i]
        next_digit = digits_to_type[i + 1]

        r1 = c1 = r2 = c2 = 0

        for r in range(3):
            for c in range(3):
                if grid[r][c] == current:
                    r1 = r
                    c1 = c

                if grid[r][c] == next_digit:
                    r2 = r
                    c2 = c

        row_diff = abs(r1 - r2)
        col_diff = abs(c1 - c2)

        total += max(row_diff, col_diff)

    return total
 




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

    print(entryTime('423692', '923857614'))      # Should print: 8
    print(entryTime('5111', '752961348'))        # Should print: 1
    print(entryTime('91566165', '639485712'))    # Should print: 11
    print(entryTime('595275', '396748521'))      # Should print: 7
    print(entryTime('444', '923857614'))         # Should print: 0

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#



# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your functions, type one of the following commands in the terminal:
# python -m pytest tests/test_q9.py
# python3 -m pytest tests/test_q9.py