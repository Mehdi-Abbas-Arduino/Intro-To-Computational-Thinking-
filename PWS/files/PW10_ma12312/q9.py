# -----------------------------------------#
# FUNCTION DEFINITIONS                     #
# -----------------------------------------#

def multiplication_table(number, last_multiplier):
    # WRITE YOUR CODE HERE
    if last_multiplier == 0:
        return
    multiplication_table(number,last_multiplier - 1)
    print(f"{number} * {last_multiplier} = {number*last_multiplier}")


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

    multiplication_table(5, 10)
    # Should print:
    # 5 * 1 = 5
    # 5 * 2 = 10
    # 5 * 3 = 15
    # 5 * 4 = 20
    # 5 * 5 = 25
    # 5 * 6 = 30
    # 5 * 7 = 35
    # 5 * 8 = 40
    # 5 * 9 = 45
    # 5 * 10 = 50

    print()

    multiplication_table(1, 1)
    # Should print:
    # 1 * 1 = 1

    print()

    multiplication_table(12, 15)
    # Should print:
    # 12 * 1 = 12
    # 12 * 2 = 24
    # 12 * 3 = 36
    # 12 * 4 = 48
    # 12 * 5 = 60
    # 12 * 6 = 72
    # 12 * 7 = 84
    # 12 * 8 = 96
    # 12 * 9 = 108
    # 12 * 10 = 120
    # 12 * 11 = 132
    # 12 * 12 = 144
    # 12 * 13 = 156
    # 12 * 14 = 168
    # 12 * 15 = 180

    print()

    multiplication_table(7, 20)
    # Should print:
    # 7 * 1 = 7
    # 7 * 2 = 14
    # 7 * 3 = 21
    # 7 * 4 = 28
    # 7 * 5 = 35
    # 7 * 6 = 42
    # 7 * 7 = 49
    # 7 * 8 = 56
    # 7 * 9 = 63
    # 7 * 10 = 70
    # 7 * 11 = 77
    # 7 * 12 = 84
    # 7 * 13 = 91
    # 7 * 14 = 98
    # 7 * 15 = 105
    # 7 * 16 = 112
    # 7 * 17 = 119
    # 7 * 18 = 126
    # 7 * 19 = 133
    # 7 * 20 = 140

    print()

    multiplication_table(3, 5)
    # Should print:
    # 3 * 1 = 3
    # 3 * 2 = 6
    # 3 * 3 = 9
    # 3 * 4 = 12
    # 3 * 5 = 15

    print()

    multiplication_table(3, 4)
    # Should print:
    # 3 * 1 = 3
    # 3 * 2 = 6
    # 3 * 3 = 9
    # 3 * 4 = 12

    print()

    multiplication_table(7, 1)
    # Should print:
    # 7 * 1 = 7

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#


# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your function, type one of the following commands:
# python -m pytest tests/test_q9.py
# python3 -m pytest tests/test_q9.py
