# Creating the variable cars and assigning it a value
cars = 100

# Creating the variable of the space in the car and assigning it a value
space_in_a_car = 4

# Creating the variable drivers and assigning it a value
drivers = 30

# Creating the variable passengers and assigning it a value
passengers = 90

# Creating the variable cars_not_driven and assigning it an equation to determine the value
cars_not_driven = cars - drivers

# Creating the variable cars_driven and assigning it a value
cars_driven = drivers

# Creating the variable carpool_capacity and assigning it an equation to determine the value
carpool_capacity = cars_driven * space_in_a_car

# Creating a variable average_passengers_per_car and assigning it an equation to determine the value
average_passengers_per_car = passengers/cars_not_driven


# Printing a statement for cars
print('There are ', cars, ' cars available.')

# Printing a statement for how many drivers are available using the drivers variable
print('There are only ', drivers, ' drivers available.')

# Printing a statement for how many empty cars there will be using the cars_not_driven variable
print('There will be ', cars_not_driven, ' empty cars today.')

# Printing a statement for how many people can carpool today using the carpool_capacity variable
print('We can transport ', carpool_capacity, ' people today.')

# Printing a statement for how many passengers need to carpool using the passengers variable
print('We have ', passengers, ' to carpool today.')

# Printing a statement for how many passengers need to ride in each car to accomodate all passengers using the average_passengers_per_car variable
print('We need to put about ', average_passengers_per_car, ' in each car.')