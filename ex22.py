# Exercise 22 is to review all previous exercises, typing out all characters used, and describing their purpose/function

# ex1
# Each of these lines is a command to print a string.

print('Hello World!')
print('Hello Again')
print('I like typing this.')
print('This is fun.')
print('Yay! Printing.')
print("I'd much rather you 'not'.")
print('I "said" do not touch this.')

# ex2
# These are comments using the # symbol and there are additional print commands for strings.

# A comment, this is so you can read your program later.
# Anything after the # is ignored by pythong.

print('I could have code like this.') # and the comment after is ignored

# You can also use a comment to 'disable' or comment out code:
# print("This won't run")

print('This will run.')

# ex3
# Each of these lines is a command to print. Those with only quotes print strings only, those with quotes
# and equations print a string with the answer to the equation. Lastly, there are print commands for evaluating
# whether a number is greater than, greater than or equal to, or less than or equal to another number.

print("I will now count my chickens:")

print("Hens", 25 + 30/6)
print("Roosters", 100 - 25 * 3 % 4)

print("Now I will count the eggs:")

print(3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)

print("Is it true that 3 + 2 < 5-7?")

print(3 + 2 < 5 -7)

print('What is 3 + 2?', 3 + 2)
print('What is 5 - 7?', 5 - 7)

print("Oh, that's why it's false.")

print("How about some more.")

print("Is it greater?", 5 > -2)
print("Is it greater or equal?", 5 >= -2)
print("Is it less or equal?", 5 <= -2)

# ex4

cars = 100 # Creates the variable cars and assigns 100 to it
space_in_a_car = 4.0 # Creates the variable space_in_a_car and assigns 4.0 to it, a floating number
drivers = 30 # Creates the variable drivers and assigns 30 to it. 
passengers = 90 # Creates the variable passengers and assigns 90 to it. 
cars_not_driven = cars - drivers # Creates the variable cars_not_driven and assigns the difference between the cars variable and the drivers variable to it. 
cars_driven = drivers # Creates the variable cars_driven and assigns the variable drivers to it. 
carpool_capacity = cars_driven * space_in_a_car # Creates the variable carpool_capacity and assigns cars_driven to it. 
average_passengers_per_car = passengers/cars_not_driven # Creates the variable average_passengers_per_car and assigns passengers divided by cars_not_driven to it. 

print("There are", cars, "cars available.") # Prints a string using the value of the cars variable within the string. Leaving it out of quotes will use the value of the variable instead of quoting the literal name of the variable. 
print("There are only", drivers, "drivers available.") # Prints a string using the value of the drivers variable within the string.
print("There will be", cars_not_driven, "empty cars today.") # Prints a string using the value of the cars_not_driven variable within the string.
print("We can transport", carpool_capacity, "people today.") # Prints a string using the value of the carpool_capacity variable within the string.
print("We have", passengers, "to carpool today.") # Prints a string using the value of the passengers variable within the string. 
print("We need to put about", average_passengers_per_car, "in each car.") # Prints a string using the value of the average_passengers_per_car within the string.

# ex5

my_name = "Zed A. Shaw" # Establishes the variable my_name and assigns it a string
my_age = 35 # not a lie # Establishes the variable my_age and assigns it a number
my_height = 74 # inches # Establishes the variable my_height and assigns it a number
my_weight = 180 # lbs # Establishes the variable my_weight and assigns it a number
my_eyes = "Blue" # Establishes the variable my_eyes and assigns it a string
my_teeth = 'White' # Establishes the variable my_teeth and assigns it a string
my_hair = 'Brown' # Establishes the variable my_hair and assigns it a string

print(f"Let's talk about {my_name}") # Prints a string, utilising the f (format) character in order to insert the variable my_name within the string instead of seperated outside the quotes
print(f"He's {my_height} inches tall") # Prints a string, also utilizing 'format' to embed my_height 
print(f"He's {my_weight} pounds heavy.") # Prints a string, also utilizing 'format' to embed my_weight
print("Actually that's not too heavy") # Prints a string
print(f"He's got {my_eyes} eyes and {my_hair} hair.") # Prints a string utilizing 'format' to embed both my_eyes and my_hair within the string quotes
print(f"His teeth are usually {my_teeth} depending on the coffee.") # Prints a string utilizing 'format' to embed my_teeth within the string quotes

# this line is tricky, try to get it exactly right
total = my_age + my_height + my_weight # Creates a variable 'total' and assigns the combined numbers of my_age, my_height, and my_weight
print(f"If I add {my_age}, {my_height}, and {my_weight} I get {total}.") # Prints a string utilizing 'format' to embed my_age, my_height, my_weight, and total within the string quotes. 