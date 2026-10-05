# -----------------------------------------
# EXERCISE ANSWERS
# -----------------------------------------
# +---------------+------------+
# |     Input     |   Output   |
# |     P   R     |            |
# +---------------+------------+
# |     15   5    | 26           |
# |    35   23    | 48           |
# |   123   189   | 58           |
# +---------------+------------+


# -----------------------------------------
# VARIABLES
# -----------------------------------------
# Create the required variables here.
P , R = input("Enter values = ").split()
P = int(P)
R = int(R)
# -----------------------------------------
# COMPUTATIONAL LOGIC AND OUTPUT
# -----------------------------------------
# Write your computational logic and print statement(s) below.
classtotal = 2 * P
count = 1
for i in range(classtotal,0,-1):
    if i == R:
        # print()
        print(count)
        break
    else:
        count += 1
        # print(count)


# -----------------------------------------
# TEST YOUR PROGRAM
# -----------------------------------------
# Use EVERY Sample and Exercise input to test your program.
# Change the variable values to match one input at a time,
# then run the program and check the output.
