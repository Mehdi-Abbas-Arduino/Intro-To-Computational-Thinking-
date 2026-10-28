# -----------------------------------------#
# FUNCTION DEFINITIONS                     #
# -----------------------------------------#

def count_solo_invigilators(hall_layout):
    # # WRITE YOUR CODE HERE
    # count = 0
    # for i in range(len(hall_layout)):
    #     row = i
    #     for j in range(len(hall_layout[i])):
    #         col = j
    #         if hall_layout[row][col] == 'I':
    #             count += 1
    #             if count > 2
    # return count
    row = len(hall_layout)
    if row == 0:
        return 0
    col = len(hall_layout[0])
    rowcount = [0] * row
    colcount = [0] * col
    for r in range(row):
        for c in range(col):
            if hall_layout[r][c] == "I":
                rowcount[r] += 1
                colcount[c] += 1   
    temp = 0
    for r in range(row):
        for c in range(col):
            if hall_layout[r][c] == "I" : 
                if rowcount[r] == 1 and colcount[c] == 1:
                    temp += 1

    return temp
def main():
    # WRITE YOUR CODE HERE
    row,col = input().split()
    row = int(row)
    col = int(col)
    lst2 = []
    for i in range(row):
        x = input()
        x = x.split()
        lst2.append(x)
        
    y = count_solo_invigilators(lst2)
    print(y)

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

    main()
    # [ Input -> 3 4 ]
    # [ Input -> I E E E ]
    # [ Input -> E E I E ]
    # [ Input -> E I E E ]
    # Should print: 3

    main()
    # [ Input -> 3 4 ]
    # [ Input -> I I E E ]
    # [ Input -> E E I E ]
    # [ Input -> E E E I ]
    # Should print: 2

    main()
    # [ Input -> 3 3 ]
    # [ Input -> I I E ]
    # [ Input -> I I E ]
    # [ Input -> E E E ]
    # Should print: 0

    main()
    # [ Input -> 3 3 ]
    # [ Input -> I E E ]
    # [ Input -> E E I ]
    # [ Input -> E I E ]
    # Should print: 3

    main()
    # [ Input -> 3 3 ]
    # [ Input -> I E I ]
    # [ Input -> E I E ]
    # [ Input -> I E E ]
    # Should print: 1

    main()
    # [ Input -> 2 3 ]
    # [ Input -> E E E ]
    # [ Input -> E E E ]
    # Should print: 0

    main()
    # [ Input -> 4 4 ]
    # [ Input -> I E E E ]
    # [ Input -> E E I E ]
    # [ Input -> E I E E ]
    # [ Input -> E E E I ]
    # Should print: 4

    main()
    # [ Input -> 3 2 ]
    # [ Input -> I E ]
    # [ Input -> I E ]
    # [ Input -> E I ]
    # Should print: 1

    main()
    # [ Input -> 1 1 ]
    # [ Input -> I ]
    # Should print: 1

    main()
    # [ Input -> 1 5 ]
    # [ Input -> I I I I I ]
    # Should print: 0

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#



# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your functions, type one of the following commands in the terminal:
# python -m pytest tests/test_q6.py
# python3 -m pytest tests/test_q6.py