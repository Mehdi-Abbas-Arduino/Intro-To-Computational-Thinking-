def hours_per_member(task_hours, member_count):
    # WRITE YOUR CODE HERE
    if task_hours == []:
        return [0]*member_count
    else:
        return helper(task_hours,member_count,[0]*member_count)

def helper(task,member,t,c=0,index=0):
    if c == len(task):
        return t
    else:
        if index == member:
            index = 0
        t[index] = (t[index]) + (task[c])
    return helper(task,member,t,c+1,index+1)

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

    print(hours_per_member([1, 2, 3, 4, 5], 2))
    # Should print: [9, 6]

    print(hours_per_member([1, 2, 3, 4, 5], 3))
    # Should print: [5, 7, 3]

    print(hours_per_member([1, 2, 3], 5))
    # Should print: [1, 2, 3, 0, 0]

    print(hours_per_member([], 3))
    # Should print: [0, 0, 0]

    print(hours_per_member([4, 5, 6, 7], 1))
    # Should print: [22]

    print(hours_per_member([3] * 300, 4))
    # Should print: [225, 225, 225, 225]

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#


# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your function, type one of the following commands in the terminal:
# python -m pytest tests/test_q6.py
# python3 -m pytest tests/test_q6.py
