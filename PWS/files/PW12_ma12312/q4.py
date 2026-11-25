def num_toppings(toppings, budget):
    # WRITE YOUR CODE HERE
    count = 0
    lis = []
    lis2 = []
    for k , v in toppings.items():
        if k not in lis:
            lis.append(k)
            lis2.append(v)
    for i in range(len(lis)):
        for j in range(i+1,len(lis)):
            for z in range(j+1,len(lis)):
                x = lis2[i] + lis2[j] + lis2[z]
                if x <= budget:
                    count += 1
    return count 




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

    toppings = {
        'olives': 250,
        'chicken': 350,
        'onions': 150,
        'tomatoes': 200,
        'pineapple': 300
    }

    print(num_toppings(toppings, 700))
    # Should print: 4

    print(num_toppings(toppings, 400))
    # Should print: 0

    print(num_toppings({'olives': 100, 'onions': 150, 'tomatoes': 200}, 450))
    # Should print: 1

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#


# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your function, type one of the following commands in the terminal:
# python -m pytest tests/test_q4.py
# python3 -m pytest tests/test_q4.py
