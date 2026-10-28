# -----------------------------------------#
# FUNCTION DEFINITION                      #
# -----------------------------------------#

def riffle_shuffle(t):
    # WRITE YOUR CODE HERE
    x = len(t) // 2
    first = t[:x]
    second = t[x:]
    while True:
        s = []
        # if len(t) % 2 != 0:
        #     for i in range(0,len(t)):
        #         if i % 2 != 0 :
        #             s.append(second[i])
        #             s.append(first[i])            
        for i in range(0,len(first)):
                s.append(second[i])
                s.append(first[i])
        break
    t[:] = s

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

    t = [
        "aardvark", "buffalo", "crocodile", "dingo",
        "elephant", "fox", "gorilla", "hippopotamus"
    ]
    print(riffle_shuffle(t))
    # Should print: None
    print(t)
    # Should print:
    # ['elephant', 'aardvark', 'fox', 'buffalo',
    #  'gorilla', 'crocodile', 'hippopotamus', 'dingo']

    print()

    t = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(riffle_shuffle(t))
    # Should print: None
    print(t)
    # Should print: [6, 1, 7, 2, 8, 3, 9, 4, 10, 5]

    print()

    t = [1, 2]
    print(riffle_shuffle(t))
    # Should print: None
    print(t)
    # Should print: [2, 1]

    print()

    t = [1, 2, 3, 4]
    print(riffle_shuffle(t))
    # Should print: None
    print(t)
    # Should print: [3, 1, 4, 2]

    print()

    t = [10, 20, 30, 40, 50, 60]
    print(riffle_shuffle(t))
    # Should print: None
    print(t)
    # Should print: [40, 10, 50, 20, 60, 30]

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#



# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your function, type one of the following commands in the terminal:
# python -m pytest tests/test_q5.py
# python3 -m pytest tests/test_q5.py