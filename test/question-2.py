'''
question-2.py - Michael Bateman
Python Coding Bat Test - ICS3U
Feb 16/17
'''

# imports - none

# functions

def sortaSum(int_a, int_b): # this creates a function called 'sortaSum' that can recieve data
	totalsum = int_a + int_b # this creates the sum stored in a variable called 'totalsum'
	if ((10 <= totalsum <= 19) == True): # this checks to see if the total sum is between 10 and 19 (inclusive).
		return 20 # if it is between 10 and 19, it just returns 20
	else:
		return totalsum # if it is not between 10 and 19 it returns to real sum

# user input

int_a = input("Please enter your first number: ") # here, the user will input a number that is stored in 'int_a'
int_b = input("Please enter your second number: ") # then, a second number is asked and it is stored in 'int_b'
# both 'int_a' and 'int_b' data types are int's

# raw code

print(sortaSum(int_a, int_b)) # prints what is returned in in the 'sortaSum' function
