# -----------------------------------------#
# FUNCTION DEFINITION                      #
# -----------------------------------------#

def countdown(starting_floor, ending_floor):
    # starting_floor,ending_floor = int(starting_floor),int(ending_floor)
    if type(starting_floor) == int and type(ending_floor) == int:
        for i in range(starting_floor,ending_floor-1,-1):
            if i != ending_floor:
                print(i,end=', ')
            else:
                print(i)
        
    else:
        print("Error: bad argument. countdown is defined for integers only.")


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

    countdown(5, 2)
    # Should print: 5, 4, 3, 2

    countdown(4, -3)
    # Should print: 4, 3, 2, 1, 0, -1, -2, -3

    countdown(-1, -5)
    # Should print: -1, -2, -3, -4, -5

    countdown(3.0, -4)
    # Should print: Error: bad argument. countdown is defined for integers only.

    countdown(3, -4.5)
    # Should print: Error: bad argument. countdown is defined for integers only.

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#



# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your function, type the following command in the terminal:
# pytest tests/test_q1.py