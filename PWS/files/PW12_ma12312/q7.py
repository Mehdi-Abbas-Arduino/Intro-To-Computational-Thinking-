# -----------------------------------------#
# FUNCTION DEFINITIONS                     #
# -----------------------------------------#


def greedy_knapsack(items, capacity):
    # WRITE YOUR CODE HERE
    # lis = []
    sorted_items = dict(sorted(items.items(), key=lambda x: x[1][0], reverse=True))    
    total_value = 0
    remaining_capacity = capacity
    for k, v in sorted_items.items():
        value = v[0]
        weight = v[1]
        if weight <= remaining_capacity:
            total_value += value
            remaining_capacity -= weight
    return total_value


def main():
    # WRITE YOUR CODE HERE
    x = int(input())
    di = {}
    for i in range(x):
        item,value,weight = input().split()
        value = int(value)
        weight = int(weight)
        di[item] = [value,weight]
    capacity = int(input())
    x = greedy_knapsack(di,capacity)
    print(x)


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

    main()
    # Enter these lines when prompted:
    # 6
    # clock 55 5
    # painting 90 9
    # toaster 20 4
    # vase 50 2
    # book 10 1
    # desktop 150 15
    # 20
    # Should print:
    # 205

    print()

    main()
    # Enter these lines when prompted:
    # 3
    # clock 55 5
    # painting 90 9
    # toaster 20 4
    # 10
    # Should print:
    # 90

    print()

    main()
    # Enter these lines when prompted:
    # 5
    # clock 35 5
    # painting 40 5
    # TV 100 10
    # desktop 150 15
    # lamp 20 2
    # 30
    # Should print:
    # 290

    print()

    main()
    # Enter these lines when prompted:
    # 6
    # clock 35 5
    # painting 40 5
    # TV 100 10
    # desktop 150 15
    # lamp 20 2
    # book 4 1
    # 0
    # Should print:
    # 0

    # ----------------------------------------------#
    # YOU CAN DO FURTHER CUSTOM TESTING BELOW       #
    # ----------------------------------------------#

    # In order to test your function, run:
    # python -m pytest tests/test_q7.py
    # python3 -m pytest tests/test_q7.py
