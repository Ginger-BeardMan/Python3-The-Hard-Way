from sys import exit # From the system, import the exit module

def gold_room(): # Creates a function that runs the indented code if called. This function is utilized by the bear_room function.
	print("This room is full of gold. How much do you take?") # Prints a string

	choice = input("> ") # Prompts the user to input information

	if "0" in choice or "1" in choice: # If the user includes a 0 OR a 1 in their response (the variable 'choice') then their response is assigned to the variable how_much. 
		how_much = int(choice)
	else: # If the user inputs anything without a 0 or 1 in it then the dead() function is called. 
		dead("Man, learn to type a number.")

	if how_much < 50: # If how_much is less than 50, the following string prints and the user exits the program
		print("Nice, you're not greedy, you win!")
		exit(0) 
	else: # If how_much is anything 50 or greater then the following string prints
		dead("You greedy bastard!")


def bear_room(): # Creates a function that runs the indented code if called
	print("There is a bear here.") # Prints a string
	print("The bear has a bunch of honey.") # Prints a string
	print("The fat bear is in front of another door.") # Prints a string
	print("How are you going to move the bear?") # Prints a string
	bear_moved = False # bear_moved is assigned False when this function is initially called

	while True: # While the bear_room function is True the following code runs
		choice = input("> ") # Prompts the user to input a response

		if choice == "take honey": # If the user inputs 'take honey' the dead() function is called
			dead("The bear looks at you then slaps your face off.")
		elif choice == "taunt bear" and not bear_moved: # If the user inputs 'taunt bear' while bear_moved is still False then two strings print and bear_moved is now True
			print("The bear has moved from the door.")
			print("You can go through it now.")
			bear_moved = True
		elif choice == "taunt bear" and bear_moved: # If the user inputs 'taunt bear' after the bear_moved function has been changed to True, the dead() function is called
			dead("The bear gets pissed off and chews your leg off.")
		elif choice == "open door" and bear_moved: # If the user inputs 'open door' after the bear_moved function has been changed to True, the gold_room() function is called
			gold_room()
		else: # If the user inputs anything else, this string is printed
			print("I got no idea what that means.")


def cthulu_room(): # Creates a function that runs the indented code if called
	print("Here you see the great evil Cthulu.") # Prints a string
	print("He, it, whatever stares at you and you go insane.") # Prints a string
	print("Do you flee for your life or eat your head?") # Prints a string

	choice = input("> ") # Prompts the user to input information which is assigned to this variable (only within this function)

	if "flee" in choice: # If the user input a response that includes the string 'flee' then the start() function is called
		start()
	elif "head" in choice: # If the user input a response that includes the string 'head' then the dead() function is called
		dead("Well that was tasty!")
	else: # If any other response is given, the function is called again and cthulu_room starts over
		cthulu_room() # Calls the function again, forcing the user to input a correct response


def dead(why): # Creates a function 'dead' that passes in an argument
	print(why, "Good Job!") # Prints a string. 'Why' is an argument that is passed in to this function and takes the form as a string in this script of code. 
	exit(0) # Exits the program

def start(): # Creates a function 'start'. This begins the code and branches to other functions.
	print("You are in a dark room.") # Prints a string
	print("There is a door to your right and left.") # Prints a string
	print("Which one do you take?") # Prints a string

	choice = input("> ") # Prompts a user to input information which is then assigned to the variable choice (only within this function)

	if choice == "left": # If the user input 'left' then the bear_room() function is called
		bear_room()
	elif choice == "right": # If the user input 'left' then the cthulu_room() function is called
		cthulu_room()
	else: # If anything other than 'lef' or 'right' is input then the following string prints
		dead("You stumble around the room until you starve.")


start() # Calls the start() function