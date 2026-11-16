# def add_check_digit(idnum,add=0,id=None):
#     # WRITE YOUR CODE HERE
#     if id == 0:
#         div = add % 7
#         idnum = (idnum*10) + div
#         return idnum
#     else:
#         if id is None:
#             id = idnum
#         digit = id % 10
#         id = id // 10
#         add += digit ** 2
#         return add_check_digit(idnum,add,id)

def sum_squares(idnum):
    if idnum == 0:
        return 0

    digit = idnum % 10
    return digit ** 2 + sum_squares(idnum // 10)


def add_check_digit(idnum):
    check_digit = sum_squares(idnum) % 7
    return idnum * 10 + check_digit

def verify_check_digit(idnum):
    # WRITE YOUR CODE HERE
    original_id = idnum // 10
    return idnum == add_check_digit(original_id)
# -----------------------------------------#
# TESTING YOUR CODE                        #
# -----------------------------------------#
# The code below runs only when this file is executed directly.
if __name__ == "__main__":

    # ----------------------------------------------#
    # TESTING YOUR CODE ON SAMPLE TEST CASES        #
    # Run this file and manually check whether      #
    # your function produces the expected output.   #
    # ----------------------------------------------#

    print(add_check_digit(7172))
    # Should print: 71725

    print(add_check_digit(92011))
    # Should print: 920113

    print(verify_check_digit(313370))
    # Should print: True

    print(verify_check_digit(678291))
    # Should print: False

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#


# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your function, type one of the following commands in the terminal:
# python -m pytest tests/test_q2.py
# python3 -m pytest tests/test_q2.py
