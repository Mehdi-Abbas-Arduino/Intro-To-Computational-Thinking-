# -----------------------------------------#
# FUNCTION DEFINITION                      #
# -----------------------------------------#

def is_prime(number):

    # WRITE YOUR CODE HERE
    if number == 1 :
        return False
    if number == 2 :
        return True 
    
    for i in range(2,number):
        if number % i == 0:
            return False
    return True 


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

    print(is_prime(3))
    # Should print: True
    
    print(is_prime(8))
    # Should print: False

    print(is_prime(36))
    # Should print: False

    print(is_prime(51))
    # Should print: False

    print(is_prime(107))
    # Should print: True

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#


# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your function, type the following command in the terminal:
# pytest tests/test_q2.py