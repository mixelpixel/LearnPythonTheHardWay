def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for %d parties!" % (cheese_count + boxes_of_crackers)
	print "Get a blanket.\n"
	
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

print "And with user input:"
x = int(raw_input("How many cheeses?"))
y = int(raw_input("How many boxes of crackers?"))
cheese_and_crackers(x, y)

print "And with user input:"
cheese_and_crackers(int(raw_input("How many kinds of cheese?")), int(raw_input("How many boxes of crackers?")))