# -----------------------------------------
# DEFINE THE REQUIRED FUNCTION
# -----------------------------------------
# Write your function definition below.
def money_changer(reimbursement_amount):
    thousands = reimbursement_amount // 1000
    five = (reimbursement_amount % 1000) // 500
    hundred = (reimbursement_amount % 500) // 100
    ten = (reimbursement_amount % 100) // 10
    ones = reimbursement_amount % 10

    return {
        "1000": thousands,
        "500": five,
        "100": hundred,
        "10": ten,
        "1": ones
    }
# -----------------------------------------
# INPUT
# -----------------------------------------
# Read the required input values below.

reimbursement_amount = int(input("Enter values = "))

# -----------------------------------------
# CALL YOUR FUNCTION
# -----------------------------------------
# Call the function. The function itself prints the required output.
x = money_changer(reimbursement_amount)
print(x)

# -----------------------------------------
# TEST YOUR PROGRAM
# -----------------------------------------
# Test your program against the following testcases.
# +----------------------+------+-----+-----+----+---+
# | reimbursement_amount | 1000 | 500 | 100 | 10 | 1 |
# +----------------------+------+-----+-----+----+---+
# | 10200                | 10   | 0   | 2   | 0  | 0 |
# | 2769                 | 2    | 1   | 2   | 6  | 9 |
# | 7813                 | 7    | 1   | 3   | 1  | 3 |
# | 570                  | 0    | 1   | 0   | 7  | 0 |
# | 9                    | 0    | 0   | 0   | 0  | 9 |
# | 1111                 | 1    | 0   | 1   | 1  | 1 |
# +----------------------+------+-----+-----+----+---+
