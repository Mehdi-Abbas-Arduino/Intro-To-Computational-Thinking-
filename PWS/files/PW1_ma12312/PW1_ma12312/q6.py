# -----------------------------------------
# EXERCISE ANSWERS
# -----------------------------------------
# +---------------+------------+
# |     Input     |   Output   |
# |   F   T   R   |            |
# +---------------+------------+
# |   8   5   4   |   8         |
# |   9   7   0   |  63          |
# |   4   5   2   |  12          |
# +---------------+------------+


# -----------------------------------------
# VARIABLES
# -----------------------------------------
# Create the required variables here.

F , T , R = input("Enter the numbers = ").split()
F = int(F)
T = int(T)
R = int(R)
# -----------------------------------------
# COMPUTATIONAL LOGIC AND OUTPUT
# -----------------------------------------
# Write your computational logic and print statement(s) below.

formula = abs((T - R)) * F 

# -----------------------------------------
# TEST YOUR PROGRAM
# -----------------------------------------
# Use EVERY Sample and Exercise input to test your program.
# Change the variable values to match one input at a time,
# then run the program and check the output.
print(formula)