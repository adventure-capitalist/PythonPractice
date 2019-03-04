#Number of cars
cars = 100
#how many people can fit in each car
space_in_a_car = 4
#how many people have a license to drive
drivers = 30
#how many total commuters
passengers = 90
#number of cars we take out of traffic
cars_not_driven = cars - drivers
#number of cars we use in the carpool
cars_driven = drivers
#max number of people we can take
carpool_capacity = cars_driven * space_in_a_car
#how full our cars need to be today.
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
