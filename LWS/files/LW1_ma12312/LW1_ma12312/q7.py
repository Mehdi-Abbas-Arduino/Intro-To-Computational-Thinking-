# -----------------------------------------
# EXERCISE ANSWERS
# -----------------------------------------
# +----------------------------+------------+
# |           Input            |   Output   |
# |   rs    cs    rd    cd     |            |
# +----------------------------+------------+
# |    0     0     7     4     |  7          |
# |    3     2    10     9     |  7          |
# |    9     3    17    11     |  8          |
# +----------------------------+------------+


# -----------------------------------------
# VARIABLES
# -----------------------------------------
# Create the required variables here.

rs,cs,rd,cd = input("Enter Values").split()



# -----------------------------------------
# COMPUTATIONAL LOGIC AND OUTPUT
# -----------------------------------------
# Write your computational logic and print statement below.
rs,cs,rd,cd = int(rs),int(cs),int(rd),int(cd)
move = max(rd - rs , cd - cs)

# -----------------------------------------
# TEST YOUR PROGRAM
# -----------------------------------------
# Use EVERY Sample and Exercise input to test your program.
# Change the variable values to match one input at a time,
# then run the program and check the output.

print(move)