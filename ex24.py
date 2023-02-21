print("Let's practice everything.") # Prints a string
print('You\'d need to know \'bout escapes with \\ that do:') # Prints a string. \ is used when you want to include a ' within the string quote or \\ is used when including a \ in the string quote
print('\n newlines and \t tabs.') # Prints a string. \n is new line, \t is a tab

# Creates a variable and assigns it a multi line string. \t is a tab indent, \n is a new line.
poem = """
\tThat lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none
"""

print("--------------") # Prints a string
print(poem) # Prints the variable poem
print("--------------") # Prints a string


five = 10 - 2 + 3 - 6 # Creates a variable and assigns it a mathematic equation
print(f"This should be five: {five}") # Prints a formatted string that includes the variable 'five'

# Creates a function that passes in an argument
def secret_formula(started):
	jelly_beans = started * 500 # Creates a variable within the function and assigns it the argument times 500
	jars = jelly_beans / 1000 # Creates a variable within the function and assigns a value
	crates = jars / 100 # Creates a variable within the function and assigns a value
	return jelly_beans, jars, crates # Returns the value of all three variables


start_point = 10000 # Creates a variable and assigns it a value
beans, jars, crates = secret_formula(start_point) # Assigning the results of the function to multiple variables (beans, jars, crates). 
# jelly_beans was changed to beans since jelly_beans only lives within the secret_formula function it can be named again outside of the function.

# remember that this is another way to format a string
print("With a starting point of: {}".format(start_point)) # Prints a formatted string that includes the value of start_point in the brackets
# it's just like with an f"" string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.") # Prints a formatted string that includes the values of beans, jars, and crates

start_point = start_point / 10 # Changes the variable to a new value

print("We can also do that this way:") # Prints a string
formula = secret_formula(start_point) # Creates a variable and assigns it the result of the function secret_formula
# this is an easy way to apply a list to a format string
print("We'd have {} beans, {} jars, and {} crates.".format(*formula)) # Prints a formatted string with the .format command and includes the updated results of the secret_formula function.