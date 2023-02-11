# From the system, import the use of the argument variable
from sys import argv

# Establish the argument variable with script name and filename (to be the input argument)
script, filename = argv

# Creates the txt variable and assigns it the opening of the file 
txt = open(filename)

# Prints the name of the file in a string. Formatted to allow the calling of {filename}
print(f"Here's your file {filename}:")
# Prints the text of the file?
print(txt.read())

# Prints a string asking for input from the user
print("Type the file name again:")
# Allows for input from the user and creates the variable to hold the information
file_again = input("> ")

# Creates a variable and assigns it the action of opening the file that was input by the user
txt_again = open(file_again)

# Prints the txt from the file that the user input
print(txt_again.read())