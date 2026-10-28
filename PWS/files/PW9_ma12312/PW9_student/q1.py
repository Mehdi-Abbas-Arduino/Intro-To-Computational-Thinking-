# -----------------------------------------#
# FUNCTION DEFINITIONS                     #
# -----------------------------------------#

def compute_my_bill(purchased_items):
    # WRITE YOUR CODE HERE
    purchase = []
    for i in range(len(purchased_items)):
        price = 0
        quantity = 0
        for j in range(len(purchased_items[i])):
            if j == 1:
                price = purchased_items[i][j]
            if j == 2:
                quantity = purchased_items[i][j]
                total = price * quantity
        purchase.append([purchased_items[i][0],purchased_items[i][1],purchased_items[i][2],round(total,2)])
    price = 0
    quantity = 0
    for i in range(len(purchase)):
        for j in range(len(purchase[i])):
            if j == 2:
                quantity += purchase[i][j]
            if j == 3:
                price += purchase[i][j]
    purchase.append(['Quantity', quantity, 'Total Bill', round(price,2)])
    return purchase

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

    purchased_items = [
        ['Milk', 10.99, 2],
        ['Cake', 12.5, 5],
        ['Tapal Family Mixture', 450, 1],
        ['Shan Bombay Biryani', 70, 2],
    ]
    print(compute_my_bill(purchased_items))
    # Should print:
    # [
    #   ['Milk', 10.99, 2, 21.98], 
    #   ['Cake', 12.5, 5, 62.5], 
    #   ['Tapal Family Mixture', 450, 1, 450], 
    #   ['Shan Bombay Biryani', 70, 2, 140], 
    #   ['Quantity', 10, 'Total Bill', 674.48]
    # ]

    purchased_items = [
        ['Lux Soap', 45.87, 6],
        ['Zeera Plus', 20, 10],
        ['Dry Dates', 160, 3],
        ['Lipton Green Tea', 120, 2],
    ]
    print(compute_my_bill(purchased_items))
    # Should print:
    # [
    #   ['Lux Soap', 45.87, 6, 275.22], 
    #   ['Zeera Plus', 20, 10, 200], 
    #   ['Dry Dates', 160, 3, 480], 
    #   ['Lipton Green Tea', 120, 2, 240], 
    #   ['Quantity', 21, 'Total Bill', 1195.22]
    # ]

    purchased_items = [
        ['Pen', 0.99, 10],
        ['Notebook', 2.5, 5],
        ['Printer', 150.75, 2],
        ['Desk Chair', 50, 1],
    ]
    print(compute_my_bill(purchased_items))
    # Should print:
    # [
    #   ['Pen', 0.99, 10, 9.9], 
    #   ['Notebook', 2.5, 5, 12.5], 
    #   ['Printer', 150.75, 2, 301.5], 
    #   ['Desk Chair', 50, 1, 50], 
    #   ['Quantity', 18, 'Total Bill', 373.9]
    # ]

    purchased_items = [
        ['Apple', 3.0, 10],
        ['Banana', 3.0, 8],
        ['Orange', 3.0, 12],
    ]
    print(compute_my_bill(purchased_items))
    # Should print:
    # [
    #   ['Apple', 3.0, 10, 30.0], 
    #   ['Banana', 3.0, 8, 24.0], 
    #   ['Orange', 3.0, 12, 36.0], 
    #   ['Quantity', 30, 'Total Bill', 90.0]
    # ]

    print(compute_my_bill([]))
    # Should print:
    # [
    #   ['Quantity', 0, 'Total Bill', 0]
    # ]

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#



# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your functions, type one of the following commands in the terminal:
# python -m pytest tests/test_q1.py
# python3 -m pytest tests/test_q1.py