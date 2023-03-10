import random
from urllib.request import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt" # creates a variable that is assigned a URL that will be used in the script
WORDS = [] # creates an empty list

# creates a dictionary titled phrases
PHRASES = {
	"class %%%(%%%):":
		"Make a class named %%% that is-a %%%.",
	"class %%%(object):\n\tdef __init__(self, ***)":
		"class %%% has-a __init__ that takes self and *** params.",
	"class %%%(object):\n\tdef ***(self, @@@)":
		"class %%% has-a function *** that takes self and @@@ params.",
	"*** = %%%()":
		"Set *** to an instance of class %%%.",
	"***.***(@@@)":
		"From *** get the *** function, call it with params self, @@@.",
	"***.*** = '***'":
		"From *** get the *** attribute and set it to '***'."
}

# do they want to drill phrases first. An if statement that if the length of 
if len(sys.argv) == 2 and sys.argv[1] == "english":
	PHRASE_FIRST = True
else:
	PHRASE_FIRST = False

# load up the words from the website
for word in urlopen(WORD_URL).readlines(): # for each word in the url append it to the list WORDS
	WORDS.append(str(word.strip(), encoding="utf-8")) # appends the words from the url site to the list WORDS


def convert(snippet, phrase): # defines a function that passes in snippet and phrase
	class_names = [w.capitalize() for w in random.sample(WORDS, snippet.count("%%%"))] # creates a variable within the function
	other_names = random.sample(WORDS, snippet.count("***"))
	results = []
	param_names = []

	for i in range(0, snippet.count("@@@")):
		param_count = random.randint(1,3)
		param_names.append(', '.join(random.sample(WORDS, param_count)))

	for sentence in snippet, phrase:
		result = sentence[:]

		for word in class_names:
			result = result.replace("%%%", word, 1)

		for word in other_names:
			result = result.replace("***", word, 1)

		for word in param_names:
			result = result.replace("@@@", word, 1)

		results.append(result)

	return results

try:
	while True:
		snippets = list(PHRASES.keys())
		random.shuffle(snippets)

		for snippet in snippets:
			phrase = PHRASES[snippet]
			question, answer = convert(snippet, phrase)
			if PHRASE_FIRST:
				question, answer = answer, question

			print(question)

			input("> ")
			print(f"ANSWER: {answer}\n\n")
except EOFError:
	print("\nBye")