# -----------------------------------------
# DEFINE THE REQUIRED FUNCTION
# -----------------------------------------
# Write your function definition below.

def split_gum_cost(gum_packs,friend_count):
    gum = 150
    total = gum_packs * gum
    amount = total // (friend_count + 1)
    amount_dollars_dollar = amount // 100
    amount_dollars_cents = amount % 100
    return(f"Each student spends {amount_dollars_dollar} dollars and {amount_dollars_cents} cents. ")

# -----------------------------------------
# INPUT
# -----------------------------------------
# Read the required input values below.

gum_packs = int(input("Enter values = "))
friend_count = int(input("Enter values = "))

# -----------------------------------------
# CALL YOUR FUNCTION
# -----------------------------------------
# Call the function. The function itself prints the required output.

x = split_gum_cost(gum_packs,friend_count)
print(x)

# -----------------------------------------
# TEST YOUR PROGRAM
# -----------------------------------------
# Test your program against the following testcases.
# +-----------+--------------+--------------------------------------------+
# | gum_packs | friend_count | Output                                     |
# +-----------+--------------+--------------------------------------------+
# | 5         | 2            | Each person spends 2 dollars and 50 cents  |
# | 3         | 1            | Each person spends 2 dollars and 25 cents  |
# | 4         | 2            | Each person spends 2 dollars and 0 cents   |
# | 8         | 4            | Each person spends 2 dollars and 40 cents  |
# | 99        | 10           | Each person spends 13 dollars and 50 cents |
# | 1         | 1            | Each person spends 0 dollars and 75 cents  |
# | 6         | 3            | Each person spends 2 dollars and 25 cents  |
# | 10        | 4            | Each person spends 3 dollars and 0 cents   |
# | 24        | 7            | Each person spends 4 dollars and 50 cents  |
# +-----------+--------------+--------------------------------------------+