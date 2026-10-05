# -----------------------------------------
# EXERCISE ANSWERS
# -----------------------------------------
# +-------------------+------------+
# |       Input       |   Output   |
# |     F   C   W     |            |
# +-------------------+------------+
# |    1350   5   4   |    27000        |
# |    500   7   52   |   182000         |
# |   1337   3   10   |   40110         |
# +-------------------+------------+


# -----------------------------------------
# VARIABLES
# -----------------------------------------
# Create the required variables here.

F ,C ,W = input("Enter the numbers = ").split()

F = int(F)
C = int(C)
W = int(W)
# -----------------------------------------
# COMPUTATIONAL LOGIC AND OUTPUT
# -----------------------------------------
# Write your computational logic and print statement(s) below.

product = C * W
end_product = product * F

# -----------------------------------------
# TEST YOUR PROGRAM
# -----------------------------------------
# Use EVERY Sample and Exercise input to test your program.
# Change the variable values to match one input at a time,
# then run the program and check the output.
print(end_product)