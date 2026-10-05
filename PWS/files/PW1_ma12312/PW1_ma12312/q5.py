# -----------------------------------------
# EXERCISE ANSWERS
# -----------------------------------------
# +--------------+------------+
# |    Input     |   Output   |
# |    F   S     |            |
# +--------------+------------+
# |    50   2    |   264         |
# |    8   68    |  516          |
# |    9   23    |  206          |
# +--------------+------------+


# -----------------------------------------
# VARIABLES
# -----------------------------------------
# Create the required variables here.

F, S = input("Enter the numbers = ").split()
F = int(F)
S = int(S)


# -----------------------------------------
# COMPUTATIONAL LOGIC AND OUTPUT
# -----------------------------------------
# Write your computational logic and print statement(s) below.

formula = (F * 5) + (S * 7)

# -----------------------------------------
# TEST YOUR PROGRAM
# -----------------------------------------
# Use EVERY Sample and Exercise input to test your program.
# Change the variable values to match one input at a time,
# then run the program and check the output.
print(formula)