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

n , p = input("Enter values : ").split()
n = int(n)
p = int(p)

# -----------------------------------------
# COMPUTATIONAL LOGIC AND OUTPUT
# -----------------------------------------
# Write your computational logic and print statement below.

product = n * p
if product >= 10000 and product <= 99999:
    product = str(product)
    if len(product) == 5:
        print("Yes")
    else:
        print("No")
else:
    print("No")

# -----------------------------------------
# TEST YOUR PROGRAM
# -----------------------------------------
# Use EVERY Sample and Exercise input to test your program.
# Change the variable values to match one input at a time,
# then run the program and check the output.
