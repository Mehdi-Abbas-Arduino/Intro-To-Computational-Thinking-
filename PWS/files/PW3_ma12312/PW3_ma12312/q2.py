# -----------------------------------------
# DEFINE THE REQUIRED FUNCTION
# -----------------------------------------
# Write your function definition below.
def can_agree_on_temperature(ali_min_temp,raahim_max_temp,saad_min_temp):
    if raahim_max_temp >= ali_min_temp and raahim_max_temp >= saad_min_temp:
        return "Yes"
    else:
        return "No"


# -----------------------------------------
# INPUT
# -----------------------------------------
# Read the required input values below.
ali_min_temp,raahim_max_temp,saad_min_temp = input("Enter values = ").split()
ali_min_temp = int(ali_min_temp)
raahim_max_temp = int(raahim_max_temp)
saad_min_temp = int(saad_min_temp)


# -----------------------------------------
# CALL YOUR FUNCTION
# -----------------------------------------
# Call the function and print the returned value.

x = can_agree_on_temperature(ali_min_temp,raahim_max_temp,saad_min_temp)
print(x)
# -----------------------------------------
# TEST YOUR PROGRAM
# -----------------------------------------
# Test your program against the following testcases.
# +--------------+-----------------+---------------+--------+
# | ali_min_temp | raahim_max_temp | saad_min_temp | Output |
# +--------------+-----------------+---------------+--------+
# | 22           | 25              | 20            | YES    |
# | 24           | 22              | 23            | NO     |
# | 24           | 24              | 20            | YES    |
# | 21           | 24              | 24            | YES    |
# | 25           | 23              | 20            | NO     |
# | 19           | 28              | 22            | YES    |
# +--------------+-----------------+---------------+--------+