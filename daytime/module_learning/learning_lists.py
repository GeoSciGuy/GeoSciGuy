# List - a value that contains multiple values in an orded sequence. 
# List Value - referes to the list itself, which can be stored
## in a variable or passed to a function like any other value, 
## not the values inside the list value. 
# example list
example_list = [1,2,3]
another_list = ['cat','bat','rat','elephant']
yet_another_list = ['hello',3.1415, True, None, 42]
print(example_list)

spam = another_list

# Get a value with the List Index
spam[0]
print(spam[0]) # Should print cat
print(spam[1]) # Should print bat
print('Hello, ' + spam[0])

# Lists can contain other lists. 
print("Changing the value of Spam now")
spam = [['cat','bat'],[10,20,30,40,50]]
print(spam[0])
print(spam[0][1])
print(spam[1][4])
print("The last three outputs illustrated a list within a list")

# Use a negative index to begin at the EOF and work backward. 
print(spam[-1])

# Get a list from another List
# Using a SLICE
print("Changing Spam back to the another list")
spam = another_list
print(spam)
print(another_list)
# a SLICE is typed between sqaure brackets, like an index, but it has two integers sep by a colon. 
## spam[2] vs spam[1:4]
## You can use a short hand by leaving out the left or right number. Left will be the same as 0,
## and right omission is the same as length of list, which will slice to the end. 
print(spam[2])
print(spam[1:4])
print(spam[:2])
print(spam[:])
print('the legnth of the list is: ',  + len(spam))

print(" Slice Exmple Complete")



# Change a value in a list with an assigment statement and index. 
print(spam)
print('changing the value of spam at interval position 1' + "'spam[1]='aardvark'")
spam[1] = 'aardvark'
print(spam)
print('bat should now be aardvark')

# List concatenation and List Replication
# Lists can be combined with + , * operator can be used with a list and an integer to replicate the list
list_A = [1,2,3]
list_B = ["A","B","C"]
combined_lists = list_A + list_B
print(list_A)
print(list_B)
print("Created with the + sign : " , combined_lists)

# Remove things from lists with the del statement. 
print(spam)
print("Demonstrating removeing an item from a list with an index call, del spam[2]")
del spam[2]
print(spam)

# Example program using catnames. 
catNames = []
while True:
    print('Enter the name of cat ' + str(len(catNames) + 1) +
      ' (Or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    catNames = catNames + [name]  # list concatenation
print('The cat names are:')
for name in catNames:
    print('  ' + name)

# using a for loop with lists
print(" looping with lists")
supplies = ['pens', 'staplers', 'flamethrowers', 'binders']
print(supplies)
for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])

# The in and not in operators
# checking to see if something is in  a list. 
howdy_list =  ['hello', 'hi', 'howdy', 'heyas']
'howdy' in howdy_list # should return True
'howdy' not in howdy_list # should return False

# Multiple Assignment Trick
# Tuple Unpacking - also known as. 
#instead of this....
cat = ['fat', 'gray', 'loud']
size = cat[0]
color = cat[1]
disposition = cat[2]

# you can do this
cat = ['fat', 'gray', 'loud']
size, color, disposition = cat

# the num of varialbles must match the legnth of the list exactly, else value error will occur
# tuples - like a list but cannot be modified, have to be deleted and recreated. 
# These are typically faster. 
# Mutable = can be modified
# immutable = cannot be changed, strings and tuples
type(('hello',))
type(('hello'))

# Create a a list and a tuple with the data being passed with the functions
# list() or tuple()
tuple(['cat','dog',5])
list(('cat','dpg',5))
list('hello')


