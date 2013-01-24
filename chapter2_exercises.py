# Exercises for chapter 2: Problems 2.1, 2.2, 2.3, and 2.4 in Think Python

# Name: Juliana Nazare

# Name:

print "Chapter 2 Excercises"

print "\nProblem 2.1"
print "It is reading it in octal"


print "\nProblem 2.2"
print 5
x = 5
print x
x = x + 1
print x

print "\n\nProblem 2.3"
width = 17
height = 12.0
delimiter = '.'

one = width / 2 #int
print "#1: int -- " + str(one)
two = width / 2.0 # float
print "#2: float -- " + str(two)
three = height / 3 # float
print "#3: float -- " + str(three)
four = 1 + 2 * 5 # int
print "#4: int -- " + str(four)
five = delimiter * 5 # string
print "#5: string -- " + str(five) 


print "\nProblem 2.4"
print "\nPart 1"
r = 5.0
v = 4.0/3.0*3.14*r**3.0
print v

print "\nPart 2"
t = 24.95 * (1-0.4) * 60 + 3 + 59 * .75
print t

print "\nPart 3"
hr = 6
minute = 52
sec = 0
minute = minute + 8 + 7 * 3
sec = 15 + 12 * 3
if (sec >= 60):
	minute = minute + 1
	sec = sec - 60
if (minute >= 60):
	hr = hr + 1
	minute = minute - 60
print str(hr) + ":" + str(minute) + ":" + str(sec)

