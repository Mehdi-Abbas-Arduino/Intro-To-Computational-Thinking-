# -----------------------------------------#
# FUNCTION DEFINITION                      #
# -----------------------------------------#

def lucky_ticket(ticket_number):

    while ticket_number > 0:

        n = ticket_number % 10

        if n == 0 or n == 5:
            return "Yes"

        ticket_number = ticket_number // 10

    return "No"
        

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

    print(lucky_ticket(101))
    # Should print: Yes

    print(lucky_ticket(119))
    # Should print: No

    print(lucky_ticket(158))
    # Should print: Yes

    print(lucky_ticket(291))
    # Should print: No

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#


# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your function, type the following command in the terminal:
# pytest tests/test_q5.py