# -----------------------------------------
# EXERCISE ANSWERS
# -----------------------------------------
# +----------------+------------+
# |     Input      |   Output   |
# |       k        |            |
# +----------------+------------+
# |       12       |    12        |
# |       8        |     8       |
# |       31       |     33       |
# +----------------+------------+


# -----------------------------------------
# VARIABLES
# -----------------------------------------
# Create the required variables here.

k = int(input("Enter values : "))

# -----------------------------------------
# COMPUTATIONAL LOGIC AND OUTPUT
# -----------------------------------------
# Write your computational logic and print statement below.
if k % 2 != 0:
    val = k - 1
    vals = val // 2
    answer = vals * (3-1)
    answer = answer + 3 
    print(answer)
elif k%2 == 0:
    vals = k // 2
    answer = vals * (3-1)
    print(answer)

# -----------------------------------------
# TEST YOUR PROGRAM
# -----------------------------------------
# Use EVERY Sample and Exercise input to test your program.
# Change the variable values to match one input at a time,
# then run the program and check the output.
