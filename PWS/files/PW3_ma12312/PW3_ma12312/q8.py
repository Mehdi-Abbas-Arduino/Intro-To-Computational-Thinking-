# -----------------------------------------
# DEFINE THE REQUIRED FUNCTION(S)
# -----------------------------------------
# Write your function definition(s) below.


def get_letter_grade(mark):

    if mark <= 100 and mark > 95:
        return "A+"
    elif mark <= 95 and mark > 90:
        return 'A'
    elif mark <= 90 and mark > 85 :
        return 'A-'
    elif mark <= 85 and mark > 80:
        return 'B+'
    elif mark <= 80 and mark > 75:
        return 'B'
    elif mark <= 75 and mark > 70:
        return 'B-'
    elif mark <= 70 and mark > 67:
        return 'C+'
    elif mark <= 67 and mark > 63:
        return 'C'
    elif mark <= 63 and mark > 60 :
        return 'C-'
    else:
        return 'F'
    
def get_grade_point(letter_grade):
    if letter_grade == 'A+':
        return 4.00
    elif letter_grade == 'A':
        return 4.00
    elif letter_grade == 'A-':
        return 3.67
    elif letter_grade == 'B+':
        return 3.33
    elif letter_grade == 'B':
        return 3.00
    elif letter_grade == 'B-':
        return 2.67
    elif letter_grade == 'C+':
        return 2.33
    elif letter_grade == 'C':
        return 2.00
    elif letter_grade == 'C-':
        return 1.67
    elif letter_grade == 'F':
        return 0.00
        
def gpa_calculator(course_1_mark,course_2_mark,course_3_mark,course_4_mark):
    first = get_letter_grade(course_1_mark)
    second = get_letter_grade(course_2_mark)
    third = get_letter_grade(course_3_mark)
    fourth = get_letter_grade(course_4_mark)
    print(f"Your grades are {first},{second},{third},{fourth}")
    gpa_one = get_grade_point(first)
    gpa_two = get_grade_point(second)
    gpa_three = get_grade_point(third)
    gpa_four = get_grade_point(fourth)
    avg_gpa = round(((gpa_one + gpa_two + gpa_three + gpa_four) / 4),2)
    print(f"Your GPA is : {avg_gpa}")
# -----------------------------------------
# INPUT
# -----------------------------------------
# Read the required input values below.

course_1_mark,course_2_mark,course_3_mark,course_4_mark = input("Enter the value = ").split()
course_1_mark = int(course_1_mark)
course_2_mark = int(course_2_mark)
course_3_mark = int(course_3_mark)
course_4_mark = int(course_4_mark)
# -----------------------------------------
# CALL YOUR FUNCTION
# -----------------------------------------
# Call the main function. The function itself prints the required output.

x = gpa_calculator(course_1_mark,course_2_mark,course_3_mark,course_4_mark)

# -----------------------------------------
# TEST YOUR PROGRAM
# -----------------------------------------
# Test your program against the following testcases.
# +---------------+---------------+---------------+---------------+-------------------------------+
# | course_1_mark | course_2_mark | course_3_mark | course_4_mark | Output                        |
# +---------------+---------------+---------------+---------------+-------------------------------+
# | 100           | 77            | 64            | 30            | Your grades are A+ B C F      |
# |               |               |               |               | Your GPA is 2.25              |
# |-----------------------------------------------------------------------------------------------|
# | 75            | 91            | 66            | 50            | Your grades are B A C F       |
# |               |               |               |               | Your GPA is 2.25              |
# |-----------------------------------------------------------------------------------------------|
# | 95            | 82            | 71            | 61            | Your grades are A+ B+ B- C-   |
# |               |               |               |               | Your GPA is 2.92              |
# |-----------------------------------------------------------------------------------------------|
# | 89            | 68            | 63            | 59            | Your grades are A- C+ C F     |
# |               |               |               |               | Your GPA is 2.0               |
# |-----------------------------------------------------------------------------------------------|
# | 61            | 69            | 91            | 88            | Your grades are C- C+ A A-    |
# |               |               |               |               | Your GPA is 2.92              |
# |-----------------------------------------------------------------------------------------------|
# | 64            | 69            | 79            | 95            | Your grades are C C+ B A+     |
# |               |               |               |               | Your GPA is 2.83              |
# +---------------+---------------+---------------+---------------+-------------------------------+