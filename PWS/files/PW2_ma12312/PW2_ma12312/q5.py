# -----------------------------------------
# EXERCISE ANSWERS
# -----------------------------------------
# +----------------------+------------+
# |        Input         |   Output   |
# |  A   B   C   D   E   |            |
# +----------------------+------------+
# |  8   5   7  15   6   | Yes           |
# |  8   8   9  16   5   | No           |
# |  10  10  10  20  10  | Yes           |
# +----------------------+------------+


# -----------------------------------------
# VARIABLES
# -----------------------------------------
# Create the required variables here.

A ,B ,C ,D ,E = input("Enter values : ").split()
A = int(A)
B = int(B)
C = int(C)
D = int(D)
E = int(E)
# -----------------------------------------
# COMPUTATIONAL LOGIC AND OUTPUT
# -----------------------------------------
# Write your computational logic and print statement below.

if (A + B <= D and C <= E) or (A + C <= D and B <= E) or (B + C <= D and A <= E):
    print("YES")
else:
    print("NO")

# -----------------------------------------
# TEST YOUR PROGRAM
# -----------------------------------------
# Use EVERY Sample and Exercise input to test your program.
# Change the variable values to match one input at a time,
# then run the program and check the output.
