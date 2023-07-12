#Dictioanries 
myDog = {'size' : 'skinny', 'color' : 'Golden brown', 'disposition': 'loud' }
myDog['size']
print('My dog has ' + myDog['color'] + ' fur.')        
print(list(myDog.keys()))
print(list(myDog.values()))

for v in myDog.values():
    print(v)
    
for k in myDog.keys():
   print(k) 
   
print(myDog.get('size', 0))#here zero is added if there is no key named size it will return zero.

myDog.setdefault('age', '5')
print(myDog)

