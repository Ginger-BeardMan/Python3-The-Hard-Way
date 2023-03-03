# PART 1

# and - used to test two statements. Returns True if both are True, False if one is False, and False if both are False 

# as - used to create an alias
	# from sys import argv as arg

# assert - lets you test if a condition in your code returns True, if it does not then an error will be returned. 
	# x = 'hello'
	# assert x == 'hello'

# break - used to stop a for or while loop if a condition is met so that the loop does not run forever.
	# for i in range(9):
	#	if i > 3:
	#		break
	#	print(i) 

# class - an object constructor. Used to create an overarching class with sub characteristics. 
	# class Person:
		# def __init__(self, age, weight, height):
			# self.age = age
			# self.weight = weight
			# self.height = height

	# user = Person(20, 100, 200)

	# print(user.age)

# continue - used to skip a specific iteration in a for or while loop and move on to the next iteration.
	# for i in range(9):
		# if i == 3:
			# continue
		# print(i)

# def - define an object, typically used to define a function
	# def this_function():

# del - used to delete objects (i.e. anything in python)
	# x = 'hello'
	# del x
	# print(x)
	# results in an error that x is not defined

# elif - used in an if statement, stands for else-if. Will be used if the if statement contains more than two contingencies.
	# if power = on:
	# elif power = half:
	# else power = off:

# else - used in an if statement to tell the script to run code if all other conditions have not been met in the if statement.  

# except - used to handle errors when using try. If an error occurs then the exception runs
	# try:
	# 	print(x)
	# except:
	# 	print("An exception occurred")

# exec - executes any length of specified python code
	# x = 'name = "John"\nprint(name)'
	# exec(x)

	# exec(object, global, locals)

# finally - indicates a condition to run with a try except block. This code will be executed whether there is an error or not when running try
	# try:
	# 	print(x)
	# except:
	# 	print("An exception occurred")
	# finally:
	# 	print("The 'try except' is finished")

# for - a type of loop used with lists. It tells the script to run code as long as there are items in the list.
	# for x in list:
		# x += 1
		# print(x)

# from - from (location a) get a function/operator/etc.
	# from sys import argv (from the system import the argument variable to use in this script)

# global - used to declare a variable within a function (which would normally be local to that function only) as usable outside of that function once that function has been called
	# def myfunction():
	# 	global x
	# 	x = 'hello'
	#
	# myfunction()
	#
	# print(x)

# if - a type of conditional statement. If a condition is True then the script written after the condition will run. 
	# if jeans == 'blue':
		# print('Put on your jeans')

# import - a tool utilized to pull in additional functions/operators/mechanisms to use in a script. Python does not automatically run with all capabilities by default.
	# from sys import argv

# in - part of for loops
	# for x in dresser:
		# print(x)

# is - used to test of two variables refer to the same object. It returns True or False (even if the objects are 100% equal which would used the == operator instead of is)
	# x = ['apple', 'banana', 'cherry']
	# y = x
	# print(x is y)

# lambda - a small anonymous function that takes in any number of arguments but only has one expression.
	# x = lambda a: a + 10
	# print(x(5))
	# in this example 'lambda' is substituted with 'x'

# not - a logical operator. Returns True if the statement is False, returns False if the statement is True

# or - used in boolean statements to measure if one condition/statement/etc. OR a second condition/statement/etc. is True
	# True or True == True
	# True or False == True
	# False or True == True
	# False or False == False

# pass - used as a placeholder in loops instead of leaving blank code (since you cannot have blank code in loops)
	# for x in [0, 1, 2]:
	# 	pass

# print - takes what is passed in to it and displays it on the screen/console/etc.
	# print('Hello') will display Hello

# raise - a keyword used to define or raise an exception. It allows you to indicate what kind of error to raise and the text to print to the user. 
	# x = 'hello'

	# if not type(x) is int:
	#   raise TypeError('Only integers are allowed')

# return - used in a function to call back to something within the function, the function itself again, or to a different function/variable outside of the current function.

# try - used to test a block of code for errors. Used in conjunction with except. 
	# try:
	# 	print(x)
	# except:
	# 	print("An exception occurred")

# while - a type of loop that tells the system that while a condition is true run code (can loop infinitally if not written carefully)

# with - used to simplify code and to ensure that a resource is properly released when the code using the resource is completely executed (e.g. looks AND runs cleaner)
	# CHANGE THIS:
	# file = open('file_path', 'w')
	# 	file.write('hello world!')
	#	file.close()
	# INTO THIS:
	# with open('file_path', 'w') as file:
	#	file.write('hello world!')

# yield - when called returns a generator. A generator is an iterator, like a list, however, a generator can only be called once unlike a list.
	# I'm not sure of the use of this and why it would be used


# PART 2 - Data Types

True # created by comparing two conditions, either True v False or other conditions that could be True or False. True or False == True
False # created by comparing two conditions, either True v False or other conditions that could be True or False. False and True == False
None # no value
bytes # stores bytes x = b'hello'
strings # sentences/phrases/quotes, 'My name is Jon-Jon'
numbers # straight numbers without decimals, 1, 6, 999, 3243253256
floats # numbers with decimals, 3.4, 55.24, etc.
lists # mylist = [name, weight, age, height]
dicts # stores a key=value mapping of things, e = {'x': 1, 'y': 2}

# Part 3 - String Escape Sequences

# \\ # will allow one backslash in a string wherever it is placed
# \' # will keep a single quotation mark in a string where placed, used to make sure that the string is not broken when a single quotation mark is used within it
# \" # will keep a double quotation mark in a string where placed, used to make sure that the string is not broken when a double quotation mark is used within it
# \a # returns the ASCII bell character in python
# \b # will remove the space/character directly behind it when put in a string
# \f # formfeed f string 
# \n # puts the section of the string that follows it on a new line
# \r # resets the position of the cursor to the beginning of a new line of text. print('hello \rworld') will print world as the cursor resets and world is printed over hello
# \t # tabs/indents a string
# \v # vertical tab