# -----------------------------------------#
# FUNCTION DEFINITION                      #
# -----------------------------------------#


def print_rewards(last_order):
    if last_order == 0:
        return
    print_rewards(last_order - 1)
    if last_order % 3 == 0 and last_order % 5 == 0:
        print("ChaiBiscuit")
    elif last_order % 3 == 0:
        print("Chai")
    elif last_order % 5 == 0:
        print("Biscuit")
    else:
        print(last_order)

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

    print_rewards(1)
    # Should print:
    # 1

    print()

    print_rewards(5)
    # Should print:
    # 1
    # 2
    # Chai
    # 4
    # Biscuit

    print()

    print_rewards(16)
    # Should print:
    # 1
    # 2
    # Chai
    # 4
    # Biscuit
    # Chai
    # 7
    # 8
    # Chai
    # Biscuit
    # 11
    # Chai
    # 13
    # 14
    # ChaiBiscuit
    # 16

    print()

    print_rewards(7)
    # Should print:
    # 1
    # 2
    # Chai
    # 4
    # Biscuit
    # Chai
    # 7

    print()

    print_rewards(34)
    # Should print:
    # 1
    # 2
    # Chai
    # 4
    # Biscuit
    # Chai
    # 7
    # 8
    # Chai
    # Biscuit
    # 11
    # Chai
    # 13
    # 14
    # ChaiBiscuit
    # 16
    # 17
    # Chai
    # 19
    # Biscuit
    # Chai
    # 22
    # 23
    # Chai
    # Biscuit
    # 26
    # Chai
    # 28
    # 29
    # ChaiBiscuit
    # 31
    # 32
    # Chai
    # 34

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#


# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your function, type one of the following commands in the terminal:
# python -m pytest tests/test_q4.py
# python3 -m pytest tests/test_q4.py
