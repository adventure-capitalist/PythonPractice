list_colors = ['w', 'g', 'r', 'b', 'v']

for v in list_colors:
    print v + '\n'
    if v == 'w':
        print "my fav color"

count = 0

def goWhile(count):
    print 'function starts'
    while (count < 10):
    	print 'The count is', count
    	count = count+1
print 'fun ends'

goWhile(1)
