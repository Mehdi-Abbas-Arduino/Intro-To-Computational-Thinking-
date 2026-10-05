# -----------------------------------------#
# FUNCTION DEFINITION                      #
# -----------------------------------------#

def print_code_permutations(team_code):
    # WRITE YOUR CODE HERE
    n = len(team_code)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if i!=j and i != k and j != i and j != k and k != i and k != j :
                    code = team_code [i] + team_code[j] + team_code[k]
                    print(code,end=' ')
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

    print_code_permutations("ABC")
    ''' Should print all six arrangements on one line, separated by one space.
    One valid ordering is:
    ABC ACB BAC BCA CAB CBA
    The ordering may vary.
    '''

    print_code_permutations("XYA")
    ''' Should print all six arrangements on one line, separated by one space.
    One valid ordering is:
    XYA XAY YXA YAX AXY AYX
    The ordering may vary.
    '''

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#



# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your function, type the following command in the terminal:
# pytest tests/test_q8.py
