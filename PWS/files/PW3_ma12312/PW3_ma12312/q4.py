# -----------------------------------------
# DEFINE THE REQUIRED FUNCTION
# -----------------------------------------
# Write your function definition below.
def daily_buffet_cost(age,breakfast_choice,lunch_choice,dinner_choice):
    total = 0
    if age >= 13 :
        breakfast = 800
        Lunch = 1200
        Dinner = 1500
        if breakfast_choice == 'y' or breakfast_choice == 'Y':
            total += breakfast
        
        if lunch_choice == 'y' or lunch_choice == 'Y':
            total += Lunch
            
        if dinner_choice == 'y' or dinner_choice == 'Y':
            total += Dinner
        return "Adult charges for the day will be: ",total
    elif age >= 6 and age <=12:
        breakfast = 400
        Lunch = 700
        Dinner = 800
        if breakfast_choice == 'y' or breakfast_choice == 'Y':
                    total += breakfast
                
        if lunch_choice == 'y' or lunch_choice == 'Y':
                    total += Lunch
                    
        if dinner_choice == 'y' or dinner_choice == 'Y':
                    total += Dinner
        return "Child charges for the day will be: ",total 
    elif age <= 5:
        breakfast = 0
        Lunch = 0
        Dinner = 300
        if breakfast_choice == 'y' or breakfast_choice == 'Y':
                    total += breakfast
                
        if lunch_choice == 'y' or lunch_choice == 'Y':
                    total += Lunch
                    
        if dinner_choice == 'y' or dinner_choice == 'Y':
                    total += Dinner
        return "Toddler charges for the day will be: ",total       
            
        
# -----------------------------------------
# INPUT
# -----------------------------------------
# Read the required input values below.
age,breakfast_choice,lunch_choice,dinner_choice = input("Enter values : ").split()
age = int(age)
breakfast_choice = str(breakfast_choice)
lunch_choice = str(lunch_choice)
dinner_choice = str(dinner_choice)


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