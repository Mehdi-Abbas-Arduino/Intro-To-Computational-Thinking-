# -----------------------------------------
# DEFINE THE REQUIRED FUNCTION(S)
# -----------------------------------------
# Write your function definition(s) below.
def temp_converter (temperature,target_scale):
    celsius = round((((temperature-32) * 5) / 9),2)
    farenheit = round(((temperature * (9/5)) + 32),2)

    if target_scale == 'C':
        return(f"{celsius} deegres Celsius is the temperature for Fatima ")

    elif target_scale == 'F':
        return(f"{farenheit} deegres Celsius is the temperature for Sana ")


# -----------------------------------------
# INPUT
# -----------------------------------------
# Read the required input values below.
temperature = int(input("Enter = "))
target_value = input("Enter = ")


# -----------------------------------------
# CALL YOUR FUNCTION
# -----------------------------------------
# Call the function. The function itself prints the required output.

x = temp_converter(temperature,target_value)
print(x)

# -----------------------------------------
# TEST YOUR PROGRAM
# -----------------------------------------
# Test your program against the following testcases.
# +-------------+--------------+------------------------------------------------------+
# | temperature | target_scale | Output                                               |
# +-------------+--------------+------------------------------------------------------+
# | 95          | C            | 35.0 degrees Celsius is the temperature for Fatima.  |
# | 30          | F            | 86.0 degrees Fahrenheit is the temperature for Sana. |
# | 68          | C            | 20.0 degrees Celsius is the temperature for Fatima. |
# | 22          | F            | 71.6 degrees Fahrenheit is the temperature for Sana.|
# | 86          | C            | 30.0 degrees Celsius is the temperature for Fatima. |
# +-------------+--------------+------------------------------------------------------+