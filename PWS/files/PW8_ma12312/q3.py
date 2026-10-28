# -----------------------------------------#
# FUNCTION DEFINITION                      #
# -----------------------------------------#

def minimum_replacements(words):
    initials = []

    for i in range(len(words)):
        count = 0
        j = 0

        while j < len(words[i]) - 1:
            if words[i][j] == words[i][j + 1]:
                count += 1
                j += 2
            else:
                j += 1

        initials.append(count)

    return initials
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

    print(minimum_replacements(["ab", "aab", "abb", "abab", "abaaaba"]))
    # Should print: [0, 1, 1, 0, 1]

    print(minimum_replacements(["aa"]))
    # Should print: [1]

    print(minimum_replacements(["aaaaaa"]))
    # Should print: [3]

    print(minimum_replacements(["abababab"]))
    # Should print: [0]

    print(minimum_replacements(["aabbcc"]))
    # Should print: [3]

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#



# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your function, type one of the following commands in the terminal:
# python -m pytest tests/test_q3.py
# python3 -m pytest tests/test_q3.py