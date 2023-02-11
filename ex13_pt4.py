# You will still have to type in first, second, third after the file name in powershell to run
from sys import argv
script, first, second, third = argv
script = input('Name this file: ')
first = input('Tell me a noun: ')
second = input('Tell me a verb: ')
third = input('Tell me an adjective: ')

print('This script is called:', script)
print('The noun you gave was:', first)
print('The verb you gave was:', second)
print('The adjective you gave was:', third)