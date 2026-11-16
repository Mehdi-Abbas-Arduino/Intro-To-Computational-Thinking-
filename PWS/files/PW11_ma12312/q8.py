def count_group(bubbles, target, count=0):
    if bubbles == '':
        return count

    if bubbles[0] != target:
        return count

    return count_group(bubbles[1:], target, count + 1)


def helper(bubbles, min_group_size, string=''):
    if bubbles == '':
        return string

    target = bubbles[0]

    count = count_group(bubbles, target)

    if count < min_group_size:
        string += target * count

    return helper(bubbles[count:], min_group_size, string)


def pop_bubbles(bubbles, min_group_size):
    return helper(bubbles, min_group_size)

# -----------------------------------------#
# TESTING YOUR CODE                        #
# -----------------------------------------#
# The code below runs only when this file is executed directly.
if __name__ == "__main__":

    # ----------------------------------------------#
    # TESTING YOUR CODE ON SAMPLE TEST CASES        #
    # Run this file and manually check whether      #
    # your function produces the expected output.   #
    # ----------------------------------------------#

    print(pop_bubbles('acccbba', 3))
    # Should print: abba

    print(pop_bubbles('abbbaa', 3))
    # Should print: (blank line)

    print(pop_bubbles('dddde', 3))
    # Should print: e

    print(pop_bubbles('aabba', 2))
    # Should print: a

    print(pop_bubbles('aabbbaacd', 3))
    # Should print: cd

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#


# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your function, type one of the following commands in the terminal:
# python -m pytest tests/test_q8.py
# python3 -m pytest tests/test_q8.py
