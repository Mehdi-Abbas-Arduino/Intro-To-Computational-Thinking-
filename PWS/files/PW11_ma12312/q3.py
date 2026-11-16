def helper_up(size,index=1,string=''):
    if index > size:
        return string 
    string += ' ' * abs(index-size) + index * '* ' + '\n'
    return helper_up(size,index+1,string)

def helper_down(size,index=None,string=''):
    if index is None:
        index = size - 1
    if index < 1:
        return string
    string += ' ' * abs(index-size) + index * '* ' + '\n'
    return helper_down(size,index-1,string)

def diamond(size):
    upper = helper_up(size)
    lower = helper_down(size)
# -1 removes the newline
    return (upper + lower)[:-1]
# -----------------------------------------#
# TESTING YOUR CODE                        #
# -----------------------------------------#
# The code below runs only when this file is executed directly.
if __name__ == "__main__":

    # ----------------------------------------------#
    # TESTING YOUR CODE ON SAMPLE TEST CASES        #
    # Run this file and manually check whether      #
    # your function produces the expected output.   #
    # Each expected row starts right after the      #
    # "# " prefix (the first space belongs to it).  #
    # ----------------------------------------------#

    print(diamond(1))
    # Should print:
    # *

    print(diamond(2))
    # Should print:
    #  *
    # * *
    #  *

    print(diamond(4))
    # Should print:
    #    *
    #   * *
    #  * * *
    # * * * *
    #  * * *
    #   * *
    #    *

    print(diamond(7))
    # Should print:
    #       *
    #      * *
    #     * * *
    #    * * * *
    #   * * * * *
    #  * * * * * *
    # * * * * * * *
    #  * * * * * *
    #   * * * * *
    #    * * * *
    #     * * *
    #      * *
    #       *

    print(diamond(10))
    # Should print:
    #          *
    #         * *
    #        * * *
    #       * * * *
    #      * * * * *
    #     * * * * * *
    #    * * * * * * *
    #   * * * * * * * *
    #  * * * * * * * * *
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

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#


# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your function, type one of the following commands in the terminal:
# python -m pytest tests/test_q3.py
# python3 -m pytest tests/test_q3.py
