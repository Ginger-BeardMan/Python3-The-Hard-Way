# Changing the increment change of i within the function.

i = 100
numbers = []

def loopy(i):
	if i < 250:
		print(f"At the stop i is {i}")
		numbers.append(i)

		i += 10

		print("Numbers now: ", numbers)
		print(f"At the bottom i is {i}")

		return loopy(i)
	else:
		print("All done.")

loopy(i)

print("The numbers: ") 

for num in numbers: 
	print(num)