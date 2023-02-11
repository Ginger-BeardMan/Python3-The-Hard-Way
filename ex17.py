# from the system import the argument variable
from sys import argv
# import the exists command which checks whether something is True (exists) or False (does not)
from os.path import exists

# your script name, your original file to copy, the file that you will copy to
script, from_file, to_file = argv

# a script indicating the action of the code, to copy from one file to another
print(f"Copying from {from_file} to {to_file}")

# we could do these two on one line, how? indata = read(in_file(open(from_file)))
# in_file = open(from_file)
# indata = in_file.read()
# consolidating this code in to one line
indata = open(from_file).read()

print(f"The input file is {len(indata)} bytes long")

print(f"Does the output file exist? {exists(to_file)}")

print("Ready, hit RETURN to continue, CTRL-C to abort.")

input()

# out_file = open(to_file, 'w')
# out_file.write(indata)
# consolidating these lines in to one line
out_file = open(to_file, 'w').write(indata)

print("Alright, all done.")

# removing these as the file already closes due to the consolidation of the indata line of code
# out_file.close()
# in_file.close()