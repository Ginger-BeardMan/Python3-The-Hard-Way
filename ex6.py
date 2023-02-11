# Creating a variable and assigning it a integer
types_of_people = 10

# Creating a variable and assigning it a string that includes an f string and another variable inside {}
x = f"There are {types_of_people} types of people."

# Creating a variable and assigning it a string
binary = 'binary'

# Creating a variable and assigning it a string
do_not = "don't"

# Creating a variable and assigning it a string that is an f string that includes 2 other variables in separate {}
y = f"Those who know {binary} and those who {do_not}."

# Calling and displaying the variable x
print(x)

# Calling and displaying the variable y
print(y)

# Calling and displaying a f string with the variable x within it
print(f"I said: {x}")

# Calling and displaying a f string with the variable y within it
print(f"I also said: '{y}'")

# Creating a variable and stating it is false
hilarious = False

# Creating a variable and assigning it a string
joke_evaluation = "Isn't that joke so funny?! {}"

# Calling and displaying the variable joke_evalutation while formatting it to the rules of the hilarious variable
print(joke_evaluation.format(hilarious))

# Creating a variable w and assiging it a string
w = "This is the left side of..."

# Creating a variable e and assigning it a string
e = "a string with a right side."

# Calling and displaying the variables w and e and combining them in to one string using the + command 
print(w + e)