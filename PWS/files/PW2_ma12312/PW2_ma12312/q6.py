# -----------------------------------------
# EXERCISE ANSWERS
# -----------------------------------------
# +-----------------+------------+
# |      Input      |   Output   |
# |  d     a     b  |            |
# +-----------------+------------+
# |  4     5     6  | Too Early           |
# |  8    10    12  | Too Early           |
# |  9     2    21  | Pickup Allowed           |
# +-----------------+------------+


# -----------------------------------------
# VARIABLES
# -----------------------------------------
# Create the required variables here.

d,a,b = input("Enter values = ").split()
d = int(d)
a = int(a)
b = int(b)

# -----------------------------------------
# COMPUTATIONAL LOGIC AND OUTPUT
# -----------------------------------------
# Write your computational logic and print statement below.

if d >= a and d <= b :
    print("Pickup Allowed")
elif d < a :
    print("Too Early")
elif d > b:
    print("Too late")

# -----------------------------------------
# TEST YOUR PROGRAM
# -----------------------------------------
# Use EVERY Sample and Exercise input to test your program.
# Change the variable values to match one input at a time,
# then run the program and check the output.
