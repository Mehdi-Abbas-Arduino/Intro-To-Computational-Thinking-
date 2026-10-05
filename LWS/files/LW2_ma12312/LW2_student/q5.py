# -----------------------------------------
# EXERCISE ANSWERS
# -----------------------------------------
# +----------------+------------+
# |     Input      |   Output   |
# |       g        |            |
# +----------------+------------+
# |       29       |   29         |
# |       78       |   80         |
# |       51       |   51         |
# +----------------+------------+

# -----------------------------------------
# VARIABLES
# -----------------------------------------
# Create the required variable here.

g = int(input("Enter the number = "))

# -----------------------------------------
# COMPUTATIONAL LOGIC AND OUTPUT
# -----------------------------------------
# Write your computational logic and print statement below.
if g > 38:
    if (g+1) % 5 == 0:
        g = g + 1
        print(g)
    elif (g + 2) % 5 == 0:
        g = g + 2
        print(g)
    elif (g) % 5 == 0:
        print(g)
    else:
        print(g)

# -----------------------------------------
# TEST YOUR PROGRAM
# -----------------------------------------
# Use EVERY Sample and Exercise input to test your program.
# Change the variable values to match one input at a time,
# then run the program and check the output.