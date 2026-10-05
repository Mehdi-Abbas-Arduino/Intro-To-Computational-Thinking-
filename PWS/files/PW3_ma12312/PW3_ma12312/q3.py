# -----------------------------------------
# DEFINE THE REQUIRED FUNCTION
# -----------------------------------------
# Write your function definition below.
def ride_choice(trip_distance_km,petrol_price, diesel_price,petrol_km_per_litre,diesel_km_per_litre):
    
    cost_petrol = (trip_distance_km * petrol_price) //  petrol_km_per_litre
    cost_diesel = (trip_distance_km * diesel_price) // diesel_km_per_litre
    
    if cost_diesel < cost_petrol :
        return "Diesel"
    elif cost_diesel > cost_petrol:
        return "Petrol"
    elif cost_diesel == cost_petrol:
        return "Any"

# -----------------------------------------
# INPUT
# -----------------------------------------
# Read the required input values below.

trip_distance_km,petrol_price, diesel_price,petrol_km_per_litre,diesel_km_per_litre = input("Enter values = ").split()
trip_distance_km = int(trip_distance_km)
petrol_price = int(petrol_price)
diesel_price =  int(diesel_price)
petrol_km_per_litre = int(petrol_km_per_litre)
diesel_km_per_litre = int(diesel_km_per_litre)


# -----------------------------------------
# CALL YOUR FUNCTION
# -----------------------------------------
# Call the function and print the returned value.

x = ride_choice(trip_distance_km,petrol_price, diesel_price,petrol_km_per_litre,diesel_km_per_litre)
print(x)

# -----------------------------------------
# TEST YOUR PROGRAM
# -----------------------------------------
# Test your program against the following testcases.
# +------------------+--------------+--------------+---------------------+---------------------+--------+
# | trip_distance_km | petrol_price | diesel_price | petrol_km_per_litre | diesel_km_per_litre | Output |
# +------------------+--------------+--------------+---------------------+---------------------+--------+
# | 120              | 290          | 280          | 12                  | 16                  | Diesel |
# | 150              | 285          | 300          | 15                  | 12                  | Petrol |
# | 100              | 300          | 240          | 10                  | 8                   | Any    |
# | 180              | 290          | 290          | 12                  | 18                  | Diesel |
# | 160              | 280          | 310          | 16                  | 10                  | Petrol |
# | 210              | 300          | 270          | 15                  | 14                  | Diesel |
# | 180              | 300          | 240          | 15                  | 12                  | Any    |
# +------------------+--------------+--------------+---------------------+---------------------+--------+