# defines the variable add, which prints a string including the arguments passed in and returns the value of the equation
def add(a, b):
	print(f"ADDING {a} + {b}")
	return a + b

# defines the variable subtract, which prints a string including the arguments passed in and returns the value of the equation
def subtract(a, b):
	print(f"SUBTRACTING {a} - {b}")
	return a - b

# defines the variable multiply, which prints a string including the arguments passed in and returns the value of the equation
def multiply(a, b):
	print(f"MULTIPLYING {a} * {b}")
	return a * b

# defines the variable divide, which prints a string including the arguments passed in and returns the value of the equation
def divide(a, b):
	print(f"DIVIDING {a} / {b}")
	return a / b

# prints a string
print("Let's do some math with just functions!")

# establishes multiple variables and assigns them the value of the results of the different functions listed above
age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

# prints the value of each variable in a string
print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

# A puzzle for the extra credit, typie it in anyway
print("Here is a puzzle.")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
# what = -4391
print("That becomes: ", what, "Can you do it by hand?")