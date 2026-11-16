# -----------------------------------------#
# FUNCTION DEFINITION                      #
# -----------------------------------------#

def most_prolific_authors(books):
    # WRITE YOUR CODE HERE
    di = {}
    for i in books:
        author = i['author']
        if author not in di:
            di[i['author']] = 1
        else:
             di[i['author']] += 1

    highest = 0
    lst = []
    for i in di:
        freq = di[i]
        if freq > highest:
            highest = freq

    for i in di:
        if highest == di[i]:
            lst.append(i)
    lst.sort()
    return ', '.join(lst)




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


    books = [{'title': 'C++ How to Program', 'author': 'Harvey Deitel', 'year': 1994},
     {'title': 'Introduction to Algorithms', 'author': 'Charles E. Leiserson', 'year': 1989},
     {'title': 'C# for Programmers', 'author': 'Harvey Deitel', 'year': 2008},
     {'title': 'Code Complete', 'author': 'Steve McConnell', 'year': 1993}]
    print(most_prolific_authors(books))
    # Should print: Harvey Deitel
    print()

    books = [{'title': 'Advanced Research in VLSI', 'author': 'Charles E. Leiserson', 'year': 1986},
     {'title': 'C++ How to Program', 'author': 'Harvey Deitel', 'year': 1994},
     {'title': 'Introduction to Algorithms', 'author': 'Charles E. Leiserson', 'year': 1989},
     {'title': 'C# for Programmers', 'author': 'Harvey Deitel', 'year': 2008},
     {'title': 'Code Complete', 'author': 'Steve McConnell', 'year': 1993}]
    print(most_prolific_authors(books))
    # Should print: Charles E. Leiserson, Harvey Deitel

    # ----------------------------------------------#
    # YOU CAN DO FURTHER CUSTOM TESTING BELOW       #
    # ----------------------------------------------#

    # In order to test your function, run:
    # pytest tests/test_q2.py
