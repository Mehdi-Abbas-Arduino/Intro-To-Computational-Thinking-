# -----------------------------------------#
# FUNCTION DEFINITION                      #
# -----------------------------------------#
def decode_message(encoded_text):

    name = ""
    i = 0
    j = 0

    while j < len(encoded_text):
        if encoded_text[j].isdigit():
            i += int(encoded_text[j])
            name += encoded_text[i]
        j += 1

    return name
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

    print(decode_message('2qc2a3zt'))
    # Should print: cat

    print(decode_message('xgo11'))
    # Should print: go

    print(decode_message('H0zi3'))
    # Should print: Hi

    print(decode_message('1a2 2b'))
    # Should print: a b

    print(decode_message('habib'))
    # Should print: 

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#



# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your function, type the following command in the terminal:
# pytest tests/test_q2.py
