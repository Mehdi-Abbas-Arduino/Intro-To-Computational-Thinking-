def flatten_eidi(envelope):
    # WRITE YOUR CODE HERE
    if not envelope:
        return []
    
    if type(envelope[0]) == int:
        return [envelope[0]] + flatten_eidi(envelope[1:])
    else:
        return flatten_eidi(envelope[0]) + flatten_eidi(envelope[1:])


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

    print(flatten_eidi([5000]))
    # Should print: [5000]

    print(flatten_eidi([]))
    # Should print: []

    print(flatten_eidi([2000, [3000, 4000]]))
    # Should print: [2000, 3000, 4000]

    print(flatten_eidi([[], [[]], 1000]))
    # Should print: [1000]

    envelope = [10000, [7000, 8000], 9000, [5500, 6000], [4000, 10000, [5500, 5000]]]
    print(flatten_eidi(envelope))
    # Should print: [10000, 7000, 8000, 9000, 5500, 6000, 4000, 10000, 5500, 5000]

    # You may also check that the original envelope remains unchanged.

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#


# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your function, type one of the following commands in the terminal:
# python -m pytest tests/test_q4.py
# python3 -m pytest tests/test_q4.py
