# -----------------------------------------
# DEFINE THE REQUIRED FUNCTION(S)
# -----------------------------------------
# Write your function definition below.
def format_name(name,order_hour):
    if order_hour > 19 and order_hour <= 24:
        name = name.upper()
    elif order_hour <= 19:
        name = name.lower()

    return name


# -----------------------------------------
# INPUT
# -----------------------------------------
# Read the required input values below.
name = input("Enter name = ")
order_hours = int(input("Enter order hours = "))

# -----------------------------------------
# CALL YOUR FUNCTION
# -----------------------------------------
# Call the function. The function itself prints the required output.

x = format_name(name,order_hours)
print(x)


# -----------------------------------------
# TEST YOUR PROGRAM
# -----------------------------------------
# Test your program against the following testcases.
# +--------+------------+--------+
# | name   | order_hour | Output |
# +--------+------------+--------+
# | waQar  | 20         | WAQAR  |
# | FatIMA | 19         | fatima |
# | AHMED  | 22         | AHMED  |
# | kaRIm  | 5          | karim  |
# | uShNa  | 10         | ushna  |
# +--------+------------+--------+