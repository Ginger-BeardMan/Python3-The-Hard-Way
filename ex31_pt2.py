print("""You enter a dark room with two doors.
	Do you go through door #1 or door #2?""")

door = input("> ")

if door == "1":
	print("There's a giant bear here eating a cheese cake.")
	print("What do you do?")
	print("1. Take the cake.")
	print("2. Scream at the bear.")

	bear = input("> ")

	if bear == "1":
		print("The bear eats your face off. Somehow you find the will to stand.")
		print("While the bear chews your face, you manage to escape to an adjacent room.")
		print("1. You pick up Mjolnir, Thor's hammer.")
		print("2. You choose matching ham hock and a meat helmet.")

		weapon = input("> ")

		if weapon == "1":
			print("You return and smite down the creature until the final breath leaves it's body.")
			print("The bear is dead, you pass out, only to awaken in a hospital.")
			print("Congratulations warrior!")
		else:
			print("Not much to explain here with a hungry bear.")
			print("Hello from the afterlife, you tried. Good job!")

	elif bear == "2":
		print("The bear eats your legs off. Good job!")
	else:
		print(f"Well, doing {bear} is probably better.")
		print("Bear runs away.")
 
elif door == "2":
	print("You stare into the endless abyss at Cthulu's retina.")
	print("1. Blueberries.")
	print("2. Yellow jacket clothespins.")
	print("3. Understanding revolvers yelling melodies.")

	insanity = input("> ")

	# Let's embrace insanity somehow
	if insanity == "1" or insanity == "2":
		print("Your body survives powered by a mind of jello.")
		print("Good job!")
	else:
		print("The insanity rots your eyes into a pool of muck.")
		print("Still, you have acended and your mind's eye sees more clearly then ever before.")
		print("1. You channel this new found power and step further in to the room.")
		print("2. You resist the power with all of your might.")

		darkness = input("> ")

		if darkness == "1":
			print("Cthulu welcomes you, granting you stronger abilities.")
			print("You are given followers of your own. Welcome visionary...")
		else:
			print("Your head explodes. Cthulu consumes your essence. Blueberries...")

# If the user didn't input any information or input something other than 1 or 2 the following string prints. 
else:
	print("You stumble around and fall on a knife and die. Good job!")