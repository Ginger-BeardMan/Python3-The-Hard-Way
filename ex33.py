i = 0 # Creating a variable, i, and assigning it an initial value
numbers = [] # Creating a variable, numbers, and assigning it an empty list

while i < 6: # States that as long as i has a value less than 6, the indented code nested under it will run
	print(f"At the top i is {i}") # Prints a formatted string while condition is still met
	numbers.append(i) # Takes the current value of i and adds it to the end of the list "numbers"

	i += 1 # Takes i and adds one every time the sequence of code runs

	print("Numbers now: ", numbers) # Prints a string
	print(f"At the bottom i is {i}") # Prints a formatted string


print("The numbers: ") # Prints a string

for num in numbers: # For every number in the numbers list print the number until there are no numbers left in the list
	print(num)