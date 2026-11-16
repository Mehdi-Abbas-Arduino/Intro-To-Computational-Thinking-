def first_scrolls(first,string=''):
    if first == '':
        return string
    else:
        result = first[0].lower()
        # Comparing the last add elemrnt in the string to add a new one
        if string == '' or result != string[-1]:
            string += result
        return first_scrolls(first[1:],string)

def second_scrolls(second,string=''):
    if second == '':
        return string
    else:
        result = second[0].lower()
        # Comparing the last add elemrnt in the string to add a new one
        if string == '' or result != string[-1]:
            string += result
        return second_scrolls(second[1:],string)

def compare(first,second,string=''):
    if first == '' and second == '':
        return string

    # If the first string is empty, process the second
    if first == '':
        return second + string

    # If the second string is empty, process the first
    if second == '':
        return first + string
    else:
        firsts = first[0].lower()
        seconds = second[0].lower()
        string += firsts + seconds
        return compare(first[1:],second[1:],string)

def remove_consecutive(string, result=''):
    if string == '':
        return result

    # Only add a character if it differs
    # from the previous character in the result
    if result == '' or string[0] != result[-1]:
        result += string[0]

    return remove_consecutive(string[1:], result)


def create_scroll(first_scroll, second_scroll):
    first = first_scrolls(first_scroll)
    second = second_scrolls(second_scroll)
    x =  compare(first,second)
    return remove_consecutive(x)

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

    print(create_scroll('aab', 'cck'))
    # Should print: acbk

    print(create_scroll('act', 'sat'))
    # Should print: ascat

    print(create_scroll('sSsiIi', 'tttaAa'))
    # Should print: stia

    print(create_scroll('bcd', 'efg'))
    # Should print: becfdg

    print(create_scroll('vvvv', 'vvvv'))
    # Should print: v

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#


# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your function, type one of the following commands in the terminal:
# python -m pytest tests/test_q9.py
# python3 -m pytest tests/test_q9.py
