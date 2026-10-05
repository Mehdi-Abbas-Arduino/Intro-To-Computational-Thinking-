# -----------------------------------------#
# FUNCTION DEFINITION                      #
# -----------------------------------------#

def replace_not_bad(text):
    # WRITE YOUR CODE HERE
    pass


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

    print(replace_not_bad('This dinner is not that bad!'))
    # Should print: This dinner is good!

    print(replace_not_bad('Maula Jatt is awesome.'))
    # Should print: Maula Jatt is awesome.

    print(replace_not_bad('Cheating is not my cup of tea.'))
    # Should print: Cheating is not my cup of tea.

    print(replace_not_bad('Babar was not a badminton player growing up in Islamabad.'))
    # Should print: Babar was goodminton player growing up in Islamabad.

    print(replace_not_bad('Not every Badshah is a Maharaja.'))
    # Should print: Goodshah is a Maharaja.

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#



# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your function, type the following command in the terminal:
# pytest tests/test_q7.py
