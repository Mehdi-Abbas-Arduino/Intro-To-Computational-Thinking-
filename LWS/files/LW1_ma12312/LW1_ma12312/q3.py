# -----------------------------------------
# EXERCISE ANSWERS
# -----------------------------------------
# +----------------------------+------------+
# |           Input            |   Output   |
# |   b     f      B      F    |            |
# +----------------------------+------------+
# |  100   450   1000   1350   | 13          |
# |  200   500   1200   1500   | 9           |
# |  150   500   1050   1500   | 10          |
# +----------------------------+------------+


# -----------------------------------------
# VARIABLES
# -----------------------------------------
# Create the required variables here.

b, f, B, F = input("Enter the number = ").split()


# -----------------------------------------
# COMPUTATIONAL LOGIC AND OUTPUT
# -----------------------------------------
# Write your computational logic and print statement below.
b, f, B, F = int(b),int(f),int(B),int(F)

# 100 ≤ b ≤ 200
# • 400 ≤ f ≤ 500
# • 1000 ≤ B ≤ 1200
# • 1000 ≤ F ≤ 1500
if (100 <= b <= 200) and (400 <= f <= 500) and (1000 <= B <= 1200) and (1000 <= F <= 1500) :
    base = B//b
    fruit = F//f
add = base + fruit
# -----------------------------------------
# TEST YOUR PROGRAM
# -----------------------------------------
# Use EVERY Sample and Exercise input to test your program.
# Change the variable values to match one input at a time,
# then run the program and check the output.

print(add)