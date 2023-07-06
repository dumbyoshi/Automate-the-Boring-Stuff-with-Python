"""Flow control statements often start with a part called the condition, and all
are followed by a block of code called the clause.
>>>Conditions
The Boolean expressions you’ve seen so far could all be considered conditions,
which are the same thing as expressions; condition is just a more
specific name in the context of flow control statements. Conditions always
evaluate down to a Boolean value, True or False. A flow control statement
decides what to do based on whether its condition is True or False, and
almost every flow control statement uses a condition.

>>> Blocks of Code
Lines of Python code can be grouped together in blocks. You can tell when a
block begins and ends from the indentation of the lines of code. There are
three rules for blocks.
1. Blocks begin when the indentation increases.
2. Blocks can contain other blocks.
3. Blocks end when the indentation decreases to zero or to a containing
block’s indentation.
Blocks are easier to understand by looking at some indented code, so
let’s find the blocks in part of a small game program, shown here:
"""
from os import name
if name == 'Nithin':
    print('Hello Nithin')

"""
All flow control statements end with a colon and are followed by a
new block of code (the clause). This if statement’s clause is the block with
print('Hello Nithin.').
"""
"""
>>> else Statements
An if clause can optionally be followed by an else statement. The else clause
is executed only when the if statement’s condition is False. In plain English,
an else statement could be read as, “If this condition is true, execute this
code. Or else, execute that code.” An else statement doesn’t have a condition,
and in code, an else statement always consists of the following:
• The else keyword
• A colon
• Starting on the next line, an indented block of code (called the else
clause)
"""

name = input()
if name == 'Nithin':
    print('Hello Nithin')
else:
   print('Looks like a Stranger!!!')
   
""" 
>>> elif statements
While only one of the if or else clauses will execute, you may have a case
where you want one of many possible clauses to execute. The elif statement
is an “else if” statement that always follows an if or another elif statement.
It provides another condition that is checked only if any of the previous conditions
were False. In code, an elif statement always consists of the following:
• The elif keyword
• A condition (that is, an expression that evaluates to True or False)
• A colon
• Starting on the next line, an indented block of code (called the elif
clause)
Let’s add an elif to the name checker to see this statement in action.

"""
from os import name
name = input()
age = int(input())
if name == 'Nithin':
   print('Hello Nithin')  
elif age < 12:
   print('You are not Nithin, kiddo.')
"""
>>> while Loop Statements
You can make a block of code execute over and over again with a while statement.
The code in a while clause will be executed as long as the while statement’s
condition is True. In code, a while statement always consists of the
following:
• The while keyword
• A condition (that is, an expression that evaluates to True or False)
• A colon
• Starting on the next line, an indented block of code (called the while
clause)
>>> You can see that a while statement looks similar to an if statement. The
difference is in how they behave. At the end of an if clause, the program
execution continues after the if statement. But at the end of a while clause,
the program execution jumps back to the start of the while statement. The
while clause is often called the while loop or just the loop.

"""
eggs = int(input())
while eggs < 12:
   print('Hello Nithin')
   eggs =  eggs + 1
   print(eggs)
   
""" 
>>>break Statements
There is a shortcut to getting the program execution to break out of a while
loop’s clause early. If the execution reaches a break statement, it immediately
exits the while loop’s clause. In code, a break statement simply contains
the break keyword.
"""
while True:
   print('Please type your name.')
   name = str(input())
   if name == 'Nithin':
      break
print('Thank You!')

""" 
>>> continue Statements
Like break statements, continue statements are used inside loops. When the
program execution reaches a continue statement, the program execution
immediately jumps back to the start of the loop and reevaluates the loop’s
condition. (This is also what happens when the execution reaches the end
of the loop.)

"""
#--------------------------------------------------------------------
while True:
   print('Who are you?')
   name = input()
   if name != 'Nithin':
       continue
   print('Hello, Joe. What is the password? (It is a fish.)')
   password = input()
   if password == 'swordfish':
         break
print('Access granted.')
#------------------------------------------------------------------
while True:
   print('Who are you?')
   mood = input()
   if mood != 'How are you?':
      continue
   print("I'm fine, thanks. Who are you?")
   name = input()
   if name != 'Nithin':
       continue
   print('Hell0 Nithin, What is the password?')
   password = str(input())
   if password == 'shark':
         break
print('Access granted.')
""" 
>>> Range() Function
The while loop keeps looping while its condition is True (which is the reason
for its name), but what if you want to execute a block of code only a certain
number of times? You can do this with a for loop statement and the range()
function.
"""
print('My name is')
for i in range(5):
   print('Nithin five time ' + str(r))
#---------------------------------------------------------------
total = 0
for num in range(101):
   total = total + num
print(total)
#---------------------------------------------------------------
for i in range(1,10):
   print(i)
   
#---------------------------------------------------------------
for i in range(0,10,3):
     print(i)

