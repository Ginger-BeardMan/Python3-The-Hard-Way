noun1 = input('First noun:')
verb = input('Verb:')
adjective = input('Adjective:')
noun2 = input('Second noun:')
noun3 = input('Third noun:')

# creates function
def mad_libs(noun1, verb, adjective, noun2, noun3):
	print(f"You are a johnny {noun1} who likes to {verb}")
	print(f"I have to let out a {adjective} laugh when I see you.")
	print(f"{noun2} would flick their {noun3} at you.")
	print("Have a wonderful day!")

mad_libs(noun1, verb, adjective, noun2, noun3)