# Exercise 22 is to review all previous exercises, typing out all characters used, and describing their purpose/function

# ex1
# Each of these lines is a command to print a string.

print('Hello World!')
print('Hello Again')
print('I like typing this.')
print('This is fun.')
print('Yay! Printing.')
print("I'd much rather you 'not'.")
print('I "said" do not touch this.')

# ex2
# These are comments using the # symbol and there are additional print commands for strings.

# A comment, this is so you can read your program later.
# Anything after the # is ignored by pythong.

print('I could have code like this.') # and the comment after is ignored

# You can also use a comment to 'disable' or comment out code:
# print("This won't run")

print('This will run.')

# ex3
# Each of these lines is a command to print. Those with only quotes print strings only, those with quotes
# and equations print a string with the answer to the equation. Lastly, there are print commands for evaluating
# whether a number is greater than, greater than or equal to, or less than or equal to another number.

print("I will now count my chickens:")

print("Hens", 25 + 30/6)
print("Roosters", 100 - 25 * 3 % 4)

print("Now I will count the eggs:")

print(3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)

print("Is it true that 3 + 2 < 5-7?")

print(3 + 2 < 5 -7)

print('What is 3 + 2?', 3 + 2)
print('What is 5 - 7?', 5 - 7)

print("Oh, that's why it's false.")

print("How about some more.")

print("Is it greater?", 5 > -2)
print("Is it greater or equal?", 5 >= -2)
print("Is it less or equal?", 5 <= -2)

# ex4

cars = 100 # Creates the variable cars and assigns 100 to it
space_in_a_car = 4.0 # Creates the variable space_in_a_car and assigns 4.0 to it, a floating number
drivers = 30 # Creates the variable drivers and assigns 30 to it. 
passengers = 90 # Creates the variable passengers and assigns 90 to it. 
cars_not_driven = cars - drivers # Creates the variable cars_not_driven and assigns the difference between the cars variable and the drivers variable to it. 
cars_driven = drivers # Creates the variable cars_driven and assigns the variable drivers to it. 
carpool_capacity = cars_driven * space_in_a_car # Creates the variable carpool_capacity and assigns cars_driven to it. 
average_passengers_per_car = passengers/cars_not_driven # Creates the variable average_passengers_per_car and assigns passengers divided by cars_not_driven to it. 

print("There are", cars, "cars available.") # Prints a string using the value of the cars variable within the string. Leaving it out of quotes will use the value of the variable instead of quoting the literal name of the variable. 
print("There are only", drivers, "drivers available.") # Prints a string using the value of the drivers variable within the string.
print("There will be", cars_not_driven, "empty cars today.") # Prints a string using the value of the cars_not_driven variable within the string.
print("We can transport", carpool_capacity, "people today.") # Prints a string using the value of the carpool_capacity variable within the string.
print("We have", passengers, "to carpool today.") # Prints a string using the value of the passengers variable within the string. 
print("We need to put about", average_passengers_per_car, "in each car.") # Prints a string using the value of the average_passengers_per_car within the string.

# ex5

my_name = "Zed A. Shaw" # Establishes the variable my_name and assigns it a string
my_age = 35 # not a lie # Establishes the variable my_age and assigns it a number
my_height = 74 # inches # Establishes the variable my_height and assigns it a number
my_weight = 180 # lbs # Establishes the variable my_weight and assigns it a number
my_eyes = "Blue" # Establishes the variable my_eyes and assigns it a string
my_teeth = 'White' # Establishes the variable my_teeth and assigns it a string
my_hair = 'Brown' # Establishes the variable my_hair and assigns it a string

print(f"Let's talk about {my_name}") # Prints a string, utilising the f (format) character in order to insert the variable my_name within the string instead of seperated outside the quotes
print(f"He's {my_height} inches tall") # Prints a string, also utilizing 'format' to embed my_height 
print(f"He's {my_weight} pounds heavy.") # Prints a string, also utilizing 'format' to embed my_weight
print("Actually that's not too heavy") # Prints a string
print(f"He's got {my_eyes} eyes and {my_hair} hair.") # Prints a string utilizing 'format' to embed both my_eyes and my_hair within the string quotes
print(f"His teeth are usually {my_teeth} depending on the coffee.") # Prints a string utilizing 'format' to embed my_teeth within the string quotes

# this line is tricky, try to get it exactly right
total = my_age + my_height + my_weight # Creates a variable 'total' and assigns the combined numbers of my_age, my_height, and my_weight
print(f"If I add {my_age}, {my_height}, and {my_weight} I get {total}.") # Prints a string utilizing 'format' to embed my_age, my_height, my_weight, and total within the string quotes. 

# ex6

types_of_people = 10 # Creates a variable and assigns it a number
x = f"There are {types_of_people} types of people." # Creates a variable and assigns it a string with the format command and types_of_people embeded within the string quotes

binary = "binary" # Creates the variable binary and assigns it a string
do_not = "don't" # Creates the variable do_not and assigns it a string
y = f"Those who know {binary} and those who {do_not}." # Creates a variable and assigns it a string with the format command and both binary and do_not embeded within the string quotes

print(x) # Prints the variable x
print(y) # Prints the variable y

print(f"I said: {x}") # Prints a formated string to include the variable x embeded within
print(f"I also said: '{y}'") # Prints a formated string to include the variable y embeded within

hilarious = False # Creates a variable and assigns it the boolean false
joke_evaluation = "Isn't that joke so funny?! {}" # Creates a variable and assigns it a string with an emtpy format bracket

print(joke_evaluation.format(hilarious)) # Prints the joke_evaluation string, formatted to include the variable hilarious

w = "This is the left side of..." # Creates a variable and assigns it a string
e = "a string with a right side." # Creates a variable and assigns it a string

print(w + e) # Prints a string that is the combination of the variables w and e

# ex7

print("Mary had a little lamb.") # Prints a string
print("It's fleece was white as {}.".format('snow')) # Prints a string using the format command to insert 'snow' within the string quotes
print("And everywhere that Mary went.") # Prints a string
print("." * 10) # Prints 10 periods

end1 = "C" # Creates the variable end1 and assigns it a string
end2 = "h" # Creates the variable end2 and assigns it a string
end3 = "e" # Creates the variable end3 and assigns it a string
end4 = "e" # Creates the variable end4 and assigns it a string
end5 = "s" # Creates the variable end5 and assigns it a string
end6 = "e" # Creates the variable end6 and assigns it a string
end7 = "B" # Creates the variable end7 and assigns it a string
end8 = "u" # Creates the variable end8 and assigns it a string
end9 = "r" # Creates the variable end9 and assigns it a string
end10 = "g" # Creates the variable end10 and assigns it a string
end11 = "e" # Creates the variable end11 and assigns it a string
end12 = "r" # Creates the variable end12 and assigns it a string

print(end1 + end2 + end3 + end4 + end5 + end6, end=' ') # Prints a combination of variables in to a string with a space at the end
print(end7 + end8 + end9 + end10 + end11 + end12) # Prints a combination of variables in to a string

# ex8

formatter = "{} {} {} {}" # Creates a variable with 4 brackets that can be formatted

print(formatter.format(1, 2, 3, 4)) # Prints the formatter string using the format function to make it 1, 2, 3, 4
print(formatter.format("one", "two", "three", "four")) # Prints the formatter string using the format function to make it "one", "two", "three", "four"
print(formatter.format(True, False, False, True)) # Prints the formatter string using the format function to make it True False False True
print(formatter.format(formatter, formatter, formatter, formatter)) # Prints the formatter string using the format function to print formatter four times
print(formatter.formate(
	"Bee bee",
	"Naa naa",
	"Koo koo",
	"See saw"
)) # Prints the formatter string using the format function to print four seperate lines of strings

# ex9

days = "Mon Tue Wed Thu Fri Sat Sun" # Creates a variable 'days' and assigns it a string
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJyl\nAug" # Creates a variable months and assigns it a string with new line characters (\n)

print("Here are the days: ", days) # Prints a string that includes the variable days
print("Here are the months: ", months) # Prints a string that includes the variable months

print("""
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
""") # Prints a string that spans across multiple lines due to the usage of triple quotes

# ex10

tabby_cat = "\tI'm tabbed in." # Creates a variable and assigns it a string that will be indented using the tab command (\t)
persian_cat = "I'm split\non a line." # Creates a variable and assigns it a string that will be seperated across two lines using the new line command (\n)
backslash_cat = "I'm \\ a \\ cat." # Creates a variable and assigns it a string that will have backslashes between each word

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
""" # Creates a variable and assigns it a string that will make a list that is indended using the tab command \t and new line command \n

print(tabby_cat) # Prints the variable tabby_cat
print(persian_cat) # Prints the variable persian_cat
print(backslash_cat) # Prints the variable backslash_cat
print(fat_cat) # Prints the variable fat_cat

# ex11

print("How old are you?", end=' ') # Prints a string with a space at the end
age = input() # Asks the user/viewer to input the requested information and assigns it to a variable
print("How tall are you?", end=' ') # Prints a string with a space at the end
height = input() # Asks the user/viewer to input the requested information and assigns it to a variable
print("How much do you weight?", end=' ') # Prints a string with a space at the end
weight = input() # Asks the user/viewer to input the requested information and assigns it to a variable

print(f"So, you're {age} old, {height} tall and {weight} heavy.") # Prints a string using the formatted function (f) to include the inputed information of age, height, and weight

# ex12

age = input("How old are you? ") # Creates a variable (age) and prompts the user with a question, assigning the inputted information to the variable
height = input("How tall are you? ") # Creates a variable (height) and prompts the user with a question, assigning the inputted information to the variable
weight = input("How much do you weigh? ") # Creates a variable (weight) and prompts the user with a question, assigning the inputted information to the variable

print(f"So, you're {age} old, {height} tall and {weight} heavy.") # Prints a string using the formatted function (f) to include the inputed information of age, height, and weight

# ex13

from sys import argv # From the system, imports the argument variable (argv) which 'holds' your arguments that are passed to the script when running it

script, first, second, third = argv # These are the command line arguments that are passed in to the script when launching it
 
print("The script is called:", script) # Prints a string with the name of the script (The file that your script is saved on)
print("Your first variable is:", first) # Prints a string with the name of the first command line argument after the script name
print("Your second variable is:", second) # Prints a string with the name of the second command line argument after the script name
print("Your third variable is:", third) # Prints a string with the name of the second command line argument after the script name

# ex14

from sys import argv # From the system, imports the argument variable (argv) which 'holds' your arguments that are passed to the script when running it

script, user_name = argv # These are the command line arguments that are passed in to the script when launching the script
prompt = '> ' # A prompt to insert user_name which is assigned to the variable

print(f"Hi {user_name}, I'm the {script} script.") # Prints a string that uses the format function to include {user_name} and {script}
print("I'd like to ask you a few questions.") # Prints a script
print(f"Do you like me {user_name}?") # Prints a string that uses the format function to include {user_name}
likes = input(prompt) # Displays a prompt and allows the user to input information that is assigned to the variable likes

print(f"Where do you live {user_name}?") # Prints a string that uses the format function to include {user_name}
lives = input(prompt) # Displays a prompt and allows the user to input information that is assigned to the variable lives

print("What kind of computer do you have?") # Prints a string
computer = input(prompt) # Displays a prompt and allows the user to input information that is assigned to the variable computer

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""") # Prints a multi-line string that uses the format function to include the variables likes, lives, and computer

# ex15

from sys import argv # From the system import the argument variable (argv) which holds your arguments that are passed to the script

script, filename = argv # Indicates items to be passed in to the argument variable (the script name and the file name that is seperate from the py file)

txt = open(filename) # Creating a variable, txt, and assigning it the file and using the open() function (it opens the file in the 'background')

print(f"Here's your file {filename}") # Prints a formatted (f) string which includes the 'filename' within the quote strings
print(txt.read()) # Prints the opened file (open(filename)) which was assigned to txt. This is printed using .read() 

print("Type the filename again:") # Prints a string
file_again = input("> ") # Creates a variable file_again and assigns whichever new file is input when the user is prompted

txt_again = open(file_again) # Creates a variable 'txt_again' and assigns it the variable 'file_again' that has been opened using the open() function

print(txt_again.read()) # Prints the txt_again variable using the .read() function

# ex16

from sys import argv # From the system import the argument variable (argv)

script, filename = argv # Assigns the command line variables to the argument variable for the script

print(f"We're going to erase {filename}.") # Prints a formatted script (f) that includes the name of the file input on the command line
print("If you don't want that, hit CTRL-C (^C).") # Prints a script
print("If you do want that, hit RETURN.") # Prints a script

input("?") # Prints a script along with allowing the user to input their command (RETURN OR CTRL-C based on the previous scripts)

print("Opening the file...") # Prints a string
target = open(filename, 'w') # Creates a variable (target) and assigns it the opened file along with putting the file in "write" mode ('w')

print("Truncating the file. Goodbye!") # Prints a string
target.truncate() # Takes the 'target' variable and resizes it (aka truncates it). The size does not change, however, because no size change is specified with the ()

print("Now I'm going to ask you for three lines.") # Prints a string

line1 = input("line 1: ") # Prints a string along with an input prompt for the user to add a new line which is assigned to the line1 variable
line2 = input("line 2: ") # Prints a string along with an input prompt for the user to add a new line which is assigned to the line2 variable
line3 = input("line 3: ") # Prints a string along with an input prompt for the user to add a new line which is assigned to the line3 variable

print("I'm going to write these to the file.") # Prints a string

target.write(line1) # Takes the target variable an writes in the string input in the line1 variable to the file use in this script ('filename')
target.write('\n') # Indicates that the next string will be placed on a new line
target.write(line2) # Takes the target variable an writes in the string input in the line2 variable to the file use in this script ('filename')
target.write('\n') # Indicates that the next string will be placed on a new line
target.write(line3) # Takes the target variable an writes in the string input in the line3 variable to the file use in this script ('filename')
target.write('\n') # Indicates that the next string will be placed on a new line

print("And finally, we close it.") # Prints a string
target.close() # Closes the file assigned to the target variable

# ex17

from sys import argv # From the system imports the argument variable
from os.path import exists # From the system import the exists function which can be used to determine if an item (file/variable/etc.) exists in the script/system/program

script, from_file, to_file = argv # Assigns the script name, the file with information (from_file) and the file without information to transfer/copy to (to_file)

print(f"Copying from {from_file} to {to_file}") # Prints a formatted string that includes the from_file name and to_file name.

in_file = open(from_file) # Assigns the open from_file to in_file
indata = in_file.read() # Assigns in_file in read mode to the variable indata

print(f"The input file is {len(indata)} bytes long") # Prints a formatted string that includes the length of the variable indata in bytes

print(f"Does the output file exist? {exists(to_file)}") # Prints a formatted string that includes whether to_file exists using the exists function
print("Ready, hit RETURN to continue, CTRL-C to abort.") # Prints a string
input() # Prompts the user/viewer to input information

out_file = open(to_file, 'w') # Creates a variable and assigns it the open file to_file in write mode ('w')
out_file.write(indata) # Takes out_file and writes the information from indata to it

print('Alright, all done.') # Prints a string

out_file.close() # Closes the out_file
in_file.close() # Closes the in_file

# Written as one line?
# out_file = open(to_file, 'w').write(open(from_file).read())

# ex18

def print_two(*args): # Creates a function (def=define) and names it, including an argument parameter within the parenthesis
	arg1, arg2 = args # Defines args
	print(f"arg1: {arg1}, arg2: {arg2}") # Completes the function by printing a formatted string that prints arg1 and what was passed through and arg2 and what was passed through

def print_two_again(arg1, arg2): # Creates a function (def=define) and names it, including two argument parameters within the parenthesis
	print(f"arg1: {arg1}, arg2: {arg2}") # Completes the function by printing a formatted string that prints arg1 and what was passed through and arg2 and what was passed through

def print_one(arg1): # Creates a function (def=define) and names it, including one argument parameter within the parenthesis
	print(f"arg1: {arg1}") # Completes the function by printing a formatted string that prints arg1 and what was passed through

def print_none(): # Creates a function (def=define) and names it, no argument is included here
	print("I got nothin'.") # Completes the function by printing a string

print_two("Zed", "Shaw") # Calls the function and passes in two arguments that are strings
print_two_again("Zed", "Shaw") # Calls the function and passes in two arguments that are strings
print_one("First!") # Calls the function and passes in an argument that is a string
print_none() # Calls the function