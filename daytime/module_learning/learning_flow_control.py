# from How to Automate the Boring Stuff
# https://automatetheboringstuff.com/2e/chapter2/
# The idea is starting with a flow chart. 
# traversing the logic with yes and no and comparisons
# executing only the code you want to while certain conditions
# are true. 

# Boolean values
spam = True
print ( spam)

# Operators

# Operator    Meaning

# ==          Equal to
# !=          Not equal to
# <           Less than
# >           Greater than
# <=          Less than or equal to
# >=          Greater than or equal to

43 == 43

# Binary Boolean Operators
# These are "and" and "or"
# The authoer creates what are called "Truth Tables"
# These show all the possible comparisons and which will yield "True"

# if Statements Example
# The order of the If statements matters, once a True hits, the execution stops. 
if 1+1 == 2: # Some conidition evalutation yields True 
    print("Block of code")
elif 2+ 2 == 4: # Additonal statements that equal a True Response. 
    print("secondary positive statement")
else: # This code executes when the If Statement yields a False
    print("this block of code")
    pass

# While Loop Statements
# Makes a block of code execute over and over while a condition evaluates as True
while True:
    print("Please type your name")
    name = input()
    if name == 'your name' == "your name":
        break
print('Thank you!')

# Break Statements Halt execution of the loop. 
# continue statements send the execution back the beginning of the loop. 
# Reaching the end of a loop statement is the same as the continue statement in a loop
# For Loops and the Range() Function
print( 'My name is ')
for i in range(5):
    print('Jimmy Five Times(' + str(i) +')')

# EQUIVALENT to a while loop
print ('my name is')
i = 0
while i < 5:
    print('Jimmy Five Times(' + str(i) + ')')
    i = i+1


# Forcing a program to close early!
import sys

while True:
    print('Type exit to exit.')
    response = input()
    if response == 'exit':
        sys.exit()
    print('You typed ' + response + '.')


# Putting it all together! 
# This is a guess the number game. 