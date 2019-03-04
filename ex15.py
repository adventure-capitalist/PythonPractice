# #Tells the file to grab an argument from the terminal.
# from sys import argv
# #defines the two arguments as "script" and "filename"
# script, filename = argv
# #grabs the file with that name and sets it equal to txt
# txt = open(filename)
# #prints a statement and then the file name
# print "here's your file %r: " % filename
# #prints the file set equal to txt in plain text
# print txt.read()
#prints out a statement/prompt
print "Type the filename again:"
#defines the raw input entered after the arrow as "file_again"
file_again = raw_input("> ")
#grabs the file with the name and sets it equal to txt_again
txt_again = open(file_again)
#prints the contents of the file called text_again in plain text
print txt_again.read()
