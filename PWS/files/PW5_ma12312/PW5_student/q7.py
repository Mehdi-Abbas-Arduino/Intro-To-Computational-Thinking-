# -----------------------------------------#
# FUNCTION DEFINITION                      #
# -----------------------------------------#

def print_spaces(space_count):
    # prints space_count spaces
    for index in range(space_count):
        print(" ", end="")


def print_stars(star_count):
    # prints star_count space-separated stars
    for index in range(1,star_count+1):
        print("* ", end="")
    print()


def print_pyramid(height):
    # prints a pyramid of the given height
    for row_number in range(height):
        space_count = (height - row_number) - 1
        print_spaces(space_count)
        star_count = height - space_count
        print_stars(star_count)


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

    print_pyramid(5)
    ''' Should print:
        *
       * *
      * * *
     * * * *
    * * * * *
    '''

    print_pyramid(3)
    ''' Should print:
      *
     * *
    * * *
    '''

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#



# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your function, type the following command in the terminal:
# pytest tests/test_q7.py
