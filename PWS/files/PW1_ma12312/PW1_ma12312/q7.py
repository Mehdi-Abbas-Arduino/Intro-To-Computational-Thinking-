# -----------------------------------------
# EXERCISE ANSWERS
# -----------------------------------------
# +--------------+------------+
# |    Input     |   Output   |
# |    C   E     |            |
# +--------------+------------+
# |    50   2    |   0         |
# |    8   68    |   8         |
# |    9   23    |   2         |
# +--------------+------------+


# -----------------------------------------
# VARIABLES
# -----------------------------------------
# Create the required variables here.

C , E = input("Enter values = ").split()
C = int(C)
E = int(E)
# -----------------------------------------
# COMPUTATIONAL LOGIC AND OUTPUT
# -----------------------------------------
# Write your computational logic and print statement(s) below.

compute = E // C

# -----------------------------------------
# TEST YOUR PROGRAM
# -----------------------------------------
# Use EVERY Sample and Exercise input to test your program.
# Change the variable values to match one input at a time,
# then run the program and check the output.
print(compute)