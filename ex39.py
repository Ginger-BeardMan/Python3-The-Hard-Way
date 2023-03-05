# Create a mapping of state to abbreviation
states = {
	'Oregon': 'OR',
	'Florida': 'FL',
	'California': 'CA',
	'New York': 'NY',
	'Michigan': 'MI',
	'New Hampshire': 'NH', # Added in for study drill
	'Maine': 'ME' # Added in for study drill
}

# Create a basic set of states and some cities in them
cities = {
	'CA': 'San Francisco',
	'MI': 'Detroit',
	'FL': 'Jacksonville'
}

# Add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'
cities['NH'] = 'Concord' # Added in for study drill
cities['ME'] = 'Portland' # Added in for study drill

# Print out some cities
print('-' * 10)
print('NY State has: ', cities['NY'])
print('OR State has: ', cities['OR'])

# Print some states
print('-' * 10)
print('Michigan\'s abbreviation is: ', states['Michigan'])
print('Florida\'s abbreviation is: ', states['Florida'])

# Do it by using the state then cities dict
print('-' * 10)
print('Michigan has: ', cities[states['Michigan']])
print('Florida has: ', cities[states['Florida']])

# Print every state abbreviation
print('-' * 10)
for state, abbrev in list(states.items()):
	print(f'{state} is abbreviated {abbrev}')

# Print every city in state
print('-' * 10)
for abbrev, city in list(cities.items()):
	print(f'{abbrev} has the city {city}')

# Now do both at the same time
print('-' * 10)
for state, abbrev in list(states.items()):
	print(f'{state} state is abbreviated {abbrev}')
	print(f'and has city {cities[abbrev]}')

print('-')
# Safely get an abbreviation by state that might not be there
state = states.get('Texas')

if not state:
	print('Sorry, no Texas')

# Get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print(f'The city for the state of \'TX\' is: {city}')


# STUDY DRILLS:

print('How many items are in cities dictionary?')
print(len(cities))
print('How many items are in states dictionary?')
print(len(states))
type(cities)
type(states)

print('We\'ll make a new dictionary called this_guy')
this_guy = dict(name = 'Fen', age = '33', country = 'United States')
print(this_guy)

print('Now we\'ll add some additional information to this dictionary with the .update() function')
favorites = dict(fav_food = 'Pizza', fav_drink = 'Beer', fav_instrument = 'Drums')
this_guy.update(favorites)
print(this_guy)
print('What are the keys in this_guy?')
print(this_guy.keys())
print('What are the values in this_guy?')
print(this_guy.values())
print('What are the items in this_guy?')
print(this_guy.items())