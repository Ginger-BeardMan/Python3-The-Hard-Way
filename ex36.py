# Weeklong Game Project

# 1. Tasks/Ideas:
	# Decide to quest
	# Decide location
	# Fight a lower boss
	# Travel to final location
	# Fight final boss
# 2. Pick the easiest thing:
	# Initiate interaction with user
	# Create functions in the order of appearance
# 3. Write comments on how to accomplish this task:
	# Prompt the user 'awake'
	# User ventures to make tea but a bang in the front yard prompts them to another location
	# The user meets a warlock
	# The quest is presented
	# The user chooses their path (one leads to a specific boss, the other to another boss)
	# The user chooses a different path
	# The user is presented with a puzzle (their answer reveals the final villan or leads to death)
	# The user confronts the final challenge, victory or death
# 4. Write code:

def adventure():
	print('You awake to a beautiful sunrise, another perfect morning.')
	print('As you venture to make a pot of tea, you hear what sounds like a crash outside the front of your home.')
	print('Do you choose to investigate or continue with your morning tea?')

	breakfast = input('> ')

	if breakfast == 'investigate':
		investigate()
	elif breakfast == 'morning tea':
		tea()
	else:
		print('I\'m not sure what you want to do, maybe go back to bed and start over')
		adventure()


def investigate():
	print('You walk outside to take a look.')
	print('Surprisingly, or maybe not surprisingly, you find a tall figure covered in soot and dirt.')
	print('He introduces himself and feels compelled to provide you the reason for his presence.')
	print('He stops to think, then says you seem like just the person to assist him as he continues. Do you accept or decline his invitation, not knowing much about the request?')

	invitation = input('> ')

	if invitation == 'accept':
		journey_begins()
	elif inviation == 'decline':
		clean_up()
	else:
		print('You walk away leaving the individual confused.')


def tea():
	print('You start the kettle and choose your tea')
	print('You have Earl Grey or Green, what to choose?')

	tea_flavor = input('> ')

	if tea_flavor == 'Earl Grey':
		print('A calm choice for a calm morning.')
		print('You enjoy your tea while the sun rises.')
		exit(0)
	elif tea_flavor == 'Green':
		print('A strong flavor to power you up for the day ahead.')
		print('A long day in the garden will do you good.')
		exit(0)
	else:
		print('I guess you changed your mind about tea.')
		print('Would you like to investigate the noise in your front yard after all?')

		changed_mind = input('> ')

		if changed_mind == 'yes':
			investigate()
		else:
			print('Okay, have a wonderful day then!')
			exit()
			

# 5. Run the script:

# 6. Test-Fix-Repeat:

# 7. Repeat steps 2-6 for another task
:
