# Creating a variable titled formatter with a string list
formatter = "{} {} {} {}"

# Display and format 'formatter' to be a list of numbers
print(formatter.format(1, 2, 3, 4))

# Display and format 'formatter' to be a list of numbers that are strings/words
print(formatter.format('one', 'two', 'three', 'four'))

# Display and format 'formatter' to be a list of boolean statements
print(formatter.format(True, False, False, True))

# Display and format 'formatter' to include the blank list 4 times
print(formatter.format(formatter, formatter, formatter, formatter))

# Display and format 'formatter' to include my own text (this does not print on seperate lines)
print(formatter.format(
	'I am',
	'Trying',
	'My best',
	'Here'
))
