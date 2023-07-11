""" 
A list is a value that contains multiple values in an ordered sequence. The
term list value refers to the list itself (which is a value that can be stored in a
variable or passed to a function like any other value), not the values inside
the list value. A list value looks like this: ['cat', 'bat', 'rat', 'elephant'].
"""
pets = ['cat','dog','horse','rabbit']
print(pets)
print(len(pets))
print(pets[1])
print(pets[3])
#Slice
pets[1:4]
pets[2] = "mouse"
print(pets)
#del() function
pets = ['cat','dog','horse','rabbit']
del pets[2] 
print(pets)
#len function
pets = ['cat','dog','horse','rabbit']
print(len(pets))
#list function
name = 'Nithin'
print(list(name))


pets_and_wildani = [['cat','dog','rabbit','horse'],['lion','tiger','cheetah','python']]
print(pets_and_wildani[1])
print(pets_and_wildani[0][0])
print(pets_and_wildani[1][-2])
print('The ' +pets_and_wildani[0][0]+ ' is afraid of '+pets_and_wildani[0][1]+'!')