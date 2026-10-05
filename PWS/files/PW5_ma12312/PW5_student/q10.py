# -----------------------------------------#
# FUNCTION DEFINITION                      #
# -----------------------------------------#

def is_lucky_code(entry_code):
    n = entry_code
    reversed_num = 0
    
    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n = n // 10
        
    differences = 0
    a = entry_code
    b = reversed_num

    while a > 0:
        digit1 = a % 10
        digit2 = b % 10

        if digit1 != digit2:
            differences  += 1

        a = a // 10
        b = b // 10

    if differences <= 2:
        return "YES"
    else:
        return "NO"
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

    print(is_lucky_code(213212))
    ''' Should print:
    YES
    '''

    print(is_lucky_code(218812))
    ''' Should print:
    YES
    '''

    print(is_lucky_code(121212))
    ''' Should print:
    NO
    '''

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#



# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your function, type the following command in the terminal:
# pytest tests/test_q10.py
