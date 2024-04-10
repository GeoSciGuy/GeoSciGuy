# Content here comes from the Automate the Boring Stuff online. 
myCat = {'size': 'fat' , 'color': 'gray' , 'disposition': 'loud'}

print(myCat['size'])
print('My cat has ' + myCat['color'] + ' fur.')

birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == '':
        break

if name in birthdays:
    print(birthdays[name] + ' is the birthday of ' + name)
else:
    print('I do not have birthday information for ' + name)
    print('What is their birthday?')
    bday = input()
    birthdays[name] = bday
    print('Birthday database updated.')

# for loop iterating over each of the values in the spam dictionary
spam = {'color': 'red', 'age': 42}
for v in spam.values():
    print(v)

for k in spam.keys():
    print(k)

for i in spam.items():
    print(i)

# Using the in and not in keywords. 
spam = {'name': 'Zophie', 'age': 7}
'name' in spam.keys()
'Zophie' in spam.values()
'color' in spam.keys()
'color' not in spam.keys()
'color' in spam

