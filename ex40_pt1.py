class Song(object): # Creating a class with an empty object

	def __init__(self, lyrics): # defining a function that takes in the arguments self (the empty object from before) and lyrics
		self.lyrics = lyrics # this sets the lyrics instance variable using the variable self

	def sing_me_a_song(self): # defining a function that takes the argument self
		for line in self.lyrics: # for each line that is available in self.lyrics the code will print that line
			print(line)

happy_bday = Song(["Happy birthday to you",
	"I don't want to get sued",
	"So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
	"With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()