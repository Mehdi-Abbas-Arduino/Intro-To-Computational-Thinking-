# -----------------------------------------
# EXERCISE ANSWERS
# -----------------------------------------
# +----------------+------------+
# |     Input      |   Output   |
# |       m        |            |
# +----------------+------------+
# |       8        |  North          |
# |       15       |  West          |
# |      253       |  East          |
# +----------------+------------+

# -----------------------------------------
# VARIABLES
# -----------------------------------------
# Create the required variable here.

m = int(input("Enter the number = "))

# -----------------------------------------
# COMPUTATIONAL LOGIC AND OUTPUT
# -----------------------------------------
# Write your computational logic and print statement below.

compute = (m % 4) 
if compute == 1:
    print("East")

if compute == 2:
    print("South")
if compute == 3:
    print("West")
if compute == 0:
    print("North")
# -----------------------------------------
# TEST YOUR PROGRAM
# -----------------------------------------
# Use EVERY Sample and Exercise input to test your program.
# Change the variable values to match one input at a time,
# then run the program and check the output.