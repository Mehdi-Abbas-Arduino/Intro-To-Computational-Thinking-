# -----------------------------------------#
# FUNCTION DEFINITION                      #
# -----------------------------------------#

def print_led_channels(row_count):
    # WRITE YOUR CODE HERE
    count = 1
    for i in range(1,row_count+1):
        for j in range(1,2*i): # we need to stop work till n - 1 so to get an odd number we need to work till 2*i
            print(count,end=' ')
            count += 1
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

    print_led_channels(3)
    ''' Should print:
    1
    2 3 4
    5 6 7 8 9
    '''

    print_led_channels(1)
    ''' Should print:
    1
    '''

    print_led_channels(6)
    ''' Should print:
    1
    2 3 4
    5 6 7 8 9
    10 11 12 13 14 15 16
    17 18 19 20 21 22 23 24 25
    26 27 28 29 30 31 32 33 34 35 36
    '''

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#



# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your function, type the following command in the terminal:
# pytest tests/test_q3.py
