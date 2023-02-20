# Newish, why import the sys? What is sys.argv?
import sys 
script, input_encoding, error = sys.argv


# Function with arguments.
def main(language_file, encoding, errors): 
	line = language_file.readline() # Variable assigned a line from the file, the function 'reads a line'

	if line: # A if statement, when true, runs the following code. This is written such that it will be true until the entire file is read (i.e. if there is a line that can be read, perform the following:)
		print_line(line, encoding, errors) 
		return main(language_file, encoding, errors) # Calling the function main again turns this function in to a loop since it returns back to it's beginning each time it's run


# Function with arguments to print the lines.
def print_line(line, encoding, errors): 
	next_lang = line.strip() # Strip removes any leading/beginning and trailing/ending spaces. In this case, the line will have no spaces at the beginning or end of it. 
	raw_bytes = next_lang.encode(encoding, errors=errors)
	# .encode() returns an encoded version (the 'bytes' version) of a string (default is utf-8). 
	# The first parameter specifies the type of encoding, the second parameter specifies the message if an error occurs
	cooked_string = raw_bytes.decode(encoding, errors=errors) 
	# .decode() returns the 'bytes' version converted to a string.
	# The first parameter specifies the type of encoding, the second parameter specifies the message if an error occurs

	print(raw_bytes, "<===>", cooked_string) 


languages = open("languages.txt", encoding="utf-8") 
# Variable assigned the language.txt file in open mode
# Encoding indicates what type of encoding to use, i.e. what format to display the information in.
# utf-8 is a variable length character encoding standard used for electronic communication

main(languages, input_encoding, error)