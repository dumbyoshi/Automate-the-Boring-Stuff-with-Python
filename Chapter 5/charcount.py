#program to find the number of occurance of a character in a string.

msg = 'Hello this is Nithin,am from India'
count = {}
for character in msg.lower():
   count.setdefault(character, 0)
   count[character] = count[character] + 1

print(count)
   