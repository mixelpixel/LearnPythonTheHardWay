print "I will now count my chickens:"

print "Hens", 25.0 + 30.0 / 6.0

print "Roosters", 100.0 - 25.0 * 3.0 % 4.0
# P.E.M.D.A.S.
# Parentheses; Exponents; Multiplication;
# Division; Addition; Subtraction
# in the P.E.M.D.A.S. order, so
# 25 times 3 equals 75
# 75 modulo 4 equals 75 divided by 4 resulting
# in 18 with a remainder - after division - of 3 
# and 100 minus 3 equals 97
# Q.E.D.

print "Now I will count the eggs:"

print 3.0 + 2.0 + 1.0 - 5.0 + 4.0 % 2.0 - 1.0 / 4.0 + 6.0
# solve using PEMDAS: no P. E. or M.
# 4 modulo 2 is zero - evenly dividable, no remainder
# 1 divided by 4 is 0.25 - solvable with floating point
# so, 3+2+1-5+0-0.25+6 
# as 5+1-5+0 = 1
# 1 - 0.25 = 0.75
# 0.75 + 6 = 6.75,
# Also, solve using floating point integer
# 3.0 + 2.0 + 1.0 - 5.0 + 4.0 % 2.0 - 1.0 / 4.0 + 6.0
# 3.0 + 2.0 + 1.0 - 5.0 + modulo remainder of 0 - 1.0 / 4.0 + 6.0
# 3.0 + 2.0 + 1.0 - 5.0 + 0 - 1.0 / 4.0 + 6.0
# 3.0 + 2.0 + 1.0 - 5.0 + 0 - 0.25 + 6.0
# 5.0 + 1.0 - 5.0 + 0 - 0.25 + 6.0
# 6.0 - 5.0 + 0 - 0.25 + 6.0
# 1.0 + 0 - 0.25 + 6.0
# 1.0 - 0.25 + 6.0
# .75 + 6.0
# = 6.75

print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6
# or 7 when truncating the decimal
# 4 modulo 2 leaves a remainder of 0
# 1 divided by 4 results in 0.25; truncated to 0
# therefore:
# 3 + 2 + 1 - 5 + 0 - 0 + 6
# 5 + 1 - 5 + 0 - 0 + 6
# 6 - 5 + 0 - 0 + 6
# 1 + 0 - 0 + 6
# 1 - 0 + 6
# 1 + 6 = 7

print "Is it true that 3 + 2 < 5 - 7?"

print 3 + 2 < 5 - 7

print "What is 3+ 2?", 3 + 2
print "What is 5 - 7?", 5 - 7

print "Oh, that's why it's False."

print "Is it greater?", 5 > -2
print "Is it greater or equal?", 5 >=-2
print "Is it less or equal?", 5<= -2