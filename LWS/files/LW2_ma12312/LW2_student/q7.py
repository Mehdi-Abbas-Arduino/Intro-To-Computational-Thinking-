# -----------------------------------------
# EXERCISE ANSWERS
# -----------------------------------------
# +----------------+------------+
# |     Input      |   Output   |
# |       A        |            |
# +----------------+------------+
# |       14       | Alice           |
# |       21       | Charlie           |
# |       63       | Bob           |
# +----------------+------------+

# -----------------------------------------
# VARIABLES
# -----------------------------------------
A = int(input("Enter the number = "))

# -----------------------------------------
# DEBUGGING TASK
# -----------------------------------------
# The code below is intended to solve the problem, but it contains logical errors.
# Run the program using provided sample and exercise inputs, 
# identify the logical errors,
# and correct the code so that it produces the expected outputs.

if (A % 2 == 0) and (A % 7 == 0):
    print("Alice")
elif (A % 2 != 0) and (A % 9 == 0):
    print("Bob")
else:
    print("Charlie")