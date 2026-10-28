# -----------------------------------------#
# FUNCTION DEFINITION                      #
# -----------------------------------------#

def countdown(start_hour, end_hour):
    # WRITE YOUR CODE HERE
        if start_hour == end_hour:
             print(start_hour)
             return 
        else:
             print(start_hour,end=', ')
             countdown(start_hour-1,end_hour)
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

    countdown(5, -3)
    # Should print:
    # 5, 4, 3, 2, 1, 0, -1, -2, -3

    countdown(3, 1)
    # Should print:
    # 3, 2, 1

    countdown(0, 0)
    # Should print:
    # 0

    countdown(-2, -4)
    # Should print:
    # -2, -3, -4

    countdown(7, 7)
    # Should print:
    # 7

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#


# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your function, type one of the following commands in the terminal:
# python -m pytest tests/test_q1.py
# python3 -m pytest tests/test_q1.py
