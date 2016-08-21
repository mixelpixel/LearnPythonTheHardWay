def add(a, b):
    print "ADDING TWO INTEGERS %r + %r" % (a, b)
    return a + b

prompt1 = 'first integer? >>>'
prompt2 = 'second integer? >>>'
added = add(float(raw_input(prompt1)), float(raw_input(prompt2)))

print "Added together, that makes: %r" % (added)

def add(a, b):
    return a + b

prompt1 = 'first integer? >>>'
prompt2 = 'second integer? >>>'
added = add(float(raw_input(prompt1)), float(raw_input(prompt2)))

print "Added together, that makes: %r" % (added)