# -----------------------------------------
# EXERCISE ANSWERS
# -----------------------------------------
# +----------------+------------+
# |     Input      |   Output   |
# |       s        |            |
# +----------------+------------+
# |      1312      | 2624.0           |
# |      2300      | 5054.0           |
# |      1899      | 4260.02           |
# +----------------+------------+


# -----------------------------------------
# VARIABLES
# -----------------------------------------
# Create the required variables here.

s = int(input("Enter the number : "))

# -----------------------------------------
# COMPUTATIONAL LOGIC AND OUTPUT
# -----------------------------------------
# Write your computational logic and print statement below.

if s < 1500:
    total = s + (0.1 * s) + (0.9 * s)
else:
    total = s + 500 + (0.98 * s)
    
print(total)
# -----------------------------------------
# TEST YOUR PROGRAM
# -----------------------------------------
# Use EVERY Sample and Exercise input to test your program.
# Change the variable values to match one input at a time,
# then run the program and check the output.
