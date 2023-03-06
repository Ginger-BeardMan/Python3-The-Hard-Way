# mystuff as a dictionary
mystuff = {'apple': 'I AM APPLES!'}
# Get apple from dict
print(mystuff['apple']) # Get x from y

# mystuff as a module: 

def apple():
	print("I AM APPLES!")

tangerine = "Living reflection of a dream"

import mystuff
mystuff.apple() # get apple from module
print(mystuff.tangerine) # get tangerine from module

# mystuff as a class:

class MyStuff(object):

	def __init__(self):
		self.tangerine = "And now a thousand years between"

	def apple(self):
		print("I AM CLASSY APPLES!")

# instantiating (creating) a class (this is done after creating the class MyStuff)

thing = MyStuff()
thing.apple()
print(thing.tangerine)