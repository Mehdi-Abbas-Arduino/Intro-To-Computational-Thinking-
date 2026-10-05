# -----------------------------------------
# EXERCISE ANSWERS
# -----------------------------------------
# +--------------+------------+
# |    Input     |   Output   |
# |    S   E     |            |
# +--------------+------------+
# |    1   3     |    2        |
# |    3   7     |    4        |
# |    9   11    |    2        |
# +--------------+------------+


# -----------------------------------------
# VARIABLES
# -----------------------------------------
# Create the required variables here.
S , E = input("Enter values = ").split()
S = int(S)
E = int(E)
# -----------------------------------------
# COMPUTATIONAL LOGIC AND OUTPUT
# -----------------------------------------
# Write your computational logic and print statement(s) below.

Time = E - S


# -----------------------------------------
# TEST YOUR PROGRAM
# -----------------------------------------
# Use EVERY Sample and Exercise input to test your program.
# Change the variable values to match one input at a time,
# then run the program and check the output.
print(Time)