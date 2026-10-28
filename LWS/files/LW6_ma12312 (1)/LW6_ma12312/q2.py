# -----------------------------------------#
# FUNCTION DEFINITION                      #
# -----------------------------------------#

def rotate_message(display_message, rotation_count):
    n = len(display_message)
    rotation_count = rotation_count % n
    if rotation_count > 0:
        return display_message[rotation_count:] + display_message[:rotation_count]
    elif rotation_count < 0:
        return display_message[rotation_count:] + display_message[:rotation_count]
    else:
        return display_message


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

    print(rotate_message('campus', 3))
    # Should print: puscam
     
    print(rotate_message('campus', -2))
    # Should print: uscamp
     
    print(rotate_message('campus', 8))
    # Should print: mpusca
     
    print(rotate_message('campus', -8))
    # Should print: uscamp

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#



# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your function, type the following command in the terminal:
# pytest tests/test_q2.py

x = 'campus'
rotation = 2
length = len(x)
rotation = rotation % length
new_rotation = (length - rotation)
# first = x[:-rotation]
# second = x[-rotation:]
first = x[:new_rotation]
second = x[new_rotation:]

print(second+first)