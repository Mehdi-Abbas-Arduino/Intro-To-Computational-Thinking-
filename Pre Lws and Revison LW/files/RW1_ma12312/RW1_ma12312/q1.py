# -----------------------------------------
# EXERCISE ANSWERS
# -----------------------------------------
# +--------------+------------+
# |    Input     |   Output   |
# |    L   D     |            |
# +--------------+------------+
# |    18   3    |    7        |
# |    48   8    |   7         |
# |    63   9    |    8        |
# +--------------+------------+


# -----------------------------------------
# VARIABLES
# -----------------------------------------
# Create the required variables here.
count = 0
L,D = input("Enter values = ").split()
L = int(L)
D = int(D)
l = L // D
# -----------------------------------------
# COMPUTATIONAL LOGIC AND OUTPUT
# -----------------------------------------
# Write your computational logic and print statement(s) below.

for i in range(l + 1):
    n = D * i
    # print(n)
    if n <= L:
        count += 1
    elif n > L :
        break

print(count)

# -----------------------------------------
# TEST YOUR PROGRAM
# -----------------------------------------
# Use EVERY Sample and Exercise input to test your program.
# Change the variable values to match one input at a time,
# then run the program and check the output.

