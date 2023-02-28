# Weeklong Game Project

# 1. Tasks/Ideas:
	# Decide to quest
	# Gather things
	# Begin quest
# 2. Pick the easiest thing:
	# Initiate interaction with user
	# Create functions in the order of appearance
# 3. Write comments on how to accomplish this task:
	# Prompt the user 'awake'
	# User ventures to make tea but a bang in the front yard prompts them to another location
	# The user meets a warlock
	# The quest is presented
	# The user chooses their path

# 4. Write code:

from sys import exit

def adventure():
	print('You awake to a beautiful sunrise, another perfect morning.')
	print('As you venture to make a pot of tea, you hear what sounds like a crash outside the front of your home.')
	print('Do you choose to investigate or continue with your morning tea?')

	breakfast = input('> ')

	if breakfast.lower() == 'investigate':
		investigate()
	elif breakfast.lower() == 'morning tea':
		tea()
	else:
		print('I\'m not sure what you want to do, maybe go back to bed and start over')
		adventure()


def investigate():
	print('You walk outside to take a look.')
	print('Surprisingly, or maybe not surprisingly, you find a tall figure covered in soot and dirt.')
	print('He labels himself a weary traveler and feels compelled to provide you the reason for his presence.')
	print('He stops to think, then says you seem like just the person to assist him as he continues. Do you accept or decline his invitation, not knowing much about the request?')

	invitation = input('> ')

	if invitation.lower() == 'accept':
		journey_begins()
	elif inviation.lower() == 'decline':
		clean_up()
	else:
		print('You walk away leaving the individual confused.')
		print('You walk to the garden to find peace and carry out your day.')
		exit(0)


def tea():
	print('You start the kettle and choose your tea')
	print('You have Earl Grey or Green, what to choose?')

	tea_flavor = input('> ')

	if tea_flavor.lower() == 'earl grey':
		print('A calm choice for a calm morning.')
		print('You enjoy your tea while the sun rises.')
		exit(0)
	elif tea_flavor.lower() == 'green':
		print('A strong flavor to power you up for the day ahead.')
		print('A long day in the garden will do you good.')
		exit(0)
	else:
		print('I guess you changed your mind about tea.')
		print('Would you like to investigate the noise in your front yard after all?')

		changed_mind = input('> ')

		if changed_mind.lower() == 'yes':
			investigate()
		elif changed_mind.lower() == 'no':
			print('Okay, have a wonderful day then!')
			exit(0)
		else:
			print('Hmm, how about yes or no?')

def journey_begins():
	print('The man tells you of his quest and where he has been.')
	print("'The journey will be challenging, with potential battles ahead, but you seem like the type to take pleasure in challenges'")

	challenges = input('Do you? ')

	if challenges.lower() == 'yes':
		print("'Yes, I suppose I do.' You find yourself saying.")
		print("The tall man states 'You won't need much, some clothes, a walking stick, and food to last a couple days. Why don't you gather your things and meet me back here'")
		gather_belongings()
	elif challenges.lower() == 'no':
		print("'Well, we can find a use for even those that don't find themselves adventurous' He says.")
		print("'Gather your things anyway and meet me back here. Don't forget to lock up!")
		gather_belongings()
	else:
		print("'We'll see in time, my new friend' He says.")
		print("'Gather your things anyway and meet me back here. Don't forget to lock up!")
		gather_belongings()

def clean_up():
	print("'Although I won't be joining you, please let me help you gather up your things' You say.")
	print("You find all sorts of odd nick-nacks in his belongings. Fireworks, crystals, coin, animal bones, and worn pages of old books.")
	print("You mention that he might find some help at the local inn.")
	print("The cleaning is finished, you offer some food and directions before he get's to his journey again.")
	print("What an interesting fellow, you say to yourself.")
	print("You head back inside to make tea.")
	tea()

def gather_belongings():
	print("You walk back in to your house to gather your things.")
	print("Do you gather food first or clothes?")

	belongings = input('> ')

	if belongings.lower() == 'food':
		print('You walk to the pantry, gather bread, cheese, and fruit.')
		print('You also back a waterskin, pipe weed, and ale.')
		print('You then walk to your room to gather clothing.')
		leaving_home()
	elif belongings.lower() == 'clothes':
		print('You walk to your room to gather a few articles of clothing.')
		print('Not knowing the weather, you gather a couple warm outfits and a couple cool outfits')
		print('You then return to the kitchen to grab some foods')
		leaving_home()
	else:
		print('Figure out what you want to do already!')
		gather_belongings()

def leaving_home():
	print('You return to your new aquaintence and let him know you are ready to go.')
	print("'Glad to hear it my friend. Before we go, may I formally introduce myself as Uhnlan, the Warlock. What shall I call you my friend?'")
	name = input('> ')
	print(f"'Thank you {name}, I am forever grateful that you are joining me on my journey'")
	print("'We shall head north west, stop at the inn across the river for sustanance and rest. May we hope for a wonderful adventure with little hardship, however, let us take any challenge head on!'")
	print('Your journey begins... who knows when you will return...')

adventure()

# 5. Run the script:

# Done, fixed uppercase v. lowercase (potential) issue.
# Script runs without errors.

# 6. Test-Fix-Repeat:

# Script works after adding .lower() to input() variables

# 7. Repeat steps 2-6 for another task