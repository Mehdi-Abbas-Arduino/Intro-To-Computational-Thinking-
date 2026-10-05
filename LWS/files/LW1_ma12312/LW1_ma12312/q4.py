# -----------------------------------------
# EXERCISE ANSWERS
# -----------------------------------------
# +----------------------+------------+
# |        Input         |   Output   |
# |    L      W      C   |            |
# +----------------------+------------+
# |   11     15     50   |  2600          |
# | 1000   1000   1000   |  4000000          |
# |   67     37     23   |  4784          |
# +----------------------+------------+


# -----------------------------------------
# VARIABLES
# -----------------------------------------
# Create the required variables here.

L ,W, C = input("Enter values = ").split()

# -----------------------------------------
# COMPUTATIONAL LOGIC AND OUTPUT
# -----------------------------------------
# Write your computational logic and print statement below.
L = int(L)
W = int(W)
C = int(C)
if (1<=L,W,C<=1000):
    perimeter = 2*(L + W)
    Cost = perimeter * C


# -----------------------------------------
# TEST YOUR PROGRAM
# -----------------------------------------
# Use EVERY Sample and Exercise input to test your program.
# Change the variable values to match one input at a time,
# then run the program and check the output.

print(Cost)