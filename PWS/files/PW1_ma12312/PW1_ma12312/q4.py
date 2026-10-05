# -----------------------------------------
# EXERCISE ANSWERS
# -----------------------------------------
# +--------------+------------+
# |    Input     |   Output   |
# |   cp   dr    |            |
# +--------------+------------+
# |   500   0    |  500          |
# |   85   10    |  76.5          |
# |   50   100   |   0.0         |
# +--------------+------------+


# -----------------------------------------
# VARIABLES
# -----------------------------------------
# Create the required variables here.

cp , dr = input("Enter the numbers = ").split()
cp = int(cp)
dr = int(dr)
# -----------------------------------------
# COMPUTATIONAL LOGIC AND OUTPUT
# -----------------------------------------
# Write your computational logic and print statement(s) below.

Discount = cp * (1-(dr/100))

# -----------------------------------------
# TEST YOUR PROGRAM
# -----------------------------------------
# Use EVERY Sample and Exercise input to test your program.
# Change the variable values to match one input at a time,
# then run the program and check the output.
print(Discount)