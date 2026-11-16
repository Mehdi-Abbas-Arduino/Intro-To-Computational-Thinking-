# -----------------------------------------#
# FUNCTION DEFINITION                      #
# -----------------------------------------#

from helper_for_formatting_dont_delete import dictFormatting


def merge_by_value(north_branch, south_branch):
    # WRITE YOUR CODE HERE
    comp = {}

    for i in north_branch:
        if north_branch[i] not in comp:
            comp[north_branch[i]] = [i]
        else:
            comp[north_branch[i]].append(i)

    for j in south_branch:
        if south_branch[j] not in comp:
            comp[south_branch[j]] = [j]
        else:
            comp[south_branch[j]].append(j)

    
    return comp 
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

    north_branch = {101: 'Python Basics', 102: 'Data Structures', 103: 'Python Basics'}
    south_branch = {201: 'Data Structures', 202: 'Algorithms', 203: 'Python Basics'}
    print(dictFormatting(merge_by_value(north_branch, south_branch)))
    # Should print:
    # {'Algorithms': [202], 'Data Structures': [102, 201], 'Python Basics': [101, 103, 203]}
    print()

    north_branch = {1101: 'Python Basics', 1102: 'Database Systems', 1103: 'Algorithms'}
    south_branch = {2201: 'Algorithms', 2202: 'Python Basics', 2203: 'Database Systems'}
    print(dictFormatting(merge_by_value(north_branch, south_branch)))
    # Should print:
    # {'Algorithms': [1103, 2201], 'Database Systems': [1102, 2203], 'Python Basics': [1101, 2202]}
    print()

    north_branch = {1104: 'Physics Fundamentals', 1105: 'World History', 1106: 'Calculus I'}
    south_branch = {2204: 'Physics Fundamentals'}
    print(dictFormatting(merge_by_value(north_branch, south_branch)))
    # Should print:
    # {'Calculus I': [1106], 'Physics Fundamentals': [1104, 2204], 'World History': [1105]}
    print()

    north_branch = {1107: 'Modern Literature', 1108: 'Biology Essentials', 1109: 'Modern Literature'}
    south_branch = {}
    print(dictFormatting(merge_by_value(north_branch, south_branch)))
    # Should print:
    # {'Biology Essentials': [1108], 'Modern Literature': [1107, 1109]}
    print()

    north_branch = {1110: 'Discrete Mathematics', 1111: 'Organic Chemistry'}
    south_branch = {2210: 'Art History', 2211: 'Computer Networks'}
    print(dictFormatting(merge_by_value(north_branch, south_branch)))
    # Should print:
    # {'Art History': [2210], 'Computer Networks': [2211], 'Discrete Mathematics': [1110], 'Organic Chemistry': [1111]}
    print()

    north_branch = {}
    south_branch = {}
    print(dictFormatting(merge_by_value(north_branch, south_branch)))
    # Should print:
    # {}
    print()

    north_branch = {1112: 'Introduction to Python', 1113: 'Data Structures', 1114: 'Introduction to Python'}
    south_branch = {2212: 'Data Structures', 2213: 'Introduction to Python', 2214: 'Data Structures'}
    print(dictFormatting(merge_by_value(north_branch, south_branch)))
    # Should print:
    # {'Data Structures': [1113, 2212, 2214], 'Introduction to Python': [1112, 1114, 2213]}

    # ----------------------------------------------#
    # YOU CAN DO FURTHER CUSTOM TESTING BELOW       #
    # ----------------------------------------------#

    # In order to test your function, run:
    # pytest tests/test_q3.py
