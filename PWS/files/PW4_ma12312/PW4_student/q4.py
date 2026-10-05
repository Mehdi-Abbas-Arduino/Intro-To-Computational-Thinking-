# -----------------------------------------#
# FUNCTION DEFINITION                      #
# -----------------------------------------#

def submission_score(total_tests, required_tests, partial_score, test_results):

    # -----------------------------------------
    # STEP 1: Check whether ALL tests passed
    # -----------------------------------------

    all_passed = True

    # Go through every test result
    for i in range(total_tests):

        # If we find even ONE failed test...
        if test_results[i] == '0':

            # Then not all tests passed
            all_passed = False

            # We don't need to keep checking for this condition
            break

    # If every test passed, the score is 100
    if all_passed:
        return 100


    # -----------------------------------------
    # STEP 2: Check the REQUIRED tests
    # -----------------------------------------

    # Go through only the first required_tests
    for i in range(required_tests):

        # If any required test failed...
        if test_results[i] == '0':

            # The score is 0
            return 0


    # -----------------------------------------
    # STEP 3: Required tests passed,
    # but not ALL tests passed
    # -----------------------------------------

    # Therefore, give the partial score
    return partial_score

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

    print(submission_score(4, 2, 50, "1011"))
    # Should print: 0
     
    print(submission_score(3, 2, 66, "110"))
    # Should print: 66
     
    print(submission_score(4, 2, 50, "1111"))
    # Should print: 100

    print(submission_score(5, 3, 30, "11011"))
    # Should print: 0
    
    print(submission_score(10, 7, 60, "1111101111"))
    # Should print: 0

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#


# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your function, type the following command in the terminal:
# pytest tests/test_q4.py