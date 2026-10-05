# -----------------------------------------#
# FUNCTION DEFINITION                      #
# -----------------------------------------#

def collatz_sequence(starting_number):
    # WRITE YOUR CODE HERE
    current = starting_number
    line = ''
    while True:
        if current in (1,5,17):
            line = line + str(current)
            break
        line = line + str(current) + ', '
  
        if current % 2 == 0:
            current = current // 2
        elif current % 2 != 0:
            current = (3 * current) - 1
    print(line)
    
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

    collatz_sequence(1)
    # Should print: 1

    collatz_sequence(3)
    # Should print: 3, 8, 4, 2, 1

    collatz_sequence(8)
    # Should print: 8, 4, 2, 1

    collatz_sequence(14)
    # Should print: 14, 7, 20, 10, 5

    collatz_sequence(17)
    # Should print: 17

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#
    


# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your function, type the following command in the terminal:
# pytest tests/test_q3.py