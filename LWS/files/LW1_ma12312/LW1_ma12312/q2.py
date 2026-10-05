# -----------------------------------------
# EXERCISE ANSWERS
# -----------------------------------------
# +----------------+------------+
# |     Input      |   Output   |
# |    T     C     |            |
# +----------------+------------+
# |   10     3     |   3.0      |
# |  100    10     |   100.0    |
# |  130     4     |   52.0     |
# +----------------+------------+


# -----------------------------------------
# VARIABLES
# -----------------------------------------
# Create the required variables here.

T , C = input("Enter marks = ").split()

# -----------------------------------------
# COMPUTATIONAL LOGIC AND OUTPUT
# -----------------------------------------
# Write your computational logic and print statement below.

T = int(T)
C = int(C)

if (10<=T<=200) and (0<=C<=10):
    divide = T / 10
    multiply = divide * C

# -----------------------------------------
# TEST YOUR PROGRAM
# -----------------------------------------
# Use EVERY Sample and Exercise input to test your program.
# Change the variable values to match one input at a time,
# then run the program and check the output.

print(multiply)