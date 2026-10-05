# -----------------------------------------
# EXERCISE ANSWERS
# -----------------------------------------
# +---------------------+------------+
# |        Input        |   Output   |
# |  r1   c1   r2   c2  |            |
# +---------------------+------------+
# |  1    2    1    5   | Yes           |
# |  2    4    4    8   | No           |
# |  3    3    4    3   | Yes           |
# +---------------------+------------+

# -----------------------------------------
# VARIABLES
# -----------------------------------------
# Create the required variables here.
r1,c1,r2,c2 = input("Enter the positions = ").split()
r1 = int(r1)
r2 = int(r2)
c1 = int(c1)
c2 = int(c2)

# -----------------------------------------
# COMPUTATIONAL LOGIC AND OUTPUT
# -----------------------------------------
# Write your computational logic and print statement below.

if c1 == c2 or r1 == r2:
    print("Yes")
else:
    print("No")

# -----------------------------------------
# TEST YOUR PROGRAM
# -----------------------------------------
# Use EVERY Sample and Exercise input to test your program.
# Change the variable values to match one input at a time,
# then run the program and check the output.