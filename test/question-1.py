'''
question-1.py - Michael Bateman
Python Coding Bat Test - ICS3U
Feb 16/2017
'''

# imports - none

# functions

def newString(word): # creates a function called newString and recieves data
	if (len(word) < 2): # checking to see if the string is less than 2
		return (word) # if string is less than 2, it will just return the word
	else:
		first = word[:1] # this stores the first letter in the variable 'first'
		last = word[len(word)-1:] # this stores the last letter in the variable 'last'
		mid = word[1:len(word)-1] # this creates a string without the first and last letters, stored in 'mid'
		return (last + mid + first) # this will return it with the first and last letters switched

# input

word = raw_input("Please type a word: ") # this is raw_input, therefore the variable 'word' is a string

# raw code

print(newString(word)) # this prints the funtion to the screen
