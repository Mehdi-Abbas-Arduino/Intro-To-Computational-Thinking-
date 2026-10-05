# -----------------------------------------#
# FUNCTION DEFINITION                      #
# -----------------------------------------#

def word_mood(word):
    # WRITE YOUR CODE HERE
    vowels = ('a','e','i','o','u')
    for i in range(len(word)-2):
        if word[i] in vowels:
            if word[i+1] in vowels:
                if word[i+2] in vowels:
                    return "Happy"
    return "Sad"


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

    print(word_mood("abxy"))
    # Should print: Sad

    print(word_mood('abcdeeafg'))
    # Should print: Happy

    print(word_mood('aeiou'))
    # Should print: Happy

    print(word_mood("abedfeg"))
    # Should print: Sad

    print(word_mood("ewkiaou"))
    # Should print: Happy

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#



# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your function, type the following command in the terminal:
# pytest tests/test_q4.py