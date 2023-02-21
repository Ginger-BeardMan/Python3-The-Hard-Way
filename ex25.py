def break_words(stuff):
	"""This function will break up words for us."""
	words = stuff.split(' ') # .split() turns a string in to a list in brackets []. Ex. "This is a string", .split() makes [This, is, a, string]
	return words

def sort_words(words):
	"""Sorts the words."""
	return sorted(words) # .sorted() simply sorts the words in a list. Default is alphabetically.

def print_first_word(words):
	"""Prints the first word after popping it off. *This only occurs within the function"""
	word = words.pop(0) # .pop means to remove the first word in a string/line/doc, whatever is specified. 0 indicates the initial word (0 is the start point of all things, not 1)
	print(word)

def print_last_word(words):
	"""Prints the last word after popping it off. *This only occurs within the function"""
	word = words.pop(-1) # Same as above, however, -1 indicates that the last word (i.e. the first from the end of the line/doc/string. Start at the end and take a step back.)
	print(word)

def sort_sentence(sentence):
	"""Takes in a full sentence and returns the sorted words. *This only occurs within the function"""
	words = break_words(sentence) # Takes the break_words function and assigns it's result to 'words' within the function. 
	return sort_words(words) # Returns the result of the sort_words function after passing in the 'words' variable

def print_first_and_last(sentence):
	"""Prints the first and last words of the sentence. *This only occurs within the function"""
	words = break_words(sentence) # Takes the break_words function and assigns it's result to 'words' within the function.
	print_first_word(words) # Passes in the words variable to the print_first_word function
	print_last_word(words) # Passes in the words variable to the print_last_word function

def print_first_and_last_sorted(sentence):
	"""Sorts the words then prints the first and last one. *This only occurs within the function""" 
	words = sort_sentence(sentence) # Takes the sort_sentence function and assigns it's result to 'words' within the function.
	print_first_word(words) # Passes in the words variable to the print_first_word function
	print_last_word(words) # Passes in the words variable to the print_last_word function
