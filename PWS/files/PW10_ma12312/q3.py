# -----------------------------------------#
# FUNCTION DEFINITIONS                     #
# -----------------------------------------#
def helper(last_number,index=1):
    if type(last_number) != int:
        print("Error: last_number must be a positive integer.")
        return
    if last_number <= 0:
        print("Error: last_number must be a positive integer.")
        return
    if last_number == index:
        if index % 5 == 0:
            print("Buzz")
            # index += 1
        else:
            print(index)
        return
    else:
        if index % 5 == 0:
            print("Buzz",end=', ')
            # index += 1
        else:
            print(index,end=', ')
        helper(last_number,index+1)
        # if index > last_number:
        #     return

def count_buzz(last_number):
    # WRITE YOUR CODE HERE
    helper(last_number)


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

    count_buzz(3)
    # Should print:
    # 1, 2, 3

    count_buzz(13)
    # Should print:
    # 1, 2, 3, 4, Buzz, 6, 7, 8, 9, Buzz, 11, 12, 13

    count_buzz(20)
    # Should print:
    # 1, 2, 3, 4, Buzz, 6, 7, 8, 9, Buzz, 11, 12, 13, 14, Buzz, 16, 17, 18, 19, Buzz

    count_buzz(-13)
    # Should print:
    # Error: last_number must be a positive integer.

    count_buzz('thirteen')
    # Should print:
    # Error: last_number must be a positive integer.

    count_buzz(5)
    # Should print:
    # 1, 2, 3, 4, Buzz

    count_buzz(1)
    # Should print:
    # 1

    count_buzz(0)
    # Should print:
    # Error: last_number must be a positive integer.

    count_buzz(-3)
    # Should print:
    # Error: last_number must be a positive integer.

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#


# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your function, type one of the following commands:
# python -m pytest tests/test_q3.py
# python3 -m pytest tests/test_q3.py
