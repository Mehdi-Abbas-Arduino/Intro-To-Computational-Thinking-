# -----------------------------------------#
# FUNCTION DEFINITIONS                     #
# -----------------------------------------#

def special_list_sort(student_records):
    # WRITE YOUR CODE HERE
    new = []
    for i in range(len(student_records)):
        new.append(student_records[i])

    def sort_key(x):
        return (x[2], x[1], x[0])

    new.sort(key=sort_key)

    return new 

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

    student_records = [
        ['Sarwan', 'EE', 2021], ['Ayesha Khan', 'CND', 2021], ['Hamza Junaid', 'EE', 2021],
        ['Ahsan Qadeer', 'CS', 2020], ['Muhammad Ali Bhutto', 'EE', 2020], ['Marium Habiby', 'SDP', 2021],
        ['Adil Ali Khan', 'EE', 2021]]
    print(special_list_sort(student_records))
    # Should print:
    # [
    #   ['Ahsan Qadeer', 'CS', 2020], ['Muhammad Ali Bhutto', 'EE', 2020], ['Ayesha Khan', 'CND', 2021],
    #   ['Adil Ali Khan', 'EE', 2021], ['Hamza Junaid', 'EE', 2021], ['Sarwan', 'EE', 2021], 
    #   ['Marium Habiby', 'SDP', 2021]
    # ]

    student_records = [
        ['Sarwan', 'EE', 2021], ['Lulowalokand Wala', 'CND', 2021], ['Hamza Junaid', 'EE', 2021],
        ['Ahsan Qadeer', 'CS', 2020], ['Muhammad Ali Bhutto', 'EE', 2020], ['Marium Habiby', 'SDP', 2021],
        ['Adil Ali Khan', 'EE', 2021]]
    print(special_list_sort(student_records))
    # Should print:
    # [
    #   ['Ahsan Qadeer', 'CS', 2020], ['Muhammad Ali Bhutto', 'EE', 2020], ['Lulowalokand Wala', 'CND', 2021],
    #   ['Adil Ali Khan', 'EE', 2021], ['Hamza Junaid', 'EE', 2021], ['Sarwan', 'EE', 2021], 
    #   ['Marium Habiby', 'SDP', 2021]
    # ]

    student_records = [
        ['Aazan Ijlal', 'CS', 2021], ['Adina Zuberi', 'SNP', 2020], ['Ahmed Sultan', 'EE', 2021],
        ['Basim Haqqui', 'CND', 2022], ['Syed Pasha', 'EE', 2020], ['Darab Moazzam', 'CS', 2021],
        ['Eesha Sadiq', 'CND', 2022], ['Eman Imam', 'CND', 2020], ['Huzaifa Ahmed', 'EE', 2022],
        ['Maham Jawed', 'EE', 2020], ['Manaal Fatima', 'CND', 2021], ['Mir Akbar', 'CS', 2020],
        ['Muhammad Ali', 'CS', 2020], ['Munsif Rehman', 'CS', 2022], ['Pashmeenay Shahzad', 'SNP', 2021],
        ['Sania Zehra', 'SNP', 2020], ['Sarah Mandviwala', 'CS', 2020], ['Sheryar Ur Rehman', 'EE', 2021],
        ['Tara Vera Ahmed', 'CND', 2022], ['Usman Abdullah', 'CND', 2022]]
    print(special_list_sort(student_records))
    # Should print:
    # [
    #   ['Eman Imam', 'CND', 2020], ['Mir Akbar', 'CS', 2020], ['Muhammad Ali', 'CS', 2020],
    #   ['Sarah Mandviwala', 'CS', 2020], ['Maham Jawed', 'EE', 2020], ['Syed Pasha', 'EE', 2020],
    #   ['Adina Zuberi', 'SNP', 2020], ['Sania Zehra', 'SNP', 2020], ['Manaal Fatima', 'CND', 2021],
    #   ['Aazan Ijlal', 'CS', 2021], ['Darab Moazzam', 'CS', 2021], ['Ahmed Sultan', 'EE', 2021],
    #   ['Sheryar Ur Rehman', 'EE', 2021], ['Pashmeenay Shahzad', 'SNP', 2021], ['Basim Haqqui', 'CND', 2022],
    #   ['Eesha Sadiq', 'CND', 2022], ['Tara Vera Ahmed', 'CND', 2022], ['Usman Abdullah', 'CND', 2022],
    #   ['Munsif Rehman', 'CS', 2022], ['Huzaifa Ahmed', 'EE', 2022]
    # ]

    student_records = []
    print(special_list_sort(student_records))
    # Should print:
    # []

    # -----------------------------------------#
    # ADD YOUR OWN TEST CASES BELOW            #
    # -----------------------------------------#



# -----------------------------------------#
# TESTING ALL TEST CASES                   #
# -----------------------------------------#
# To test your functions, type one of the following commands in the terminal:
# python -m pytest tests/test_q4.py
# python3 -m pytest tests/test_q4.py