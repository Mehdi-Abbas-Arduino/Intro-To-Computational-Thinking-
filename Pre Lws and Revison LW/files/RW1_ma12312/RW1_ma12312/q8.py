# -----------------------------------------#
# FUNCTION DEFINITIONS                     #
# -----------------------------------------#
# Write the required function(s) below.


def apples_in_house(house_start,house_end,apple_tree,total_apples):
    applecount = 0
    for i in range(total_apples):
        friut_offset = int(input("Enter the value = "))
        diff = apple_tree + friut_offset

        if diff >= house_start and diff <= house_end:
            applecount += 1
    return applecount

def oranges_in_house(house_start, house_end,orange_tree,total_oranges):
    orangecount = 0
    for i in range(total_oranges):
        friut_offset = int(input("Enter the value = "))
        diff = orange_tree + friut_offset

        if diff >= house_start and diff <= house_end:
            orangecount += 1
    return orangecount
def fruits_in_house(house_start, house_end, apple_tree, orange_tree, total_apples, total_oranges):

    x = apples_in_house(house_start,house_end,apple_tree,total_apples)
    y = oranges_in_house(house_start, house_end,orange_tree,total_oranges)

    print(x,y)


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

    # Note: Inputs to be entered are labelled as [ Input -> X ] where X is the input.

    fruits_in_house(7, 11, 5, 15, 3, 2)
    # [ Input -> -2]
    # [ Input -> 2]
    # [ Input -> 1]
    # [ Input -> 5]
    # [ Input -> -6]
    # Should print: 1 1

    print()

    fruits_in_house(8, 13, 6, 18, 4, 3)
    # [ Input -> 3]
    # [ Input -> -2]
    # [ Input -> 2]
    # [ Input -> 1]
    # [ Input -> -4]
    # [ Input -> -6]
    # [ Input -> 2]
    # Should print: 2 1

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#

    
# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your function, type the following command in the terminal:
# pytest tests/test_q7.py