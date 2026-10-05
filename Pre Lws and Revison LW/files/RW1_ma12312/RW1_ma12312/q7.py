# -----------------------------------------#
# FUNCTION DEFINITION                      #
# -----------------------------------------#

def triangle_number_sequence(term_count):
    # WRITE YOUR CODE HERE
    
    for i in range(1,term_count):
        sequence = ((i*(i+1)) / 2)
        print(sequence,end=', ')
    print()

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

    triangle_number_sequence(1)
    # Should print: 1

    triangle_number_sequence(4)
    # Should print: 1, 3, 6, 10

    triangle_number_sequence(3)
    # Should print: 1, 3, 6

    triangle_number_sequence(20)
    # Should print: 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#
    

# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your function, type the following command in the terminal:
# pytest tests/test_q3.py