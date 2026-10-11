# -----------------------------------------#
# FUNCTION DEFINITION                      #
# -----------------------------------------#




def clean_walkway(walkway):
    """Process volunteers from left to right.
    Each volunteer checks right for litter first.
    If there is no litter on the right, check left.
    Replace one piece of litter with E if found.
    Return the final walkway as a string. 
    """

    string = list(walkway)

    for i in range(len(string)):
        if string[i] == 'V':
            if i + 1 < len(string) and string[i + 1] == 'L':
                string[i + 1] = 'E'
            elif i > 0 and string[i - 1] == 'L':
                string[i - 1] = 'E'

    return ''.join(string)


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

    print(clean_walkway('LVLEL'))
    # Should print: LVEEL
     
    print(clean_walkway('VLLVE'))
    # Should print: VEEVE

    print(clean_walkway("LLLLL"))
    # Should print: LLLLL

    print(clean_walkway("VVVV"))
    # Should print: VVVV

    print(clean_walkway("LVLVLV"))
    # Should print: LVEVEV

    print(clean_walkway("LLLV"))
    # Should print: LLEV

    print(clean_walkway("VLLL"))
    # Should print: VELL

    print(clean_walkway("LVLELVLEVL"))
    # Should print: LVEELVEEVE

    print(clean_walkway("LLLLLVVVVV"))
    # Should print: LLLLEVVVVV

    print(clean_walkway("EVVEVLELV"))
    # Should print: EVVEVEEEV

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#



# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your function, type the following command in the terminal:
# pytest tests/test_q4.py