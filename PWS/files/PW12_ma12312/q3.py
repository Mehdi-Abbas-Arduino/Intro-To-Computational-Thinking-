def partition_modulo_n(divisor, numbers):
    # WRITE YOUR CODE HERE
    if divisor > 0 :
        m = {}
        for i in range(divisor):
            if i not in m :
                m[i] = []
        for d in range(divisor):
            for i in range(len(numbers)):
                if numbers[i] % divisor == d:
                    m[d].append(numbers[i])

        return m
    else: 
        m = {}
        for i in range(divisor+1,1):
            if i not in m :
                m[i] = []
        for d in range(divisor+1,1):
            for i in range(len(numbers)):
                if numbers[i] % divisor == d:
                    m[d].append(numbers[i])

        return m



# -----------------------------------------#
# TESTING YOUR CODE                        #
# -----------------------------------------#
# The code below runs only when this file is executed directly.
if __name__ == "__main__":
    # ----------------------------------------------#
    # TESTING YOUR CODE ON SAMPLE TEST CASES        #
    # Run this file and manually compare the output #
    # with the expected output below.                #
    # ----------------------------------------------#

    divisor = 3
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    print(partition_modulo_n(divisor, numbers))
    # Should print: {0: [0, 3, 6, 9], 1: [1, 4, 7, 10], 2: [2, 5, 8, 11]}

    divisor = 3
    numbers = []
    print(partition_modulo_n(divisor, numbers))
    # Should print: {0: [], 1: [], 2: []}

    divisor = 4
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    print(partition_modulo_n(divisor, numbers))
    # Should print: {0: [0, 4, 8], 1: [1, 5, 9], 2: [2, 6, 10], 3: [3, 7, 11]}

    divisor = -4
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    print(partition_modulo_n(divisor, numbers))
    # Should print: {-3: [1, 5, 9], -2: [2, 6, 10], -1: [3, 7, 11], 0: [0, 4, 8]}

    divisor = -4
    numbers = [-6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
    print(partition_modulo_n(divisor, numbers))
    # Should print: {-3: [-3, 1, 5], -2: [-6, -2, 2], -1: [-5, -1, 3], 0: [-4, 0, 4]}

    print(partition_modulo_n(3, [4, 7, -2]))
    # Should print: {0: [], 1: [4, 7, -2], 2: []}

    print(partition_modulo_n(-4, [-6, -5, -4, -3, -2, -1, 0, 1]))
    # Should print: {-3: [-3, 1], -2: [-6, -2], -1: [-5, -1], 0: [-4, 0]}

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#


# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your function, type one of the following commands in the terminal:
# python -m pytest tests/test_q3.py
# python3 -m pytest tests/test_q3.py
