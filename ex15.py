#This is importing a library 
from sys import argv
#here it saves what it is next to the script 
script, filename = argv
#here is opens the "filename" we gave in the script
txt = open(filename)
#here it prints the name of the file we opened
print ("Here's your file %r:" %filename)
#here it opens the file and present it to the script "it reads it"
print (txt.read())
#here we imput the filename again "we late the user open a file to read it"
print("Type the file name again:")
file_again = input("> ")
#it opens the file that the user named
txt_again = open(file_again)
#it reads the file the user told to the program to open
print (txt_again.read())