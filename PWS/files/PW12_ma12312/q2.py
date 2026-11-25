def price_check(products, product_prices, sold_products, sold_prices):
    m = {}
    m2 = {}
    count = 0
    for i in range(len(products)):
        m[products[i]] = product_prices[i]

    for j in range(len(sold_products)):
        if sold_products[j] not in m2:
            m2[sold_products[j]] = []
        m2[sold_products[j]].append(sold_prices[j])

    for k, v in m2.items():
        for price in v:
            if price != m[k]:
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

    products = ['rice', 'sugar', 'wheat', 'cheese']
    product_prices = [16.89, 56.92, 20.89, 345.99]
    sold_products = ['rice', 'cheese']
    sold_prices = [18.99, 400.89]
    print(price_check(products, product_prices, sold_products, sold_prices))
    # Should print: 2

    products = ['chocolate', 'cheese', 'tomato']
    product_prices = [15.0, 300.9, 23.44]
    sold_products = ['cheese', 'tomato', 'chocolate']
    sold_prices = [300.9, 23.44, 10.0]
    print(price_check(products, product_prices, sold_products, sold_prices))
    # Should print: 1

    products = ['toaster',
     'marker',
     'sanitizer',
     'tracks',
     'bottle',
     'stand',
     'adapter',
     'staple',
     'water',
     'wires']
    product_prices = [100.78212688799995,
     20.066673702062374,
     94.83868838020052,
     76.81190517349611,
     86.92530793466595,
     52.4514871306522,
     54.26374289000169,
     96.56913611950449,
     6.690542660921505,
     17.172357298482286]
    sold_products = ['stand',
     'staple',
     'water',
     'wires',
     'bottle',
     'marker',
     'sanitizer',
     'adapter',
     'toaster',
     'tracks']
    sold_prices = [52.4514871306522,
     96.56913611950449,
     6.690542660921505,
     50.01372431999727,
     86.92530793466595,
     20.066673702062374,
     94.83868838020052,
     88.03965413375478,
     100.78212688799995,
     76.81190517349611]
    print(price_check(products, product_prices, sold_products, sold_prices))
    # Should print: 2

    print(price_check(
        ['chocolate', 'cheese', 'tomato'],
        [15.00, 300.90, 23.44],
        ['chocolate', 'cheese', 'tomato'],
        [15, 300.90, 10.00]))
    # Should print: 1

    print(price_check(
        ['eggs', 'milk', 'cheese'],
        [2.89, 3.29, 5.79],
        ['eggs', 'eggs', 'cheese', 'milk'],
        [2.89, 2.99, 5.97, 3.29]))
    # Should print: 2

    print(price_check(['milk'], [3.29], [], []))
    # Should print: 0

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#


# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your function, type one of the following commands in the terminal:
# python -m pytest tests/test_q2.py
# python3 -m pytest tests/test_q2.py
