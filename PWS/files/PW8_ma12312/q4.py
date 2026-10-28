# -----------------------------------------#
# FUNCTION DEFINITIONS                     #
# -----------------------------------------#

def prime_factors(num):
    # WRITE YOUR CODE HERE
    lst = []
    i = 2
    while num != 1:
        if num % i == 0 :
            lst.append(i)
            num = num // i
            i = 2
        else:
            i += 1

    return lst


def special_numbers(num):
    # WRITE YOUR CODE HERE
    lst = []
    for i in range(1,num+1):
        x = prime_factors(i)
        y = sum(x)
        if y == i:
            lst.append(i)
    return lst



# -----------------------------------------#
# TESTING YOUR CODE                        #
# -----------------------------------------#
# The code below runs only when this file is executed directly.
if __name__ == "__main__":

    # ----------------------------------------------#
    # TESTING YOUR CODE ON VISIBLE TEST CASES       #
    # Run this file and manually check whether      #
    # your functions produce the expected output.   #
    # ----------------------------------------------#

    print(prime_factors(6552))
    # Should print: [2, 2, 2, 3, 3, 7, 13]

    print(prime_factors(1567))
    # Should print: [1567]

    print(prime_factors(1))
    # Should print: []

    print(special_numbers(25))
    # Should print: [2, 3, 4, 5, 7, 11, 13, 17, 19, 23]

    print(prime_factors(36))
    # Should print: [2, 2, 3, 3]

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#



# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your functions, type one of the following commands in the terminal:
# python -m pytest tests/test_q4.py
# python3 -m pytest tests/test_q4.py