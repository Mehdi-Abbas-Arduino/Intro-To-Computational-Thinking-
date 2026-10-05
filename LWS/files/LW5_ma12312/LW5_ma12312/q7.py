# -----------------------------------------#
# FUNCTION DEFINITION                      #
# -----------------------------------------#

def boost_score(boost_count, starting_score):
    count = starting_score
    for i in range(boost_count):
        total_sum = 0
        for j in range(1,count+1):
            total_sum += j
            count = total_sum
    return count 


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

    print(boost_score(4, 2))
    ''' Should print:
    231
    '''

    print(boost_score(1, 10))
    ''' Should print:
    55
    '''

    print(boost_score(2, 6))
    ''' Should print:
    231
    '''

    print(boost_score(4, 1))
    ''' Should print:
    1
    '''

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#



# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your function, type the following command in the terminal:
# pytest tests/test_q7.py