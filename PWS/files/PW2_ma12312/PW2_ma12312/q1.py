# -----------------------------------------
# EXERCISE ANSWERS
# -----------------------------------------
# +----------------+------------+
# |     Input      |   Output   |
# |    x     y     |            |
# +----------------+------------+
# |    6    17     |  CRIT          |
# |    10   10     |  CRIT          |
# |    7    12     |  NO CRIT          |
# +----------------+------------+


# -----------------------------------------
# VARIABLES
# -----------------------------------------
# Create the required variables here.
x,y = input("Enter the value = ").split()

x = int(x)
y = int(y)

# -----------------------------------------
# COMPUTATIONAL LOGIC AND OUTPUT
# -----------------------------------------
# Write your computational logic and print statement below.

total = x + y
if total >= 20:
    print("CRIT")
else:
    print("NO CRIT")


# -----------------------------------------
# TEST YOUR PROGRAM
# -----------------------------------------
# Use EVERY Sample and Exercise input to test your program.
# Change the variable values to match one input at a time,
# then run the program and check the output.
