#names the function delcares the arguments
def cheese_and_crackers(cheese_count, boxes_of_crackers):
#clears up that the number variables given are called cheese count and positions it in the string
    print "You have %d cheeses!" % cheese_count
#same as above but for boxes of crackers
    print "You have %d boxes of crackers!" % boxes_of_crackers
#says a cheeky comment
    print "Man that's enough for a party!"
    print "Get a blanket.\n"
#provides the variables that correspond to the arguments
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)
# assigns the arguments
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

#calls the function, sets the arguments
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

#calls the function, assigns the variables
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

#you can call the function and throw assigned arguments into the maths variables
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
