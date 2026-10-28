# -----------------------------------------#
# FUNCTION DEFINITION                      #
# -----------------------------------------#


def pop_bubbles(bubbles, k):
    changed = True

    while changed:
        changed = False
        i = 0

        while i < len(bubbles):
            count = 1
            j = i + 1

            while j < len(bubbles) and bubbles[j] == bubbles[i]:
                count += 1
                j += 1

            if count >= k:
                for _ in range(count):
                    bubbles.pop(i)

                changed = True
                break
            else:
                i = j

    return bubbles

                


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

    print(pop_bubbles([1, 3, 3, 3, 2, 2, 1], 3))
    # Should print: [1, 2, 2, 1]

    print(pop_bubbles([1, 2, 2, 2, 1, 1], 3))
    # Should print: []

    print(pop_bubbles([6, 1, 1, 6, 6, 1, 1, 1, 6, 6, 6], 3))
    # Should print: [6, 1, 1]

    print(pop_bubbles([1, 2, 2, 1], 2))
    # Should print: []

    print(pop_bubbles([7, 7, 7, 7], 3))
    # Should print: []

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#



# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your function, type one of the following commands in the terminal:
# python -m pytest tests/test_q6.py
# python3 -m pytest tests/test_q6.py