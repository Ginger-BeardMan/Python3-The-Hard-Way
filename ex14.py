# Import argument variable from the system
from sys import argv

# Assign script, user_name to argv
script, user_name, title = argv
# What the users sees as a prompt after every question
prompt = 'Answer: '

# Prints a string with user_name and script imbedded within
print(f"Hi {user_name} {title}, I'm the {script} script.")
# Prints string
print("I'd like to ask you a few questions.")
# Prints a question for the user followed by a prompt to input 'likes'
print(f"Do you like me {user_name} {title}?")
likes = input(prompt)

# Prints a string for the user followed by a prompt to input where they live
print(f"Where do you live {user_name} {title}?")
lives = input(prompt)

# Prompts a string for the user followed by a prompts to input what computer they have
print("What kind of computer do you have?")
computer = input(prompt)

# Prints a multi-line string that includes user input of answered questions
print(f'''
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
''')