# -----------------------------------------
# EXERCISE ANSWERS
# -----------------------------------------
# +---------------------+------------+
# |        Input        |   Output   |
# |  d1   d2   p1   p2  |            |
# +---------------------+------------+
# |  7     2    7    2  |    0        |
# |  10    3    5   12  |    -1        |
# |  12    3    2    9  |   -1         |
# +---------------------+------------+


# -----------------------------------------
# VARIABLES
# -----------------------------------------
# Create the required variables here.

d1 ,d2 ,p1 ,p2 = input("Enter values : ").split()
d1 = int(d1)
d2 = int(d2)
p1 = int(p1)
p2 = int(p2)

# -----------------------------------------
# COMPUTATIONAL LOGIC AND OUTPUT
# -----------------------------------------
# Write your computational logic and print statement below.

opt1 = p1/d1
opt2 = p2/d2
if opt1 < opt2:
    print(-1)
elif opt2 < opt1 :
    print(1)
else:
    print(0)


# -----------------------------------------
# TEST YOUR PROGRAM
# -----------------------------------------
# Use EVERY Sample and Exercise input to test your program.
# Change the variable values to match one input at a time,
# then run the program and check the output.
