def is_winning_ticket(ticket_number):
    def helper(number, div1=1, pos=0):
        if number // div1 >= 10 :
            return helper(number,div1*10,pos)

        digit = number // div1

        if pos % 2 == 0:
            if digit %2 != 0:
                return False
        else:
            if digit %2 == 0:
                return False
        if div1 == 1 :
            return True

        return helper(number % div1, div1 // 10 ,pos +1)
    return helper(ticket_number)

    





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

    print(is_winning_ticket(2345))
    # Should print: True

    print(is_winning_ticket(3245))
    # Should print: False

    print(is_winning_ticket(2582))
    # Should print: False

    print(is_winning_ticket(7))
    # Should print: False

    print(is_winning_ticket(2))
    # Should print: True

    print(is_winning_ticket(4101))
    # Should print: True

    print(is_winning_ticket(22))
    # Should print: False

    print(is_winning_ticket(23))
    # Should print: True

    print(is_winning_ticket(230))
    # Should print: True

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#


# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your function, type one of the following commands in the terminal:
# python -m pytest tests/test_q5.py
# python3 -m pytest tests/test_q5.py
