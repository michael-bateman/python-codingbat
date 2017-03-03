# Python - Coding Bat Solutions
*Unofficial answers to Python Coding Bat solutions for `String-1`,`Logic-1` and `Warmup-1` problems*

The problems can be found here: http://codingbat.com/python

## About
I made these solutions while studying for my grade 9 computer science test.  These instructions can be useful to those who are trying the `String-1` and `Logic-1` problems since they do not come with answers.

I have both my solutions for the test, and they can be found in the `test` folder.

*Please note this project will no longer be updated with more content, only bug fixes will occur*

## Setup Instructions

It is very easy to get these things up and running on your machine.  Most people will not even want to run these, but instead see the solutions to them.

### Viewing Solutions

Well, that's easy, just open the folder that is the problem set name.  Then click the solution you want to use.

__Note:__ *If you are using Coding Bat's online interface, please follow the instructions below.*

Suppose, the following is shown below, only take the function, so everything from line 1-5 should be put in the online interface.

```python
def monkey_trouble(a_smile, b_smile):
  if(a_smile == "yes" and b_smile == "yes" or a_smile == "no" and b_smile == "no"):
    return True
  else:
    return False

a_smile = raw_input("Is a smiling? (yes or no) ")
b_smile = raw_input("Is b smiling? (yes or no) ")

print(monkey_trouble(a_smile,b_smile))
```

### Downloading the Repository

Press the green, `Clone or download` button on the top of the repository.  Then click `Download ZIP`.  You then can run the `.py` files regularly.  For example, on a Mac, you can run the python files by typing:

```bash
$ python <file_name>.py
```

## Improvements
__Note:__ *All of these solutions have been tested using Coding Bat's online interface*

If you find a better solution, please fork the repository and submit a pull request or let me know via email at [info@michaelbateman.ca](mailto:info@michaelbateman.ca).  Please note - I will not be changing anything in the `test` folder, only the other files, if a better solution can be found.
