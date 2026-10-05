# -----------------------------------------#
# FUNCTION DEFINITION                      #
# -----------------------------------------#

def event_code(event_message):
    # WRITE YOUR CODE HERE
    code = ""
    for i in range(len(event_message)):
        position = i + 1
        if position % 3 == 0 or position % 5 == 0:
            code += event_message[i]
    return code


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

    print(event_code("123456789012345678901234567890"))
    # Should print: 35690258014570

    print(event_code("pomegranate"))
    # Should print: mgrat

    print(event_code("Burqa Avenger"))
    # Should print: ra ene

    print(event_code("racecar"))
    # Should print: cca

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#



# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your function, type the following command in the terminal:
# pytest tests/test_q1.py