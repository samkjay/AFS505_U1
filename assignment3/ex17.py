from sys import argv
from os.path import exists

script, from_file, to_file = argv

#print(f"Copying from {from_file} to {to_file}")

in_file = open(from_file)
indata = in_file.read()

#above two commands in one line

#print(f"The Input file is {len(indata)} bytes long")

#print(f"Does the output file exist?{exists(to_file)}")
#print("Ready, hit RETURN to continue, CTRL_C to abort")
#input()

out_file = (open(to_file, "w"))
out_file.write(indata)

#print("Alright, all done")

out_file.close()
in_file.close()
