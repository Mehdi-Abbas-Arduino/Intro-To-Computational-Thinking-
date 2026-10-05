# -----------------------------------------
# EXERCISE ANSWERS
# -----------------------------------------
# +----------------+------------+
# |     Input      |   Output   |
# |       p        |            |
# +----------------+------------+
# |      2500      |   Yes         |
# |      2800      |   No         |
# |      2600      |   No         |
# +----------------+------------+

# -----------------------------------------
# VARIABLES
# -----------------------------------------
# Create the required variable here.

p = int(input("Enter the ticket costs = "))
total = 10000
# -----------------------------------------
# COMPUTATIONAL LOGIC AND OUTPUT
# -----------------------------------------
# Write your computational logic and print statement below.

share = p * 4
if share > total :
    print("No")
else:
    print("Yes")
# -----------------------------------------
# TEST YOUR PROGRAM
# -----------------------------------------
# Use EVERY Sample and Exercise input to test your program.
# Change the variable values to match one input at a time,
# then run the program and check the output.