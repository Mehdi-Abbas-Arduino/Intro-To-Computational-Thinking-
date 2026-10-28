# -----------------------------------------#
# FUNCTION DEFINITION                      #
# -----------------------------------------#


def noisy_neighbors(words):
    lst = []
    positions = []

    for i in range(len(words)):
        if words[i].isupper():
            if i > 0 and i - 1 not in positions:
                positions.append(i - 1)

            if i < len(words) - 1 and i + 1 not in positions:
                positions.append(i + 1)

    for i in range(len(words)):
        if i in positions:
            lst.append(words[i])

    return lst




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

    print(noisy_neighbors(
        ['how', 'much', 'wood', 'would', 'a', 'woodchuck', 'chuck',
         'if', 'a', 'woodchuck', 'could', 'chuck', 'wood']
    ))
    # Should print: []

    print(noisy_neighbors(
        ['how', 'much', 'wood', 'would', 'a', 'woodchuck', 'chuck',
         'if', 'a', 'woodchuck', 'COULD', 'chuck', 'wood']
    ))
    # Should print: ['woodchuck', 'chuck']

    print(noisy_neighbors(
        ['how', 'much', 'wood', 'would', 'a', 'WOODCHUCK', 'CHUCK',
         'if', 'a', 'woodchuck', 'could', 'CHUCK', 'WOOD']
    ))
    # Should print: ['a', 'WOODCHUCK', 'CHUCK', 'if', 'could', 'CHUCK', 'WOOD']

    print(noisy_neighbors(
        ['HOW', 'much', 'WOOD', 'would', 'a', 'woodchuck', 'chuck',
         'if', 'a', 'woodchuck', 'could', 'chuck', 'wood']
    ))
    # Should print: ['much', 'would']

    print(noisy_neighbors(
        ['HOW', 'much', 'wood', 'WOULD', 'A', 'woodchuck', 'CHUCK',
         'if', 'a', 'woodchuck', 'COULD', 'chuck', 'wood']
    ))
    # Should print: ['much', 'wood', 'WOULD', 'A', 'woodchuck', 'if', 'woodchuck', 'chuck']

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#



# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your function, type the following command in the terminal:
# python -m pytest tests/test_q5.py
# python3 -m pytest tests/test_q5.py