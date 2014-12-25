number = raw_input('pick a number: ')

print "Your number is {}".format(number)
number = int(number)
print "Fizzbuzz time!"
for i in xrange(1, number + 1):
    three = i%3 == 0
    five = i%5 == 0
    if three and five:
        print "fizzbuzz"
    elif three:
        print "fizz"
    elif five:
        print "buzz"
    else:
        print(i)

