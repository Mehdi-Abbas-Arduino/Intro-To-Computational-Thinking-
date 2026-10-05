# -----------------------------------------
# EXERCISE ANSWERS
# -----------------------------------------
# +----------------+------------+
# |     Input      |   Output   |
# |    W     D     |            |
# +----------------+------------+
# |    3    16     |   5         |
# |    5     7     |   28         |
# |    6    12     |   30         |
# +----------------+------------+


# -----------------------------------------
# VARIABLES
# -----------------------------------------
# Create the required variables here.
W , D = input("Enter the number = ").split()

# -----------------------------------------
# COMPUTATIONAL LOGIC AND OUTPUT
# -----------------------------------------
# Write your computational logic and print statement below.
W = int(W)
D = int(D)

if (1 <= W <= 10) and (1 <= D < 7*W):
    DayW = 7 * W
    remain = DayW - D

# -----------------------------------------
# TEST YOUR PROGRAM
# -----------------------------------------
# Use EVERY Sample and Exercise input to test your program.
# Change the variable values to match one input at a time,
# then run the program and check the output.

print(remain)