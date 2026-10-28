# -----------------------------------------#
# FUNCTION DEFINITION                      #
# -----------------------------------------#

def hindu_shuffle(deck, cut_size):
    # WRITE YOUR CODE HERE
    lst = []
    lst2 = []
    first = 0
    for i in range(0,len(deck),cut_size):
        lst.append(deck[first:cut_size+i])
        first = cut_size + i

    lst = lst[::-1]
    for row in lst:
        for col in row:
            lst2.append(col)

    return lst2



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

    print(hindu_shuffle([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3))
    # Should print: [10, 7, 8, 9, 4, 5, 6, 1, 2, 3]

    print(hindu_shuffle([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 12))
    # Should print: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    print(hindu_shuffle(['aardvark', 'buffalo', 'crocodile', 'dingo', 'elephant', 'fox', 'gorilla', 'hippopotamus'], 4))
    # Should print: ['elephant', 'fox', 'gorilla', 'hippopotamus', 'aardvark', 'buffalo', 'crocodile', 'dingo']

    print(hindu_shuffle([1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096], 1))
    # Should print: [4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]

    print(hindu_shuffle([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584], 5))
    # Should print: [987, 1597, 2584, 89, 144, 233, 377, 610, 8, 13, 21, 34, 55, 1, 1, 2, 3, 5]

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#



# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your function, type the following command in the terminal:
# python -m pytest tests/test_q6.py
# python3 -m pytest tests/test_q6.py