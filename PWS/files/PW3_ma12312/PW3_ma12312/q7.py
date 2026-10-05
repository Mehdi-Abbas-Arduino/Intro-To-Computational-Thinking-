# -----------------------------------------
# DEFINE THE REQUIRED FUNCTION
# -----------------------------------------
# Write your function definition below.
def time_conversion(hour_24, minute):
    
    if minute > 60:
        if minute == 60:
            minute = '00'
        else:
            return "Invalid"
        
    if hour_24 < 0 or hour_24 >= 24:
        return "Invalid"
    if hour_24 == 0:
        hour_24 = '12'
        if minute < 10:
            minute = '0' + str(minute)
        else:
            minute = str(minute)
        time = hour_24 + ':' + minute + 'AM'
        
    elif hour_24 >= 13 and hour_24 < 24:
        calc = hour_24 - 12
        calc = str(calc)
        if minute < 10:
            minute = '0' + str(minute)
        else:
                    minute = str(minute)
        time = calc + ':' + minute + 'PM'
    elif hour_24 < 12:
        if minute < 10:
                    minute = '0' + str(minute)
        else:
                    minute = str(minute)
        time = str(hour_24) + ':' + minute + 'AM'
        
    elif hour_24 == 12:
        if minute < 10:
                            minute = '0' + str(minute)
        else:
                            minute = str(minute)
        time = str(hour_24) + ':' + minute + 'PM'
        
    return time

# -----------------------------------------
# INPUT
# -----------------------------------------
# Read the required input values below.

hour_24 = int(input("Enter the value = "))
minute = int(input("Enter the value = "))
# -----------------------------------------
# CALL YOUR FUNCTION
# -----------------------------------------
# Call the function and print the returned value.

x = time_conversion(hour_24,minute)
print(x)

# -----------------------------------------
# TEST YOUR PROGRAM
# -----------------------------------------
# Test your program against the following testcases.
# +---------+--------+--------------+
# | hour_24 | minute | Output       |
# +---------+--------+--------------+
# | 13      | 5      | 1:05 PM      |
# | 12      | 61     | Invalid Time |
# | 0       | 23     | 12:23 AM     |
# | 12      | 0      | 12:00 PM     |
# | 23      | 59     | 11:59 PM     |
# | -1      | 30     | Invalid Time |
# | 24      | 0      | Invalid Time |
# | 0       | 0      | 12:00 AM     |
# | 25      | 32     | Invalid Time |
# | 18      | 7      | 6:07 PM      |
# | 9       | 45     | 9:45 AM      |
# +---------+--------+--------------+