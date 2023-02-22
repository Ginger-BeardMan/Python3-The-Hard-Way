people = 30
cars = 40
trucks = 15

if cars > people: # If the value of cars is greater than the value of people, print the following string. 
	print("We should take the cars")
elif cars < people: # If the value of cars is less than the value of people, print the following string.
	print("We should not take the cars.")
else: # If neither boolean is true, print the following string.
	print("We can't decide.")

if trucks > cars: # If the value of trucks is greater than the value of cars, print the following string. 
	print("That's too many trucks.")
elif trucks < cars: # If the value of trucks is less than the value of cars, print the following string. 
	print("Maybe we could take the trucks.")
else: # If neither is true, print the following string. 
	print("We still can't decide.")

if people > trucks: # If the value of people is greater than the value of trucks, print the following string. 
	print("Alright, let's just take the trucks.")
else: # If that is not true, print the following string. 
	print("Fine, let's stay home then.")