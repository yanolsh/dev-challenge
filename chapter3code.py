'''
Code
'''

# 3-1
'''
repeat_lyrics()

def print_lyrics():
   print "I'm a lumberjack, and I'm okay."     
   print "I sleep all night and I work all day."

def repeat_lyrics():
    print_lyrics()
    print_lyrics()

'''

# 3-2
'''
def repeat_lyrics():
    print_lyrics()
    print_lyrics()


def print_lyrics():
    print "I'm a lumberjack, and I'm okay."
    print "I sleep all night and I work all day."

repeat_lyrics()
'''


#chapter 3-3
'''
def right_justify(s):
	numspaces = 70 - len(s)
	print ' ' * numspaces + s

right_justify('allen')
'''


#chapter 3-4

# 2
'''
def do_twice(f, x):
	f(x)
	f(x)

def print_spam(num):
    print 'spam' * num

do_twice(print_spam, 5)
'''

# 3

'''
def print_twice(s):
	print s
	print s

print_twice('test')
'''

# 4
'''
def do_twice(f, x):
	f(x)
	f(x)

def print_twice(s):
	print s
	print s

do_twice(print_twice, 'spam')
'''

# 5
'''
def do_twice(f, x):
	f(x)
	f(x)

def print_twice(s):
	print s
	print s

def do_four(f, x):
	do_twice(f, x)
	do_twice(f, x)

do_four(print_twice, 'spam')
'''