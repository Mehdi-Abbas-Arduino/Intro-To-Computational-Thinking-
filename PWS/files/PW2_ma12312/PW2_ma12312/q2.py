# -----------------------------------------
# EXERCISE ANSWERS
# -----------------------------------------
# +-----------------+------------+
# |      Input      |   Output   |
# |  a   c   b   d  |            |
# +-----------------+------------+
# |  2   2   2   2  |  Possible          |
# |  0   1   8   0  | Impossible           |
# |  9   9   7  13  | Impossible           |
# +-----------------+------------+


# -----------------------------------------
# VARIABLES
# -----------------------------------------
# Create the required variables here.

a ,c ,b ,d = input("Enter the values : ").split()
a = int(a)
c = int(c)
b = int(b)
d = int(d)
# -----------------------------------------
# COMPUTATIONAL LOGIC AND OUTPUT
# -----------------------------------------
# Write your computational logic and print statement below.

if b < a or d < c :
     print("Impossible")
else:
    print("Possible")
        


# -----------------------------------------
# TEST YOUR PROGRAM
# -----------------------------------------
# Use EVERY Sample and Exercise input to test your program.
# Change the variable values to match one input at a time,
# then run the program and check the output.
