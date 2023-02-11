# establishing the ability to pass in arguments
from sys import argv

# script for the program and the argument to be input by the user
script, input_file = argv

# establishing the print_all function which prints the entire file to the terminal using .read()
def print_all(f):
	print(f.read())

# establishing the rewind function which resets the read file, starting at the 0 digit again
def rewind(f):
	f.seek(0)

# establishing the print_a_line function which takes in two arguments (the specified line and the file) and prints the line number and the string
def print_a_line(line_count, f):
	print(line_count, f.readline())

# defines the variable current_file, assigning it to open the file passed in by the programmer/user
current_file = open(input_file)

# prints a string
print("First let's print the whole file:\n")

# calls the print_all function, passing in the file that the user/programmer specified
print_all(current_file)

# prints a string
print("Now let's rewind, kind of like a tape.")

# calls the rewind function, passing in the utilized file
rewind(current_file)

# prints a string
print("Let's print three lines:")

# defines the variable current_line, assigning a value and calling the print_a_line function utilizing the arguments current_line and the established file
current_line = 1
print_a_line(current_line, current_file)
# print_a_line(current_line, test.txt):
#     print(current_line, test.txt.readline(1))

# defines the variable current_line again, using the previous variable plus 1, and calling the same print_a_line function
current_line = current_line + 1
print_a_line(current_line, current_file)
# print_a_line(current_line, test.txt):
#     print(current_line, test.txt.readline(2))

# defines the variable current_line again, using the previous variable plus 1, and calling the same print_a_line function
current_line = current_line + 1
print_a_line(current_line, current_file)
# print_a_line(current_line, test.txt):
#     print(current_line, test.txt.readline(3))