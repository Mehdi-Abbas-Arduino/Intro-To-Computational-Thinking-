# -----------------------------------------#
# FUNCTION DEFINITION                      #
# -----------------------------------------#

def same_pattern(original_message, encoded_message):
    # WRITE YOUR CODE HERE
    first = 0
    second = 0
    new = ''
    for i in range(len(original_message)):
        for j in range(len(original_message)):
            if original_message[i] == original_message[j]:
                first += 1
    for i in range(len(encoded_message)):
            for j in range(len(encoded_message)):
                if encoded_message[i] == encoded_message[j]:
                    second += 1

    if len(original_message) != len(encoded_message):
         return False
    if first == second:
        for i in range(len(original_message)):
            for j in range(len(original_message)):
                if original_message[i] == original_message[j]: # abb same repetion should be map with same reptition
                    if encoded_message[i] != encoded_message[j]: # cdc
                        return False

                if original_message[i] != original_message[j]: # cdc
                    if encoded_message[i] == encoded_message[j]: # abb 
                        return False

        return True
    if first == 0 and second == 0:
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

    print(same_pattern('foo', 'bar'))
    # Should print: False

    print(same_pattern('egg', 'add'))
    # Should print: True

    print(same_pattern('ab', 'cc'))
    # Should print: False

    print(same_pattern('aabb', 'ccdd'))
    # Should print: True

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#



# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your function, type the following command in the terminal:
# pytest tests/test_q5.py
