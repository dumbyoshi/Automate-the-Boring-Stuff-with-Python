#guessing the number python program

import random

print('Hello, what is your name?')
name = input()
print("Oh Hi " + name + " I am thinking of a number between 1 and 10")
secretnum = random.randint(1,20)

for guesstaken in range(1,4):
   print('Take a guess')
   guess = int(input())
   
   if guess < secretnum:
      print('Your guess is too low')
   elif guess > secretnum:
    print('Your guess is too high')
   else:
       break

if guess == secretnum:
   print('Good job ' + name + ' you guessed my number in ' + str(guesstaken) + ' guesses!')
else:
   print('Nope. The number I was thinking of was ' + str(secretnum))

print('Thanks for playing! Bye Bye '+ name)