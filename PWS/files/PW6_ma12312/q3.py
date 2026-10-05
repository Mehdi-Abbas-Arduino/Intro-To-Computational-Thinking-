# -----------------------------------------#
# FUNCTION DEFINITION                      #
# -----------------------------------------#

def can_form_same_word(letters):
    # WRITE YOUR CODE HERE
    if len(letters) % 2 != 0:
        return False
    x = ''
    # anothercount = 0
    for i in range(len(letters)):
        if letters[i] not in x:
            x += letters[i]
            count = 0
            for j in range(len(letters)):
                if letters[i] == letters[j]:
                    count += 1

    if count % 2 == 0:
        return True
    else:
        return False

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

    print(can_form_same_word('baba'))
    # Should print: True

    print(can_form_same_word('cbcba'))
    # Should print: False

    print(can_form_same_word('abca'))
    # Should print: False

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#



# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your function, type the following command in the terminal:
# pytest tests/test_q3.py
