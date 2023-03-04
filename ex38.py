ten_things = "Apples Oranges Crows Telephone Light Sugar" # Variable with a string attached to it

print("Wait there are not 10 things in that list. Let's fix that.") # Prints a string

stuff = ten_things.split(' ') # Creates a variable 'stuff' and assigns it ten_things as a list of items 'split up' in to single words with ' ' around them. What we see: ten_things.split(' '), what python sees: split(' ', ten_things)
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"] # Creates a list titled more_stuff

while len(stuff) != 10: # Creates a while loop that runs until the length (len) of stuff is 10
	next_one = more_stuff.pop() # Creates a variable and assigns it the last item in the list more_stuff by using .pop(). What we see: more_stuff.pop(), what python sees: pop(more_stuff)
	print('Adding: ', next_one) # Prints a string that includes the 'popped' item from the list
	stuff.append(next_one) # Adds the newly 'popped' item from more_stuff to the list 'stuff'. What we see: stuff.append(next_one), what python sees: append(next_one, stuff)
	print(f"There are {len(stuff)} items now.") # Prints a formatted string that updates the length of the list 'stuff'. 

print('There we go: ', stuff) # Prints a string that includes the fully updated list 'stuff'

print("Let's do some things with stuff.") # Prints a string

print(stuff[1]) # Prints the item at the second location in the list 'stuff'
print(stuff[-1]) # Prints the item at the last location in the list 'stuff'
print(stuff.pop()) # Prints the last item of the list 'stuff' and removes it from the list
print(' '.join(stuff)) # Takes all items from the list and joins them together in one string with a space in between each word
print('#'.join(stuff[3:5])) # Takes items at the 4 and 6 locations of the list and joins them together in a string with a # in between them instead of a space