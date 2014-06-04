# Exercises for chapter 2:

# Name:Yan Olshevskyy
'''
Exercise 2-1

01=1
010=8
0100=64
01000=512
The results are represented by base 8 number system
02132 = (2*512) + (1*64) + (3*8) + (2*1) which is  1114.
'''
'''
Exercise 2-2.
Type the following statements in the Python interpreter to see what they do:
5 
x= 5
x+ 1
Now put the same statements into a script and run it. What is the output? 
Modify the script by transforming each expression into a 
print statement and then run it again.


Theres is no output. With print statements the output is :
5
6
'''

'''
Exercise 2-3.
Assume that we execute the following assignment statements:
width = 17
height = 12.0
delimiter = '.'
￼Exercises | 21
For each of the following expressions, write the value of the expression and the type (of the value of the expression).
1. width/2 = 8 int
2. width/2.0 = 8.5 float
3. height/3 = 4.0 float
4. 1+2* 5 = 11 int
5. delimiter * 5 = '.....' str 

'''

'''
Exercise 2.4.

Practice using the Python interpreter as a calculator:
1. The volume of a sphere with radius r is 4/3*pi*r^3. What is the volume of a sphere with radius 5?
Hint: 392.7 is wrong!

2. Suppose the cover price of a book is $24.95, but bookstores get a 40% discount. Shipping costs $3 for the first copy and 75 cents for each additional copy. What is the total wholesale cost for 60 copies?
3. If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile), then 3 miles at tempo (7:12 per mile) and 1 mile at easy pace again, what time do I get home for breakfast?

1. 4.0/3.0*3.1415926535897932*5**3=523.5987755982989
2. discount=24.95*0.6
	copies=60
	shipping=3.00
	additionalCopy=0.75

	discount * copies * shipping +(copies -1) * additionalCopy = 945.4499999999999

3.  mile1 = 8*60+15
	mile3 = 7 * 60 + 12

	totalRun=(mile1 *2 + mile3*3)/60= 38 mins
	6:52+ 38 mins =7:30
'''

