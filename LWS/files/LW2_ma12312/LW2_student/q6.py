# -----------------------------------------
# EXERCISE ANSWERS
# -----------------------------------------
# +-----------------------+------------+
# |         Input         |   Output   |
# |  w1    w2    w3    s  |            |
# +-----------------------+------------+
# |  2     1     3     6  |  2          |
# |  8     5     4    10  |  2          |
# |  6     5     6    10  |  3          |
# +-----------------------+------------+

# -----------------------------------------
# VARIABLES
# -----------------------------------------
# Create the required variables here.

w1 , w2, w3, s = input("Enter = ").split()
w1 = int(w1)
w2 = int(w2)
w3 = int(w3)
s = int(s)

# -----------------------------------------
# COMPUTATIONAL LOGIC AND OUTPUT
# -----------------------------------------
# Write your computational logic and print statement below.
count = 0

total = w1 + w2 + w3

if total <= s:
    count = 1

elif w1 + w2 <= s or w1 + w3 <= s or w2 + w3 <= s:
    count = 2

else:
    count = 3

print(count)

# -----------------------------------------
# TEST YOUR PROGRAM
# -----------------------------------------
# Use EVERY Sample and Exercise input to test your program.
# Change the variable values to match one input at a time,
# then run the program and check the output.