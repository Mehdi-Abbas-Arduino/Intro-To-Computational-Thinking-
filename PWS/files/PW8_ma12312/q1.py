# -----------------------------------------#
# FUNCTION DEFINITION                      #
# -----------------------------------------#

def selek_sees(num, word):
    # WRITE YOUR CODE HERE
    lst = []
    x = word.split()
    flag = True
    for i in range(len(num)):
        nums = num[i]
        words = word[i]
        lst.append([nums,words])
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i][0] == lst[j][0] and lst[i][1] != lst[j][1]:
                flag = False

    return flag
    
                

            



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

    print(selek_sees([2, 3, 2, 4, 1], "cacta"))
    # Should print: True

    print(selek_sees([5], "z"))
    # Should print: True

    print(selek_sees([7, 9], "ab"))
    # Should print: True

    print(selek_sees([1, 2, 2, 1], "xqqr"))
    # Should print: False

    print(selek_sees([1, 2, 3, 2, 1], "wwwww"))
    # Should print: True

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#



# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your function, type one of the following commands in the terminal:
# python -m pytest tests/test_q1.py
# python3 -m pytest tests/test_q1.py