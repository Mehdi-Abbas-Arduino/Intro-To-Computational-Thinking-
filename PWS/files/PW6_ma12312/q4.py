# -----------------------------------------#
# FUNCTION DEFINITION                      #
# -----------------------------------------#

def minimum_reversals(binary_string):
    # WRITE YOUR CODE HERE
    count = 0 
    for i in range(len(binary_string) - 1):
        if binary_string[i] == '1' and binary_string[i + 1] == '0':
            count += 1
    return count

    


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

    print(minimum_reversals('00111'))
    # Should print: 0

    print(minimum_reversals('111000'))
    # Should print: 1

    print(minimum_reversals('010101'))
    # Should print: 2

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#



# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your function, type the following command in the terminal:
# pytest tests/test_q4.py
