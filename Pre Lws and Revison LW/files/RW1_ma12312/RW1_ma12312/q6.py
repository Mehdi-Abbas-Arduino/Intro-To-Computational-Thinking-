# -----------------------------------------
# DEFINE THE REQUIRED FUNCTION
# -----------------------------------------
# Write your function definition below.

def time_conversion(hour_24,minute):
    if (hour_24 >= 24 or hour_24 < 0)or (minute > 59 or minute < 0):
        return "Invalid time"
    time = 0
    minutes = 0
    if hour_24 > 12 and hour_24 <= 23:
        time = hour_24 - 12 
        if minute <= 9:
            minutes = "0" + str(minute)
        else:
            minutes = minute 
        return f'{time} : {minutes} PM'
    elif hour_24 == 0:
        time = 12
        if minute <= 9:
            minutes = "0" + str(minute)
        else:
            minutes = minute
        return f'{time} : {minutes} AM'
    elif hour_24 == 12:
        if minute <= 9:
            minutes = "0" + str(minute)
        else:
            minutes = minute
        return f'{hour_24} : {minutes} PM'
    elif hour_24>0 and hour_24 < 12 :
        if minute <= 9:
            minutes = "0" + str(minute)
        else:
            minutes = minute
        # print(minutes)
        return f'{hour_24} : {minutes} AM'



# -----------------------------------------
# INPUT
# -----------------------------------------
# Read the required input values below.
hour_24 = int(input("Enter = "))
minute = int(input("Enter value = "))


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