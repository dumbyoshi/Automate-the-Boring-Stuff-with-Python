name = 'puss the cat'
print(name[9])

#name[9] = 'f'
#print(name)#returns a error that the letter cant be swapped coz its a immutable string.

name = ['Nithin' , 'Krishnan' , 'Krish']
allNames = name
allNames[1] = 'K'
print(allNames)
print(name)#stores a reference of the list not the actual list.
#immutable values can be only replaced by new values not modified.
