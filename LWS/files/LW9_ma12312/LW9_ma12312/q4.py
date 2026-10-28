# -----------------------------------------#
# FUNCTION DEFINITION                      #
# -----------------------------------------#

def color_neighbors(tile_wall, target_color):
    # WRITE YOUR CODE HERE
    s_row = 0
    s_col = 0
    lst = []
    for row in range(len(tile_wall)):
        
        for col in range(len(tile_wall[0])):
           
            if tile_wall[row][col] == target_color:
                if (row + 1) < len (tile_wall):
                    lst.append(tile_wall[row+1][col])
                if (col - 1) >= 0:
                    lst.append(tile_wall[row][col-1])
                if (row-1) >= 0 :
                    lst.append(tile_wall[row-1][col])
                if (col + 1) < len(tile_wall[0]):  
                    lst.append(tile_wall[row][col+1])
                        
                
                

    return lst 




    # for i in range(len(tile_wall)):
    #         row = i
    #         for j in range(len(tile_wall[j])):
    #             col = j
                

# -----------------------------------------#
# TESTING YOUR CODE                        #
# -----------------------------------------#
# The code below runs only when this file is executed directly.
if __name__ == "__main__":

    # ----------------------------------------------#
    # TESTING YOUR CODE ON VISIBLE TEST CASES       #
    # Run this file and manually check whether      #
    # your function produces the expected output.   #
    # sorted() displays the colors alphabetically.   #
    # ----------------------------------------------#

    tile_wall = [
        ["Red", "Blue", "Green", "Cyan"],
        ["Yellow", "Black", "White", "Brown"],
        ["Pink", "Orange", "Purple", "Gray"]
    ]

    print(sorted(color_neighbors(tile_wall, "Black")))
    # Should print: ['Blue', 'Orange', 'White', 'Yellow']

    print(sorted(color_neighbors(tile_wall, "Blue")))
    # Should print: ['Black', 'Green', 'Red']

    print(sorted(color_neighbors(tile_wall, "Gray")))
    # Should print: ['Brown', 'Purple']

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#



# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your function, type one of the following commands in the terminal:
# python -m pytest tests/test_q4.py
# python3 -m pytest tests/test_q4.py