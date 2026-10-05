# -----------------------------------------
# EXERCISE ANSWERS
# -----------------------------------------
# +-----------------+------------+
# |      Input      |   Output   |
# |  x     n     y  |            |
# +-----------------+------------+
# |  99   11    9   |  Yes          |
# |  45    6    7   |  No          |
# |  5     1    5   |  Yes          |
# +-----------------+------------+


# -----------------------------------------
# VARIABLES
# -----------------------------------------
# Create the required variables here.

x ,n ,y = input("Enter values : ").split()
x = int(x)
n = int(n)
y = int(y)

# -----------------------------------------
# COMPUTATIONAL LOGIC AND OUTPUT
# -----------------------------------------
# Write your computational logic and print statement below.

compute = n * y
if compute < x :
    print("No")
else:
    print("Yes")

# -----------------------------------------
# TEST YOUR PROGRAM
# -----------------------------------------
# Use EVERY Sample and Exercise input to test your program.
# Change the variable values to match one input at a time,
# then run the program and check the output.
