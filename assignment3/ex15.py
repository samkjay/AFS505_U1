#import the module(library) argv
from sys import argv
#unpacks argv and are assiged to variables script and filename
script, filename = argv

# open a file and assign it to vatiable txt
txt = open(filename)

#print the file name
print(f"Here's your file {filename}:")
#read the test in the file
print(txt.read())
#prompt the user to type in the file name again
print(f"Type the filename again:")
#save the user input to file_again variable
file_again = input(">")
#opening file saved in fie_again variable and saving the file content text_again variable
txt_again = open(file_again)
# read and printing the content saved in the txt_again variable
print(txt_again.read())

txt.close()
txt_again.close()
