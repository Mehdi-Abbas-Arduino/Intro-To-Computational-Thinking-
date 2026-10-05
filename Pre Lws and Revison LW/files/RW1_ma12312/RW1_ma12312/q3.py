# -----------------------------------------
# EXERCISE ANSWERS
# -----------------------------------------
# +----------------+------------+
# |     Input      |   Output   |
# |       s        |            |
# +----------------+------------+
# |      1312      |  2624.0          |
# |      2300      |  5054.0          |
# |      1899      |  4260.02          |
# +----------------+------------+


# -----------------------------------------
# VARIABLES
# -----------------------------------------
# Create the required variables here.
s = int(input("Enter values = "))
travel = 0
event_bonus = 0
# -----------------------------------------
# COMPUTATIONAL LOGIC AND OUTPUT
# -----------------------------------------
# Write your computational logic and print statement below.
if s < 1500:
    travel = s *(10 / 100)
    event_bonus = s * (90 / 100)
    s = s + travel + event_bonus
elif s > 1500:
    travel = 500
    event_bonus = s * (98/100)
    s = s + travel + event_bonus

print(s)

# -----------------------------------------
# TEST YOUR PROGRAM
# -----------------------------------------
# Use EVERY Sample and Exercise input to test your program.
# Change the variable values to match one input at a time,
# then run the program and check the output.
