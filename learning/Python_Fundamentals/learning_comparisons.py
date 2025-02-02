# The purpose of this script is to create functions that compare items in one list
# with items in another list. 
# Each List references a Dictionary with Key Value pairs that are spans in  a document. 

# I will create two test dictionaries and lists to create the implementation. 

# Test Dictionary 1
dict_01 = {'Approved Permits : ':10, 'Redrilled Permits : ':20, 'New Permits : ':30, 'Plugged Permits : ':40, 'Dry Holes : ':50}
dict_02 = {'#12345': 11, '#12346': 21, '#12347': 31, '#12348': 41, '#12349': 51}

# Lists that are generated from the dictionaries
list_01 = list(dict_01.keys())
list_02 = list(dict_02.keys())

# print the lists one at a time for review
print(list_01)
print(list_02)

# Determine if item in list 01 is in the dictionary 01
# If it is in the dictionary, print the item and the value
# If it is not in the dictionary, print the item and a message that it is not in the dictionary
for item in list_01:
    if item in dict_01:
        print(item, dict_01[item], 'is in the dictionary')
    else:
        print(item, 'is not in the dictionary')

# Determine if item in list 02 is in the dictionary 02
# If it is in the dictionary, print the item and the value
# If it is not in the dictionary, print the item and a message that it is not in the dictionary
for item in list_02:
    if item in dict_02:
        print(item, dict_02[item], 'is in the dictionary')
    else:
        print(item, 'is not in the dictionary')

# Iterate over Items in list 02 and compare them to the values of each item in dictionary 01 to determine if they are greater or less then the value of each key in dictionary 01. 
# If the value of the item in list 02 is greater than the value of the item in dictionary 01, print the item in list 02 and the value of the item in dictionary 01
# If the value of the item in list 02 is less than the value of the item in dictionary 01, print the item in list 02 and the value of the item in dictionary 01
# If the value of the item in list 02 is equal to the value of the item in dictionary 01, print the item in list 02 and the value of the item in dictionary 01
for item in list_02:
    for key, value in dict_01.items():
        if dict_02[item] > value:
            print(item, dict_02[item], 'is greater than', key, value)
        elif dict_02[item] < value:
            print(item, dict_02[item], 'is less than', key, value)
        else:
            print(item, dict_02[item], 'is equal to', key, value)

