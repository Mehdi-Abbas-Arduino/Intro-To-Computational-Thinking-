# -----------------------------------------#
# FUNCTION DEFINITIONS                     #
# -----------------------------------------#
# Write the required function(s) below.


# def apple_in_house(house_start,house_end,apple_tree,total_apples,offset):
#     position = apple_tree + offset
#     if position >= house_start and position <= house_end:
#         return True
# def oranges_in_house(house_start, house_end,orange_tree,total_oranges,offset): 
#     position = orange_tree + offset
#     if position >= house_start and position <= house_end:
#         return True 
# def fruits_in_house(house_start, house_end, apple_tree, orange_tree, total_apples, total_oranges):
#     APPLECOUNT = 0
#     ORANGECOUNT = 0
#     number = total_apples + total_oranges
#     for i in range(1,number+1):
#         if i <= total_apples:
#             x = int(input("Enter a number = "))
#             applefunc = apple_in_house(house_start,house_end,apple_tree,total_apples,x)
#             if applefunc:
#                 APPLECOUNT += 1
#         elif i > total_apples and i <= number:
#             x = int(input("Enter a number = "))
#             orangefunc = oranges_in_house(house_start, house_end,orange_tree,total_oranges,x)
#             if orangefunc:
#                 ORANGECOUNT += 1
                
            
#     print(APPLECOUNT,ORANGECOUNT)
def apples_in_house(house_start, house_end, apple_tree, total_apples):
    count = 0

    for i in range(total_apples):
        offset = int(input())
        position = apple_tree + offset

        if house_start <= position <= house_end:
            count += 1

    return count


def oranges_in_house(house_start, house_end, orange_tree, total_oranges):
    count = 0

    for i in range(total_oranges):
        offset = int(input())
        position = orange_tree + offset

        if house_start <= position <= house_end:
            count += 1

    return count


def fruits_in_house(house_start, house_end, apple_tree, orange_tree, total_apples, total_oranges):
    apple_count = apples_in_house(house_start, house_end, apple_tree, total_apples)
    orange_count = oranges_in_house(house_start, house_end, orange_tree, total_oranges)

    print(apple_count, orange_count)

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