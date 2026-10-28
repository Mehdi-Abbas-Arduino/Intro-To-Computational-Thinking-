# -----------------------------------------#
# FUNCTION DEFINITIONS                     #
# -----------------------------------------#

def print_lift_stops(first_floor, last_floor):
    if first_floor > last_floor:
        return

    if first_floor % 2 == 0:
        if first_floor + 2 <= last_floor: # Check if another even floor exists within the range
            print(first_floor, end=', ')
        else:
            print(first_floor)

    print_lift_stops(first_floor + 1, last_floor)
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

    print_lift_stops(0, 6)
    # Should print: 0, 2, 4, 6

    print_lift_stops(1, 5)
    # Should print: 2, 4

    print_lift_stops(-3, 3)
    # Should print: -2, 0, 2

    print_lift_stops(2, 3)
    # Should print: 2

    print_lift_stops(3, 4)
    # Should print: 4

    print_lift_stops(1, 1)
    # Should print nothing.

    print_lift_stops(0, 0)
    # Should print: 0

    print_lift_stops(1, 6)
    # Should print: 2, 4, 6

    print_lift_stops(0, 5)
    # Should print: 0, 2, 4

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#

# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your function, type one of the following commands:
# python -m pytest tests/test_q8.py
# python3 -m pytest tests/test_q8.py
