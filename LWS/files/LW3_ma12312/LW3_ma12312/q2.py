# -----------------------------------------
# DEFINE THE REQUIRED FUNCTION(S)
# -----------------------------------------
# Write your function definition below.
def fan_speed(current_setting,button_presses):
    process = (current_setting + button_presses)
    compute = (process % 4) 
    if compute == 0:
        return ("OFF")
    elif compute == 1:
            return ("LOW")
    elif compute == 2:
            return ("MEDIUM")
    elif compute == 3:
            return ("HIGH")

# -----------------------------------------
# INPUT
# -----------------------------------------
# Read the required input values below.

current_setting = int(input("Enter the value = "))
button_presses = int(input("Enter the value = "))

# -----------------------------------------
# CALL YOUR FUNCTION
# -----------------------------------------
# Call the function and print the returned value.

x = fan_speed(current_setting=current_setting,button_presses=button_presses)
print(x)

# -----------------------------------------
# TEST YOUR PROGRAM
# -----------------------------------------
# Test your program against the following testcases.
# +-----------------+----------------+--------+
# | current_setting | button_presses | Output |
# +-----------------+----------------+--------+
# | 3               | 1              | OFF    |
# | 0               | 11             | HIGH   |
# | 0               | 10             | MEDIUM |
# | 3               | 8348           | HIGH   |
# | 2               | 5903787        | LOW    |
# +-----------------+----------------+--------+