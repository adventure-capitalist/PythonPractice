i = 0
numbers = []

def addNumbers(i):
    print "At the top i is %d" % i
    numbers.append(i)
    i = i + 1
    print "Numbers now: ", numbers
    print "At the bottom i is %d" % i

for i in range(1, 6):
    addNumbers(i)
    print "the numbers: "
    for num in numbers:
        print num
