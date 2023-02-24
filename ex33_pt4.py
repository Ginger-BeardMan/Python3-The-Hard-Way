# Adding an additional argument to the function to change the scale of number change. 

i = 0
j = 1
numbers = []

def loopy(i, j):
	if i < 80:
		print(f"At the stop i is {i}")
		numbers.append(i)

		i += j
		j += 3
		
		print("Numbers now: ", numbers)
		print(f"At the bottom i is {i}")

		return loopy(i, j)
	else:
		print("All done.")

loopy(i, j)

print("The numbers: ") 

for num in numbers: 
	print(num)