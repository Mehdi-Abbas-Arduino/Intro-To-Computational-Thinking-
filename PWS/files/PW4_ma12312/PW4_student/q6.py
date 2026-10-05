# -----------------------------------------#
# FUNCTION DEFINITIONS                     #
# -----------------------------------------#


def max_power_distance(planet_count, power_source_1, power_source_2):
    n = []

    # Check if both power sources are invalid
    if power_source_1 >= planet_count and power_source_2 >= planet_count:
        return 0

    # Go through every planet
    for i in range(planet_count):

        # Both power sources are valid
        if power_source_1 < planet_count and power_source_2 < planet_count:
            diff1 = abs(i - power_source_1)
            diff2 = abs(i - power_source_2)

            # Store the nearer distance
            n.append(min(diff1, diff2))

        # Only power source 1 is valid
        elif power_source_1 < planet_count:
            diff1 = abs(i - power_source_1)
            n.append(diff1)

        # Only power source 2 is valid
        elif power_source_2 < planet_count:
            diff2 = abs(i - power_source_2)
            n.append(diff2)

    return max(n)


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
     
    print(max_power_distance(5, 0, 4))
    # Should print: 2

    print(max_power_distance(3, 6, 7))
    # Should print: 0

    print(max_power_distance(5, 5, 0))
    # Should print: 4

    print(max_power_distance(5, 0, 5))
    # Should print: 4

    print(max_power_distance(11, 2, 10))
    # Should print: 4

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#


# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your function, type the following command in the terminal:
# pytest tests/test_q6.py