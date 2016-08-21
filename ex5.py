name = 'Patrick D. Kennedy'
age = 42 # not a lie
height = 70 # cm
weight = 200 # kg
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d centimeters tall." % (height * 2.54)
print "He's %d kilograms heavy." % (weight / 1.45)
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee and cigarettes" % teeth

#tricky
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)