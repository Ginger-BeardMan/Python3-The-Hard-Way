# From system import the argument variable
from sys import argv

# The arguments
script, filename = argv

# Prints a string that is formated to include the file name.
print(f"We're going to erase {filename}.")
# Prints a string that states that a command will be needed in the future for a particular action. 
print("If you don't want that, hit CTRL-C (^C).")
# Prints a string that states that a different command will be needed in the future for a different action. 
print("If you do want that, hit RETURN.")

# A visual for the prompt that the user will see. 
input("?")

# Prints a string to accompany the action of opening a file. 
print("Opening the file...")
target = open(filename, 'w')

# Prints a string to accompany the action of truncating a file. 
print("Truncating the file. Goodbye!")
target.truncate()

# A string that precedes a prompt for user input
print("Now I'm going to ask you for three lines.")

# User input commands that are assigned to three different variables.
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

# Prints a string
print("I'm going to write these to the file.")

# Writes each line in to the file that the user input and seperates them to three seperate lines using the \n command
target.write(line1)
target.write('\n')
target.write(line2)
target.write('\n')
target.write(line3)
target.write('\n')

# Prints a string that is followed by the closing of the file. 
print('And finally, we close it.')
target.close()