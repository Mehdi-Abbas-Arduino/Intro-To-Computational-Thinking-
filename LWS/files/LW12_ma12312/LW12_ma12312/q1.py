# -----------------------------------------#
# FUNCTION DEFINITION                      #
# -----------------------------------------#

month_names = {
    1: 'January', 2: 'February', 3: 'March',
    4: 'April', 5: 'May', 6: 'June',
    7: 'July', 8: 'August', 9: 'September',
    10: 'October', 11: 'November', 12: 'December'
}

def print_dates_in_long_form(date_records):
    # WRITE YOUR CODE HERE
    global month_names 
    lst = []

    for i in date_records:
        if i['month'] in month_names:
            x = month_names[i['month']]
            lst.append(f"{x} {i['day']}, {i['year']}")
    for j in lst:
        print(j)


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
    print_dates_in_long_form([
        {'day': 12, 'month': 12, 'year': 1996},
        {'day': 8, 'month': 12, 'year': 1995},
        {'day': 30, 'month': 4, 'year': 1999}
    ])
    # Should print:
    # December 12, 1996
    # December 8, 1995
    # April 30, 1999
    print()

    print_dates_in_long_form([
        {'year': 1996, 'month': 12, 'day': 12},
        {'year': 1995, 'month': 12, 'day': 8},
        {'year': 1999, 'month': 4, 'day': 30},
        {'year': 1998, 'month': 7, 'day': 30}
    ])
    # Should print:
    # December 12, 1996
    # December 8, 1995
    # April 30, 1999
    # July 30, 1998
    print()

    print_dates_in_long_form([
        {'year': 1996, 'month': 12, 'day': 12},
        {'year': 1995, 'month': 12, 'day': 8},
        {'year': 1999, 'month': 4, 'day': 30},
        {'year': 1998, 'month': 4, 'day': 30}
    ])
    # Should print:
    # December 12, 1996
    # December 8, 1995
    # April 30, 1999
    # April 30, 1998
    print()

    print_dates_in_long_form([
        {'year': 1995, 'month': 8, 'day': 3},
        {'year': 1994, 'month': 7, 'day': 15},
        {'year': 1997, 'month': 3, 'day': 17},
        {'year': 1995, 'month': 10, 'day': 17},
        {'year': 1999, 'month': 3, 'day': 7},
        {'year': 1995, 'month': 6, 'day': 4},
        {'year': 1994, 'month': 4, 'day': 29},
        {'year': 1999, 'month': 5, 'day': 18},
        {'year': 1994, 'month': 7, 'day': 3},
        {'year': 1994, 'month': 8, 'day': 7},
        {'year': 1999, 'month': 4, 'day': 5},
        {'year': 1998, 'month': 9, 'day': 30}
    ])
    # Should print:
    # August 3, 1995
    # July 15, 1994
    # March 17, 1997
    # October 17, 1995
    # March 7, 1999
    # June 4, 1995
    # April 29, 1994
    # May 18, 1999
    # July 3, 1994
    # August 7, 1994
    # April 5, 1999
    # September 30, 1998
    print()

    print_dates_in_long_form([
        {'year': 1998, 'month': 8, 'day': 24},
        {'year': 1999, 'month': 4, 'day': 22},
        {'year': 1996, 'month': 3, 'day': 2},
        {'year': 1995, 'month': 5, 'day': 19},
        {'year': 1998, 'month': 6, 'day': 14},
        {'year': 1999, 'month': 5, 'day': 20},
        {'year': 1996, 'month': 6, 'day': 14},
        {'year': 1998, 'month': 11, 'day': 15},
        {'year': 1997, 'month': 12, 'day': 31},
        {'year': 1997, 'month': 2, 'day': 22},
        {'year': 1998, 'month': 6, 'day': 27},
        {'year': 1998, 'month': 11, 'day': 18}
    ])
    # Should print:
    # August 24, 1998
    # April 22, 1999
    # March 2, 1996
    # May 19, 1995
    # June 14, 1998
    # May 20, 1999
    # June 14, 1996
    # November 15, 1998
    # December 31, 1997
    # February 22, 1997
    # June 27, 1998
    # November 18, 1998
    print()

    print_dates_in_long_form([
        {'year': 1994, 'month': 8, 'day': 29},
        {'year': 1997, 'month': 7, 'day': 31},
        {'year': 1994, 'month': 10, 'day': 18},
        {'year': 1998, 'month': 8, 'day': 31}
    ])
    # Should print:
    # August 29, 1994
    # July 31, 1997
    # October 18, 1994
    # August 31, 1998
    print()

    print_dates_in_long_form([
        {'year': 1994, 'month': 8, 'day': 29},
        {'year': 1997, 'month': 7, 'day': 31},
        {'year': 1994, 'month': 10, 'day': 18},
        {'year': 1998, 'month': 4, 'day': 31}
    ])
    # Should print:
    # August 29, 1994
    # July 31, 1997
    # October 18, 1994
    # April 31, 1998
    print()

    print_dates_in_long_form([
        {'year': 1996, 'month': 3, 'day': 5},
        {'year': 1999, 'month': 5, 'day': 3},
        {'year': 1998, 'month': 5, 'day': 13},
        {'year': 1995, 'month': 6, 'day': 1},
        {'year': 1997, 'month': 12, 'day': 4},
        {'year': 1997, 'month': 8, 'day': 5},
        {'year': 1997, 'month': 11, 'day': 12},
        {'year': 1999, 'month': 10, 'day': 4}
    ])
    # Should print:
    # March 5, 1996
    # May 3, 1999
    # May 13, 1998
    # June 1, 1995
    # December 4, 1997
    # August 5, 1997
    # November 12, 1997
    # October 4, 1999
    print()

    print_dates_in_long_form([
        {'year': 1994, 'month': 11, 'day': 30}
    ])
    # Should print:
    # November 30, 1994

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#



# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your function, type one of the following commands in the terminal:
# python -m pytest tests/test_q1.py
# python3 -m pytest tests/test_q1.py
