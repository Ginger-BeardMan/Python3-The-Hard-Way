print("""You enter a dark room with two doors.
	Do you go through door #1 or door #2?""") # Prints a multi-line string.

door = input("> ") # Prompts the user to input information

# If door == "1" is true, print the following four strings followed by another opportunity for user imput.
if door == "1":
	print("There's a giant bear here eating a cheese cake.")
	print("What do you do?")
	print("1. Take the cake.")
	print("2. Scream at the bear.")

	bear = input("> ") # Prompts the user to input information.

	# Multiple boolean scenarios that print specific strings if true. If none are true, then the string following else condition prints.
	if bear == "1":
		print("The bear eats your face off. Good job!")
	elif bear == "2":
		print("The bear eats your legs off. Good job!")
	else:
		print(f"Well, doing {bear} is probably better.")
		print("Bear runs away.")

# If the user input 2, the following four strings print. 
elif door == "2":
	print("You stare into the endless abyss at Cthulu's retina.")
	print("1. Blueberries.")
	print("2. Yellow jacket clothespins.")
	print("3. Understanding revolvers yelling melodies.")

	# Prompts the user to input information.
	insanity = input("> ")

	# If the user inputs 1 or 2, the following prints, otherwise the else string prints.
	if insanity == "1" or insanity == "2":
		print("Your body survives powered by a mind of jello.")
		print("Good job!")
	else:
		print("The insanity rots your eyes into a pool of muck.")
		print("Good job!")

# If the user didn't input any information or input something other than 1 or 2 the following string prints. 
else:
	print("You stumble around and fall on a knife and die. Good job!")