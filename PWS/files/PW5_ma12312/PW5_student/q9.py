# -----------------------------------------#
# FUNCTION DEFINITION                      #
# -----------------------------------------#

def print_prime_ids(start_id, end_id):

    first =  True

    for i in range(start_id, end_id + 1):

        if i < 2:
            continue

        count = 0

        for j in range(1, i + 1):
            if i % j == 0:
                count += 1

        if count == 2:
            if not first:
                print(", ", end="")

            print(i, end="")
            first = False
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

    print_prime_ids(1, 10)
    ''' Should print:
    2, 3, 5, 7
    '''

    print_prime_ids(3, 5)
    ''' Should print:
    3, 5
    '''

    print_prime_ids(20, 30)
    ''' Should print:
    23, 29
    '''

    print_prime_ids(14, 16)
    ''' Should print nothing.
    '''

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#



# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your function, type the following command in the terminal:
# pytest tests/test_q9.py
