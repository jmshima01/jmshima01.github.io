# This is a comment you can write any thing you want here
# Name: James Shima
# Purpose of this python program: show some basic examples

"""
This is a multi line comment
I can write comments on multiple lines without using a #
everytime!
"""

# if you want to comment out a peace of your code (program),
# highlight it, hold CONTROL and / to comment it out and repeat to undo


# to undo a change(s) hold CONTROL and press z 


# ================ TYPES ===================

x = 5 # this is a INTEGER aka a whole number (we will call it an Integer in this class)

x = 5.1 # this is a FLOAT aka a number with a decimal place

x = "Hello" # this is a STRING, which is data that holds letters or keyboard CHARACTERS as they appear in the quotes
# You can tell this is a string due to the quotes "" around it
# you can also use '' single quotes to make a string but I like the double quotes for a string and '' for a string with just
# one letter aka a CHAR

x = 'A' # this is a STRING as well but more formally called a CHAR.  A string is a group/multiple CHARs or keyboard characters

x = [] # this is a LIST, it can hold multiple variables/types or items for you. This one is empty
x = [5, 5.1, "Hello", 'A', 0, 3.14] # they are usefull for storing groups of things in one place

x = True # This is a Boolean aka a True or False value
x = False 

x = None # like it say this is a variable holding a value/type of nothing

x = float("infinity") # trick if you need infinity

x = input("Enter your name> ") # this is the input function, it takes input from the user and stores it in x
# the string "Enter your name> " is a custom prompt for the user to see what to input, it is also generally called
# a parameter, more on this and functions later...

print("Hello World") # this is the print function, it takes in anything and outputs it to the user to see

print(x) # printing a variable

print(f"The user put in {x}") # this is print with an f string. f strings allow you to put variables or expresions
# inside a string for example f"The value of 2+2 is {2+2}" --> The value of 2+2 is 4 
print(f"The value of 2+2 is {2+2}") # --> The value of 2+2 is 4

x = "3.3" # is this a float or a string?

x = float("3.3") # what about now

x = "5" # is x a string or an int?

x = int("5") # what about now?


# ever unsure of what type something is?
print(type(x))


x = x + 1 # How is this possible???

# = does not mean equals! it means assign a new value to the left hand side.
# so this is assigning x to be what x is currently, but with one added to it
# so if x is initally 5, then x = x+1, would make x now be 6 as x = x-->(5) + 1 is 6

# WE WILL USE THIS TRICK A LOT SO DON'T MIX THIS UP


# what's e? SCIENTIFIC NOTATION!
x = 1e3 # scientific notation (USEFUL for your first assignment)
x = 5.2e11 # 520000000000.0 lot nicer than writing all those zeros!
# 1e3 means 1 * 10^3 = 1000
# CAREFUL this give you a float and not an int so use the x = int(x) statement if needed










# Conditionals


# How can I tell if a number is even or odd?
if (x % 2 == 0):
    print(f"{x} is Even")
else:
    print(f"{x} is Odd")
    
# Alternatively 
if (x & 1 == 0): # more on this later when we talk about binary!
    print(f"{x} is Even")
else:
    print(f"{x} is Odd")