print "How old are you?",
age = int(raw_input())
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r months old, %s tall and %r heavy." % (
    age*12, height, weight)