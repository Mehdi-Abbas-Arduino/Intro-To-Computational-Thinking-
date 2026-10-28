# -----------------------------------------#
# FUNCTION DEFINITION                      #
# -----------------------------------------#

def add_study_hours(campus_hours, home_hours):
    # WRITE YOUR CODE HERE
    lst = []
    lst2 = []
    if len(campus_hours) != len(home_hours):
        return "Grids don't have the same dimensions."
    count = 0
    count2 = 0
    for i in range(len(campus_hours)):
        row = i
        for j in range(len(campus_hours[i])):
            col = j
            count += 1
    for z in range(len(home_hours)):
        row2 = z
        for k in range(len(home_hours[z])):
            col2 = k
            count2 += 1

    if count != count2:
        return "Grids don't have the same dimensions."
    else:
                        
        for i in range(len(campus_hours)):
            row = i
            lst2 = []
            for j in range(len(campus_hours[i])):
                col = j
                lst2.append(campus_hours[row][col] + home_hours[row][col])
            lst.append(lst2)
        return lst 

        # for i in range(len(campus_hours)):
        #     x = len(campus_hours)
        
        # for i in range(0,len(lst),x):
        #     lst2.append(lst[i:i+x])
        # return lst2




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

    print(add_study_hours([[4, 8], [3, 7]], [[1, 0], [5, 2]]))
    # Should print: [[5, 8], [8, 9]]

    print(add_study_hours([[5, 2], [0, 1], [1, 9]],
                          [[2, 3], [4, 1], [0, 2]]))
    # Should print: [[7, 5], [4, 2], [1, 11]]

    print(add_study_hours([[1], [2]], [[3, 5], [4, 6]]))
    # Should print: Grids don't have the same dimensions.

    print(add_study_hours([[12, 7, 3], [4, 5, 6], [7, 8, 9]],
                          [[5, 8, 1], [6, 7, 3], [4, 5, 9]]))
    # Should print: [[17, 15, 4], [10, 12, 9], [11, 13, 18]]

    print(add_study_hours([[1, 2], [0, 3], [6, 7]],
                          [[4, 5], [7, 8]]))
    # Should print: Grids don't have the same dimensions.

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#



# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your function, type one of the following commands in the terminal:
# python -m pytest tests/test_q3.py
# python3 -m pytest tests/test_q3.py