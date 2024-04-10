
# Test Function to illustrate a Function:
def hello():
    print('Howdy!')
    print('Howdy!!!')
    print('Hello there.')

    # General Purpose of Functions is to package code, and call it instead of having to duplicate it. 
    # Arguments - things that go inside the calls. 

def hello(name):
    print('Hello, ' + name)

hello('Alice')
hello('Bob')

# Parameters are variables that contain arguments. 
# when a function is called with arguments, they are stored in parameters. 
# Values in Parameters are destroyed when the function returns. 

# Key Terms
# Define - to define, means to create. 
# # def statement defines the sayHello() function. 
# Call - sends request to the program to execute the function
# Pass - when the "Al" string value is passed to the function. 
# Argument - a value being passed to a function in a function call. 
# Parameter - Variables that have arguments assigned to them are parameters. 
def sayHello(name): # def statement
    print('Hello, ' + name)
sayHello('Al') # call statement

# Return Value - the end result a function call resolves to. 
import random # 1

def getAnswer(answerNumber): #2
    if answerNumber == 1: #3
        return 'It is certain'
    elif answerNumber == 2:
        return 'It is decidedly so'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'Reply hazy try again'
    elif answerNumber == 5:
        return 'Ask again later'
    elif answerNumber == 6:
        return 'Concentrate and ask again'
    elif answerNumber == 7:
        return 'My reply is no'
    elif answerNumber == 8:
        return 'Outlook not so good'
    elif answerNumber == 9:
        return 'Very doubtful'
r = random.randint(1,9) #4
fortune = getAnswer(r) #5
print(fortune) #6
# OR Write these three lines like this
print(getAnswer(random.randinit(1,9)))
#

#1 - Import Random Module
#2 - getAnswer function is defined
#3 - the random.randint() function is called with two arguments, 1 and 9. 
#4 - Random evaluates to a number between 1 and 9 and this value is stored in a variable named 'r'
#5 - the getAnswer function is called with 'r' as the argument. program executes from the top down with
## - parameter value 'r' as answerNumber. Depending on the value of r, one of several text strings is returned. 
#6 - the returned string is assigned a variable named fortune, which then gets passed to print() and is printed

# Keyword Arguments  - identified by the keyword put before them in the function call. 
# # often times keyword arguments are optional parameters. 
print("Hello")
print("World")
# or 
# using a keyword argument - #3
print('Hello', end='') #3
print('World')

# Similar Example with Seperator change
print('cats', 'dogs', 'mice')

print('cats', 'dogs', 'mice', sep=',')




