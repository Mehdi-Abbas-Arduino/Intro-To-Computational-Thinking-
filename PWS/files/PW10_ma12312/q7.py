# -----------------------------------------#
# FUNCTION DEFINITIONS                     #
# -----------------------------------------#
def helper(n,index=1):
    if index > n:
        return
    helper(n,index+1)
    print(' ' * abs((index - n)) +'* '* index)
    
    


def cup(n):
    # WRITE YOUR CODE HERE
    helper(n)
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

    cup(2)
    # Should print:
    # * *
    #  *

    cup(4)
    # Should print:
    # * * * *
    #  * * *
    #   * *
    #    *

    cup(7)
    # Should print:
    # * * * * * * *
    #  * * * * * *
    #   * * * * *
    #    * * * *
    #     * * *
    #      * *
    #       *

    cup(10)
    # Should print:
    # * * * * * * * * * *
    #  * * * * * * * * *
    #   * * * * * * * *
    #    * * * * * * *
    #     * * * * * *
    #      * * * * *
    #       * * * *
    #        * * *
    #         * *
    #          *

    cup(15)
    # Should print:
    # * * * * * * * * * * * * * * *
    #  * * * * * * * * * * * * * *
    #   * * * * * * * * * * * * *
    #    * * * * * * * * * * * *
    #     * * * * * * * * * * *
    #      * * * * * * * * * *
    #       * * * * * * * * *
    #        * * * * * * * *
    #         * * * * * * *
    #          * * * * * *
    #           * * * * *
    #            * * * *
    #             * * *
    #              * *
    #               *

    cup(1)
    # Should print:
    # *

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#

# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your function, type one of the following commands:
# python -m pytest tests/test_q7.py
# python3 -m pytest tests/test_q7.py
