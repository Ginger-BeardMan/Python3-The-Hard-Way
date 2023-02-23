the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# This first kind of for-loop goes through a list
for number in the_count:
	print(f"This is count {number}")

# Same as above
for fruits in fruits:
	print(f"A fruit of type: {fruits}")

# Also we can go through mixed lists too
for i in change:
	print(f"I got {i}")

# elements = []

#for i in range(0, 6):
#	print(f"Adding {i} to the list.")
#	elements.append(i)

# Now we can print them out too

# Making the code cleaner:

elements = [*range(6)] # Creating a list that unpacks a range between 0 - 6 instead of using a for loop

for i in elements:
	print(f"Element was: {i}")