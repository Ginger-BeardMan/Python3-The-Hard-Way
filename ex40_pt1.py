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

iron_man = Song(["Has he lost his mind?",
	"Can he see of is he blind",
	"Can he walk at all",
	"Or, if he moves, will he fall?"])

cowboys = Song(["Here we come, reach for your gun",
	"and you better listen well, my friend",
	"you see, it's been slow down below",
	"aimed at you, we're the Cowboys from Hell"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

iron_man.sing_me_a_song()

cowboys.sing_me_a_song()