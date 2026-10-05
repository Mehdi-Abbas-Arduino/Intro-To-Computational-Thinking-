# -----------------------------------------
# DEFINE THE REQUIRED FUNCTION(S)
# -----------------------------------------
# Write your function definition below.
def decode_clue(clue_number):
    # first_value = clue_number // 10000
    # second_value = clue_number // 1000
    # second_value_real = second_value % 10
    # third_value = clue_number // 100
    # third_value_real = third_value % 10
    # fourth_value = clue_number // 10
    # fourth_value_real = fourth_value %10
    # fifth_value = clue_number % 10
    # print(first_value,second_value_real,third_value_real,fourth_value_real,fifth_value)
    i = 5
    total = 0
    while clue_number > 0:
        n = clue_number % 10
        clue_number = clue_number // 10
        total += (n * i)
        i = i - 1
    # product = (first_value*1) + (second_value_real * 2) + (third_value_real * 3) + (fourth_value_real*4) + (fifth_value*5)
    return total


# -----------------------------------------
# INPUT
# -----------------------------------------
# Read the required input values below.
clue_number = int(input("Enter the number = "))
# -----------------------------------------
# CALL YOUR FUNCTION
# -----------------------------------------
# Call the function and print the returned value.

x = decode_clue(clue_number=clue_number)
print(x)
# -----------------------------------------
# TEST YOUR PROGRAM
# -----------------------------------------
# Test your program against the following testcases.
# +-------------+--------+
# | clue_number | Output |
# +-------------+--------+
# | 58324       | 58     |
# | 91736       | 74     |
# | 42618       | 70     |
# | 73105       | 41     |
# | 99999       | 135    |
# +-------------+--------+