# -----------------------------------------#
# FUNCTION DEFINITIONS                     #
# -----------------------------------------#


def my_bill(all_charges, tab_id):
    result = []

    for i in range(len(all_charges)):
        if all_charges[i][0] == tab_id:
            total = 0

            for j in range(1, len(all_charges[i])):
                total += all_charges[i][j]

            result.append(round(total, 2))

    return result
                

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

    all_charges = [
        [12, 2.32, 5.6, 2.29, 6.08, 7.12],
        [35, 18.29, 18.3, 5.55, 5.55],
        [4, 12.0],
        [35, 3.0],
        [7, 3.95, 4.95, 5.95, 6.95],
        [7, 5.2, -2.0],
        [12, 0.0],
        [7, 13.69, 2.49],
    ]

    print(my_bill(all_charges, 4))
    # Should print: [12.0]

    print(my_bill(all_charges, 7))
    # Should print: [21.8, 3.2, 16.18]

    print(my_bill(all_charges, 12))
    # Should print: [23.41, 0.0]

    print(my_bill(all_charges, 35))
    # Should print: [47.69, 3.0]

    print(my_bill(all_charges, 420))
    # Should print: []

    print(my_bill([[8]], 8))
    # Should print: [0]

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#



# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your functions, type one of the following commands in the terminal:
# python -m pytest tests/test_q2.py
# python3 -m pytest tests/test_q2.py
