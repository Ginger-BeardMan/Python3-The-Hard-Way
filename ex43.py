# Then I go through these notes, drawings, and descriptions, and I pull out the key concepts. There’s a
# simple trick to doing this: Simply make a list of all the nouns and verbs in your writing and drawings,
# then write out how they’re related. This gives me a good list of names for classes, objects, and functions
# in the next step. I take this list of concepts and then research any that I don’t understand so I can refine
# them further if needed.

# Gothons from Planet Percal #25

# Game Ideas -

# Death: This is when the players dies and should be funny/odd

# Central Corridor: This is the starting point with an enemy already ready to fight and a joke has to be used to defeat the enemy

# Laser Weapon Armory: This has a number key that needs to be guessed by the player and houses the neutron bomb that will blow up the ship when the player escapes

# The Bridge: Basically the final battle scene area before the player places the bomb and escapes

# Escape Pod: Where the hero escapes IF they guess the right pod

# Key Concepts:

Alien

Player

Ship

Maze

# Room (getting rid of this and just going with scene)

Gothon

*Map
	next_scene
	opening_scene
*Engine
	play
*Scene
	enter # (this will be inherited by the 'scenes' below)
	*Death
	*Central Corridor
	*Laser Weapon Armory
	*The Bridge
	*Escape Pod

# Source Code:

from sys import exit
from random import randint
from textwrap import dedent # dedent allows for the use of """ with strings and eliminates leading white-space from the beginning of lines.


class Scene(object):

	def enter(self):
		print("Welcome to your next challenge.")
			# corridor
			print("The alarm is blaring, the lights are flashing, and the central corridor is madness.")
			print("You choose to make your way towards the Laser Weapon Armory, who knows what might be there. First stop is the Med Bay")
			print("You make your way down the hall and come face to face with a snarlying creature.")
			alien()
			# med bay
			print("The med bay is quiet, but is in disaray. Clearly the rest of the crew thought they needed supplies like you.")
			print("You pick up some bandages to mend your wounds from whatever creature you just encountered. Next you need to get to the cafateria, just before the Armory.")
			print("You go to leave out the back door towards the cafateria and meet another obstacle and it's big and green.")
			alien()
			# cafateria
			print("The cafateria is a war zone, things are flying every which way and you struggle to find your way through.")
			print("You reach the other door but a massive blob is sitting in your way.")
			alien()
			# laser weapon armory
			print("You finally reach the armory. You find a laser and spot something you hadn't thought of before...")
			print("With all this chaos, it's unlikely that much of the crew is alive or on the ship anymore, you need to erradicate this threat.")
			print("You grab the neutron bomb and head to the bridge to place it for detonation.")
			next_scene()
			# the bridge
			print("You reach the bridge and it looks like you were expected. A creature twice the size of you is standing there, poised for battle.")
			print("It probably didn't expect your new found weapon or that you grabbed the neutron bomb. You ready your pickle laser and prepare to fight.")
			alien()
			# escape pod
			print("Somehow you reach the escape pod room and set up the bomb for detonation with enough time to get out of the blast radious.")
			print("The only problem is that not every pod works and there are three left. Which is the right pod? You must head to the terminal to figure it out and set up the correct one for departure.")
			print("What do you choose?")
			EscapePod()
		exit(1)

class Engine(object):

	def __init__(self, scene_map):
		pass

	def play(self):
		pass

class Death(Scene):

	def enter(self):
		pass

class CentralCorridor(Scene):

	def enter(self):
		pass

class MedBay(Scene):

	def enter(self):
		pass

class Cafateria(Scene):

	def enter(self):
		pass

class LaserWeaponArmory(Scene):

	def enter(self):
		pass

class TheBridge(Scene):

	def enter(self):
		pass

class EscapePod(Scene):

	def enter(self):
		pass

class Map(object):

	def __init__(self, start_scene):
		pass

	def next_scene(self, scene_name):
		pass

	def opening_scene(self):
		print("You hear the alarm sound while in your cabin.")
		print("You may need to defend yourself so you look around the room for something to use.")
		print("You see a whoopy cusion, a book of dad jokes, and a rubber chicken toy, which do you go with?")

		starting_weapon = input('> ')
		
		if starting_weapon == 'book of dad jokes':
			print("You grab the book, turn around to leave your cabin and immediately come face to face with a creater which you've never seen before.")
			print("You quickly flip through the book, find a joke and say it as fast as possible. The creature laughs uncontrollably, shaking on the floor.")
			print("It's head explodes from so much joy.")
			alien = False
			next_scene()
		elif starting_weapon == 'whoopy cusion':
			print("You grab the whoopy cusion, turn around to leave your cabin and immediately come face to face with a creater which you've never seen before.")
			print("You force air in to the whoopy cusion as fast as possible and squeeze it in the face of the creature.")
			print("It appears insulted and quickly angers even more, striking you in the head with it's massive clube. Everything goes black.")
			alien = True
			death()
		else:
			print("You grab the rubber chicken, turn around to leave your cabin and immediately come face to face with a creater which you've never seen before.")
			print("You squeeze the rubber chicken in the face of the creature as many times as possible, hoping something happens to save you.")
			print("It appears insulted and quickly angers even more, striking you in the head with it's massive clube. Everything goes black.")
			alien = True
			death()
		pass

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()

# Tools to use: for loops, while loops, input, if-else, lists, dicts

# if alien dies set to False and trigger next_scene
# if alien lives keep as True and trigger death
