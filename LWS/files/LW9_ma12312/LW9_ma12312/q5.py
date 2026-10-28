# -----------------------------------------#
# FUNCTION DEFINITION                      #
# -----------------------------------------#

def get_frequent_items(orders, target_item):
    # WRITE YOUR CODE HERE
    items = []
    for order in orders:
        if target_item in order :
            for item in order :
                if item != target_item:
                    items.append(item)
    result = []
    highest = 0

    for item in items:
        count = items.count(item)
        if count > highest:
            highest = count 
            result = [item]
        elif count == highest and item not in result:
            result.append(item)
    return result


# -----------------------------------------#
# TESTING YOUR CODE                        #
# -----------------------------------------#
# The code below runs only when this file is executed directly.
if __name__ == "__main__":

    # ----------------------------------------------#
    # TESTING YOUR CODE ON VISIBLE TEST CASES       #
    # Run this file and manually check whether      #
    # your function produces the expected output.   #
    # sorted() displays the items alphabetically.   #
    # ----------------------------------------------#

    monday_orders = [
        ['Chai', 'Samosa', 'Biscuit'],
        ['Chai', 'Paratha', 'Omelette'],
        ['Pizza Slice', 'Pepsi', 'Fries'],
        ['Biryani', 'Raita', 'Lassi'],
        ['Bun Kabab', 'Fries', 'Pepsi'],
        ['Samosa', 'Roll', 'Jalebi']
    ]

    print(sorted(get_frequent_items(monday_orders, "Pepsi")))
    # Should print: ['Fries']

    print(sorted(get_frequent_items(monday_orders, "Brownie")))
    # Should print: []

    friday_orders = [
        ['Chai', 'Samosa', 'Paratha', 'Cake Rusk'],
        ['Chai', 'Biscuit', 'Samosa'],
        ['Samosa', 'Cold Coffee', 'Biscuit'],
        ['Pizza Slice', 'Fries', 'Pepsi', 'Brownie'],
        ['Omelette', 'Paratha', 'Lassi', 'Samosa'],
        ['Biscuit', 'Chai', 'Samosa', 'Pakora'],
        ['Chai', 'Biscuit', 'Paratha']
    ]

    print(sorted(get_frequent_items(friday_orders, "Chai")))
    # Should print: ['Biscuit', 'Samosa']

    shop_orders = [
        ['Pepsi', 'Pizza'],
        ['Milk', 'Tea', 'Sugar'],
        ['Tissue Box', 'Air Freshner'],
        ['Tea', 'Bread', 'Eggs', 'Butter'],
        ['Pizza', 'Pepsi', 'Chips'],
        ['Meat', 'Yogurt', 'Onion', 'Tomato', 'Potatoes'],
        ['Bun', 'Patties', 'Chips', 'Pepsi'],
        ['Samosa', 'Roll', 'Jalebi']
    ]

    print(sorted(get_frequent_items(shop_orders, 'Pepsi')))
    # Should print: ['Chips', 'Pizza']

    print(sorted(get_frequent_items(shop_orders, 'Coffee')))
    # Should print: []

    print(sorted(get_frequent_items([], 'Pepsi')))
    # Should print: []


    grocery_orders = [
        ['Meat', 'Yogurt', 'Tomato', 'Rice'],
        ['Meat', 'Onion', 'Yogurt'],
        ['Yogurt', 'Flour', 'Onion'],
        ['Sugar', 'Oil', 'Soap', 'Detergent'],
        ['Eggs', 'Bread', 'Butter', 'Yogurt'],
        ['Onion', 'Meat', 'Yogurt', 'Spices'],
        ['Meat', 'Onion', 'Tomato']
    ]

    print(sorted(get_frequent_items(grocery_orders, 'Meat')))
    # Should print: ['Onion', 'Yogurt']

    print(sorted(get_frequent_items(grocery_orders, "")))
    # Should print: []

    print(sorted(get_frequent_items(grocery_orders, 'Tomato')))
    # Should print: ['Meat']

    single_item_orders = [
        ['Tomato'],
        ['Potato'],
        ['Onion'],
        ['Garlic']
    ]

    print(sorted(get_frequent_items(single_item_orders, "Tomato")))
    # Should print: []

    snack_orders = [
        ['Samosa', 'Jalebi'],
        ['Roll', 'Jalebi'],
        ['Samosa', 'Roll', 'Jalebi'],
        ['Samosa', 'Roll', 'Gulab Jamun'],
        ['Samosa', 'Biscuits', 'Roll'],
        ['Roll', 'Biscuits', 'Jalebi'],
        ['Samosa']
    ]

    print(sorted(get_frequent_items(snack_orders, 'Samosa')))
    # Should print: ['Roll']

    snack_orders_extra = [
        ['Samosa', 'Biscuits', 'Roll'],
        ['Samosa', 'Jalebi'],
        ['Roll', 'Jalebi'],
        ['Samosa', 'Roll', 'Jalebi'],
        ['Samosa', 'Roll', 'Gulab Jamun'],
        ['Samosa'],
        ['Jalebi'],
        ['Roll', 'Biscuits', 'Jalebi'],
        ['Samosa', 'Jalebi']
    ]

    print(sorted(get_frequent_items(snack_orders_extra, 'Jalebi')))
    # Should print: ['Roll', 'Samosa']

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#



# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your function, type one of the following commands in the terminal:
# python -m pytest tests/test_q5.py
# python3 -m pytest tests/test_q5.py