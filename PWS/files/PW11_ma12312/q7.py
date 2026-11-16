def get_data_type(e):
    if type(e) == int:
        return "int"
    elif type(e) == str:
        return "str"
    elif type(e) == list:
        return "list"
    elif type(e) == bool:
        return "bool"
    elif type(e) == float:
        return "float"
def helper(items, vals):
    if items == []:
        return vals
    first = items[0]
    if type(first) == list:
        if "list" not in vals:
            vals.append("list")
        helper(first, vals)
    else:
        x = get_data_type(first)
        if x not in vals:
            vals.append(x)

    return helper(items[1:], vals)
def check_types(items):
    if type(items) != list:
        return "Error: Bad argument. Function 'check_types' only accepts lists"

    return helper(items, [])
    


# -----------------------------------------#
# TESTING YOUR CODE                        #
# -----------------------------------------#
# The code below runs only when this file is executed directly.
if __name__ == "__main__":

    # ----------------------------------------------#
    # TESTING YOUR CODE ON SAMPLE TEST CASES        #
    # Run this file and manually check whether      #
    # your function produces the expected output.   #
    # ----------------------------------------------#

    print(check_types([]))
    # Should print: []

    print(check_types(["Programming", "List", "Fundamentals"]))
    # Should print: ['str']

    print(check_types(['hello', [2, [False, [3.5]]], 'world']))
    # Should print: ['str', 'list', 'int', 'bool', 'float']

    print(check_types([True, 1, 1.0]))
    # Should print: ['bool', 'int', 'float']

    print(check_types('this is not right'))
    # Should print: Error: Bad argument. Function 'check_types' only accepts lists

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#


# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your function, type one of the following commands in the terminal:
# python -m pytest tests/test_q7.py
# python3 -m pytest tests/test_q7.py
