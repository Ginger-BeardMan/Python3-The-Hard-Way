# Changing the while loop to a function using an if-else condition.

i = 0
numbers = []

def loopy(i):
	if i < 6:
		print(f"At the stop i is {i}")
		numbers.append(i)

		i += 1

		print("Numbers now: ", numbers)
		print(f"At the bottom i is {i}")

		return loopy(i)
	else:
		print("All done.")

loopy(i)

print("The numbers: ") 

for num in numbers: 
	print(num)