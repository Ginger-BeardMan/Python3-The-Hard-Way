# add the feature argument variable (a module) from system by using the import command
from sys import argv
# read the WYSS section for how to run this; this unpacks the argument variable and assigned it to four variables to work with
script, first, second, third = argv

print('This script is called:', script)
print('Your first variable is:', first)
print('Your second variable is:', second)
print('Your third variable is:', third)