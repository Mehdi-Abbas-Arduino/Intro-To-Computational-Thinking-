# -----------------------------------------#
# FUNCTION DEFINITION                      #
# -----------------------------------------#

# def potato_song(verses):
#     # WRITE YOUR CODE HERE
#     col = 8
#     row = 2 * verses
#     for i in range(0,row,2):
#         for j in range(1,col):
#             if j == col // 2:
#                 print(f"{j}!")
#                 break
#             else:
#                 print(f"{j} potato",end=', ')
#         print()
#         for z in range(j+1,col):
#             if j == col:
#                 print("MORE!")
#             else:
#                 print(f"{z} potato",end=', ')
#         col += 4

def potato_song(verses):
    """
    Start from number 1.
    Each verse has 7 numbers:
    (1,2,3,4)
    (5,6,7,More)
    3 "potato" numbers, then a "!" number,
    then 3 more "potato" numbers and "MORE!".

    Build the whole song in a string and return it.
    """
    result = ""
    num = 1

    for i in range(verses):
        for j in range(3):
            result += f"{num} potato, "
            num += 1

        result += f"{num}!\n"
        num += 1

        for j in range(3):
            result += f"{num} potato, "
            num += 1

        result += "MORE!"

        if i != verses - 1:
            result += "\n"

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
    # ----------------------------------------------#

    print(potato_song(1))
    # Should print:
    # 1 potato, 2 potato, 3 potato, 4!
    # 5 potato, 6 potato, 7 potato, MORE!

    print(potato_song(3))
    # Should print:
    # 1 potato, 2 potato, 3 potato, 4!
    # 5 potato, 6 potato, 7 potato, MORE!
    # 8 potato, 9 potato, 10 potato, 11!
    # 12 potato, 13 potato, 14 potato, MORE!
    # 15 potato, 16 potato, 17 potato, 18!
    # 19 potato, 20 potato, 21 potato, MORE!

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#



# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your function, type the following command in the terminal:
# pytest tests/test_q6.py
