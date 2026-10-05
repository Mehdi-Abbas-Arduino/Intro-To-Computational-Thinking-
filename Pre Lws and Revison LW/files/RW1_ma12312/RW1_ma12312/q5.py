# -----------------------------------------
# DEFINE THE REQUIRED FUNCTION
# -----------------------------------------
# Write your function definition below.
def daily_buffet_cost(age,breakfast_choice,lunch_choice,dinner_choice):
    breakfast = 0 
    lunch = 0
    dinner = 0
    total = 0
    if age >= 13 :
        if breakfast_choice == 'y' or breakfast_choice == 'Y':
            breakfast = 800 
            total += breakfast
        if lunch_choice == 'y' or lunch_choice == 'Y':
                lunch = 1200
                total += lunch
        if dinner_choice == 'y' or dinner_choice == 'Y':
                dinner = 1500
                total += dinner
        
        return f"Adult charges for the day will be: Rs. {total}"
    elif age >= 6 and age <=12:
        if breakfast_choice == 'y' or breakfast_choice == 'Y':
                breakfast = 400 
                total += breakfast
        if lunch_choice == 'y' or lunch_choice == 'Y':
                lunch = 700
                total += lunch
        if dinner_choice == 'y' or dinner_choice == 'Y':
                dinner = 800
                total += dinner

        return f"Child charges for the day will be: Rs. {total}"
    elif age <= 5 :
        if breakfast_choice == 'y' or breakfast_choice == 'Y':
                breakfast = 0 
                total += breakfast
        if lunch_choice == 'y' or lunch_choice == 'Y':
                lunch = 0
                total += lunch
        if dinner_choice == 'y' or dinner_choice == 'Y':
                dinner = 300
                total += dinner

        return f"Toddler charges for the day will be: Rs. {total}"

    

        


# -----------------------------------------
# INPUT
# -----------------------------------------
# Read the required input values below.

age = int(input("Enter age = "))
breakfast_choice = input("Enter = ")
lunch_choice = input("Enter = ")
dinner_choice = input("Enter = ")


# -----------------------------------------
# CALL YOUR FUNCTION
# -----------------------------------------
# Call the function. The function itself prints the required output.
x = daily_buffet_cost(age,breakfast_choice,lunch_choice,dinner_choice)
print(x)


# -----------------------------------------
# TEST YOUR PROGRAM
# -----------------------------------------
# Test your program against the following testcases.
# +-----+------------------+--------------+---------------+----------------------------------------------+
# | age | breakfast_choice | lunch_choice | dinner_choice | Output                                       |
# +-----+------------------+--------------+---------------+----------------------------------------------+
# | 28  | Y                | y            | N             | Adult charges for the day will be: Rs. 2000  |
# | 10  | y                | n            | N             | Child charges for the day will be: Rs. 400   |
# | 5   | y                | y            | y             | Toddler charges for the day will be: Rs. 300 |
# | 35  | Y                | N            | Y             | Adult charges for the day will be: Rs. 2300  |
# | 5   | y                | y            | N             | Toddler charges for the day will be: Rs. 0   |
# | 12  | n                | N            | Y             | Child charges for the day will be: Rs. 800   |
# +-----+------------------+--------------+---------------+----------------------------------------------+