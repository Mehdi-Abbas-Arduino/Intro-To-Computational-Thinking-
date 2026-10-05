# -----------------------------------------
# EXERCISE ANSWERS
# -----------------------------------------
# +----------------+------------+
# |     Input      |   Output   |
# |    n     p     |            |
# +----------------+------------+
# |   100   100    |   Yes         |
# |   33     12    |   No         |
# |   130   120    |   Yes         |
# +----------------+------------+


# -----------------------------------------
# VARIABLES
# -----------------------------------------
# Create the required variables here.

n,p = input("Enter values = ").split()
n = int(n)
p = int(p)

# -----------------------------------------
# COMPUTATIONAL LOGIC AND OUTPUT
# -----------------------------------------
# Write your computational logic and print statement below.

total = n * p
count = 0
while total > 0:
    total = total // 10
    count += 1
    

if count == 5:
    print("Yes")
else:
    print("No")

# -----------------------------------------
# TEST YOUR PROGRAM
# -----------------------------------------
# Use EVERY Sample and Exercise input to test your program.
# Change the variable values to match one input at a time,
# then run the program and check the output.
