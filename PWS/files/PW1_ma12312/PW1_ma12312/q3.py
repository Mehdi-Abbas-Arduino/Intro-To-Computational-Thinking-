# -----------------------------------------
# EXERCISE ANSWERS
# -----------------------------------------
# +----------------+------------+
# |     Input      |   Output   |
# |   R   C   E    |            |
# +----------------+------------+
# |   7   3   2    |  27          |
# |   3   19   8   |  209          |
# |   17   5   6   |  115          |
# +----------------+------------+


# -----------------------------------------
# VARIABLES
# -----------------------------------------
# Create the required variables here.

R,C,E = input("Enter numbers = ").split()
R = int(R)
C = int(C)
E = int(E)
# -----------------------------------------
# COMPUTATIONAL LOGIC AND OUTPUT
# -----------------------------------------
# Write your computational logic and print statement(s) below.
product = (R + E) * C

# -----------------------------------------
# TEST YOUR PROGRAM
# -----------------------------------------
# Use EVERY Sample and Exercise input to test your program.
# Change the variable values to match one input at a time,
# then run the program and check the output.
print(product)