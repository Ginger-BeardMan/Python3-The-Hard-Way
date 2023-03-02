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

class

continue

# def - define an object, typically used to define a function
	# def this_function():

del

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

exec

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

global

# if - a type of conditional statement. If a condition is True then the script written after the condition will run. 
	# if jeans == 'blue':
		# print('Put on your jeans')

# import - a tool utilized to pull in additional functions/operators/mechanisms to use in a script. Python does not automatically run with all capabilities by default.
	# from sys import argv

# in - part of for loops
	# for x in dresser:
		# print(x)

is

lambda

not

or

pass

# print - takes what is passed in to it and displays it on the screen/console/etc.
	# print('Hello') will display Hello

raise

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