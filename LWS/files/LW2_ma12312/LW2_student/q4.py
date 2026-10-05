# -----------------------------------------
# EXERCISE ANSWERS
# -----------------------------------------
# +------------------+------------+
# |      Input       |   Output   |
# |  A     B     C   |            |
# +------------------+------------+
# |  18   271   31   | 302           |
# |  127  2933  182  | 3115           |
# |  21    2    18   | 39           |
# +------------------+------------+

# -----------------------------------------
# VARIABLES
# -----------------------------------------
# Create the required variables here.

A ,B ,C = input("Enter the number = ").split()
A = int(A)
B = int(B)
C = int(C)
# -----------------------------------------
# COMPUTATIONAL LOGIC AND OUTPUT
# -----------------------------------------
# Write your computational logic and print statement below.
lowest = 100000001
total = 0
if A < lowest:
    lowest = A
    total = B + C
if B < lowest:
    lowest = B
    total = A + C
if C < lowest:
    lowest = C
    total = A + B

print(total)



# -----------------------------------------
# TEST YOUR PROGRAM
# -----------------------------------------
# Use EVERY Sample and Exercise input to test your program.
# Change the variable values to match one input at a time,
# then run the program and check the output.