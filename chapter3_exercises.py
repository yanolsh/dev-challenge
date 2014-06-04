# Exercises for chapter 3:

# Name:Yan Olshevskyy
'''
Exercise 3.1.
Move the last line of this program to the top, so the function call appears before the definitions. 
Run the program and see what error message you get.

Traceback (most recent call last):
  File "chapter3code.py", line 6, in <module>
    repeat_lyrics()
NameError: name 'repeat_lyrics' is not defined
'''


'''
Exercise 3-2.
Move the function call back to the bottom and move the definition of print_lyrics after the definition of repeat_lyrics. 
What happens when you run this program?

I'm a lumberjack, and I'm okay.
I sleep all night and I work all day.
I'm a lumberjack, and I'm okay.
I sleep all night and I work all day.

'''

'''

Exercise 3.3.
Python provides a built-in function called len that returns the length of a string, so
the value of len('allen') is 5.
Write a function named right_justify that takes a string named s as a parameter and prints the string with enough leading spaces 
so that the last letter of the string is in column 70 of the display.


def right_justify(s):
	numspaces = 70 - len(s)
	print ' ' * numspaces + s

right_justify('allen')

'''