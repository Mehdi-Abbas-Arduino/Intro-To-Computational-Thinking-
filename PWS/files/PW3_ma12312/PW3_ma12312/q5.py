# -----------------------------------------
# DEFINE THE REQUIRED FUNCTION
# -----------------------------------------
# Write your function definition below.

def pugam_pugai(areeba_hand,bilal_hand,zoya_hand):
    if areeba_hand != bilal_hand and areeba_hand != zoya_hand:
        return "Areeba"
    elif bilal_hand != areeba_hand and bilal_hand != zoya_hand:
        return "Bilal"
    elif zoya_hand != bilal_hand and zoya_hand != areeba_hand:
        return "Zoya"
    elif zoya_hand == bilal_hand == areeba_hand:
        return "Draw"

# -----------------------------------------
# INPUT
# -----------------------------------------
# Read the required input values below.
areeba_hand,bilal_hand,zoya_hand = input("Enter values : ").upper().split()


# -----------------------------------------
# CALL YOUR FUNCTION
# -----------------------------------------
# Call the function and print the returned value.

x = pugam_pugai(areeba_hand,bilal_hand,zoya_hand)
print(x)

# -----------------------------------------
# TEST YOUR PROGRAM
# -----------------------------------------
# Test your program against the following testcases.
# +-------------+------------+-----------+--------+
# | areeba_hand | bilal_hand | zoya_hand | Output |
# +-------------+------------+-----------+--------+
# | DOWN        | UP         | UP        | Areeba |
# | DOWN        | UP         | DOWN      | Bilal  |
# | UP          | UP         | DOWN      | Zoya   |
# | UP          | UP         | UP        | Draw   |
# | DOWN        | DOWN       | DOWN      | Draw   |
# | UP          | DOWN       | UP        | Bilal  |
# | DOWN        | DOWN       | UP        | Zoya   |
# | UP          | DOWN       | DOWN      | Areeba |
# +-------------+------------+-----------+--------+