#saying how many people there are, setting x equal to a string.
x = "There are %d types of people." % 10
#setting binary equal to binary
binary = "binary"
#setting do_not equal to don't avoiding the problem with the apostrophe
do_not = "don't"
#settiing y equal to a string, setting up a function for binary and do_not
y = "Those who know %s and those who %s." % (binary, do_not)

#printing our completed functions
print x
print y
#printing the functions within a string
print "I said: %r." % x
print "I also said: '%s'." % y
#setting var hilarious equal to false
hilarious = False
#setting joke_evaluation equal to a function inside a string.
joke_evaluation = "Isn't that joke so funny?! %r"
#using hilarious as a variable inside function joke_evaluation
print joke_evaluation % hilarious
#giving two sides of a string a variable
w = "This is the left side of..."
e = "a string with a right side."
#conconating the strings
print w + e
