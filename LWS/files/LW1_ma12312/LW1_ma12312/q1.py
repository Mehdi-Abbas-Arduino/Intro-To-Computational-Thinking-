# -----------------------------------------
# EXERCISE ANSWERS
# -----------------------------------------
# +----------------+------------+
# |     Input      |   Output   |
# |    N     K     |            |
# +----------------+------------+
# |   50     0     |   50       |
# |  100    50     |   50       |
# |   25    12     |   13       |
# +----------------+------------+


# -----------------------------------------
# VARIABLES
# -----------------------------------------
# Create the required variables here.
N , K = input("Enter N and K = ").split()

# -----------------------------------------
# COMPUTATIONAL LOGIC AND OUTPUT
# -----------------------------------------
# Write your computational logic and print statement below.
N = int(N)
K = int(K)
if (1<=N<=100) and (0<=K<=N):
    Result = N - K
# -----------------------------------------
# TEST YOUR PROGRAM
# -----------------------------------------
# Use EVERY Sample and Exercise input to test your program.
# Change the variable values to match one input at a time,
# then run the program and check the output.

print(Result)