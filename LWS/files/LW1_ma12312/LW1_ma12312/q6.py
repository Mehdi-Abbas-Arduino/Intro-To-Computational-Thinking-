# -----------------------------------------
# EXERCISE ANSWERS
# -----------------------------------------
# +----------------------+------------+
# |        Input         |   Output   |
# |    F      T      C   |            |
# +----------------------+------------+
# |    4      4   1000   |   0         |
# |   10      5      1   |   100         |
# |   13     31     35   |    10        |
# +----------------------+------------+


# -----------------------------------------
# VARIABLES
# -----------------------------------------
# Create the required variables here.

F, T, C  = input("Enter Values = ").split()

# -----------------------------------------
# COMPUTATIONAL LOGIC AND OUTPUT
# -----------------------------------------
# Write your computational logic and print statement below.
F = int(F)
T = int(T)
C = int(C)

if (1 <= F, T, C <= 1000):
    five = F * 5
    ten = T * 10
    add = five + ten
    tokens = add // C
# -----------------------------------------
# TEST YOUR PROGRAM
# -----------------------------------------
# Use EVERY Sample and Exercise input to test your program.
# Change the variable values to match one input at a time,
# then run the program and check the output.
print(tokens)