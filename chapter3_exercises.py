# Exercises for chapter 3: Problems 3.1, 3.2, 3.3, and 3.4 in Think Python

# Name: Juliana Nazare


print "Chapter 3"

print "\n\nProblem 3.1 and 3.2"
def repeat_lyrics():
	print_lyrics()
	print_lyrics()

def print_lyrics():
	print "I'm a lumberjack, and I'm okay."
	print "I sleep all night and I work all day"

repeat_lyrics()

print "\nThe function is not defined"
print "The script runs fine"

print "\n\nProblem 3.3"
def right_justify(s):
	spaces_to_add = 70 - len(s)
	print ' ' * spaces_to_add + s

right_justify('allen')

print "\n\nProblem 3.4"

print "\nPart 1"
def do_twice(f):
	f()
	f()

def print_spam():
	print 'spam'

do_twice(print_spam)


print "\nPart 2"
def do_twice(f, s):
	f(s)
	f(s)

def print_spam(s):
	print "spam"

do_twice(print_spam, 'yo')

print "\nPart 3"
def print_twice(s):
	print s
	print s

print_twice("whatup")

print "\nPart 4"
def do_twice(s):
	print_twice(s)
	print_twice(s)

do_twice('hi')

print "\nPart 5"
def do_four(v):
	do_twice(v)
	do_twice(v)


do_four('yooo')

