"""
Part 1 - Python Programming Basics
Chapter 1 - Python Basics (Automate the Boring Stuff with Python)
Install Python latest version from https://www.python.org/downloads/ , click on the yellow box which contain the latest version of Python.
Launch the Python IDLE or Powershell or Command Prompt and type "python --version" to check the version of Python installed.
Python is an interpreted language, which means that programs written in Python need not be compiled before running.
In Python, 2 + 2 is called an expression, which is the most basic kind of
programming instruction in the language. Expressions consist of values
(such as 2) and operators (such as +), and they can always evaluate (that is,
reduce) down to a single value. That means you can use expressions anywhere
in Python code that you could also use a value.
In the previous example, 2 + 2 is evaluated down to a single value, 4.
A single value with no operators is also considered an expression, though
it evaluates only to itself, as shown here:
>>>2+2
4
>>>2
2
There are plenty of other operators you can use in Python expressions,
too. For example, Table 1-1 lists all the math operators in Python.
>>>2+3*6
20
>>>(2 + 3) * 6
30
"""
""" 
Integer , Float and String Data Types
Integers(int) = -2 , 1 , 0 etc
Floating point numbers(float) = 1.25 , 6.01 , 4.00001 etc
String(str) - 'string' , 'nitin' , 'py' etc 
>>> 'Hello World! 
this line will execute a error which is called a syntax error coz there is no closing final quote.
"""
#String Concatenation and Replication
myname = 'Nithin'
print('My name is ' + myname)
#print function prints the value of the variable or anything that is passed to it.
myfullname = myname + 'Krishnan'
print(myfullname)

spam = 40
eggs = 2
print(spam + eggs)

"""
A variable is initialized (or created) the first time a value is stored in it u.
After that, you can use it in expressions with other variables and values v.
When a variable is assigned a new value w, the old value is forgotten, which
is why spam evaluated to 42 instead of 40 at the end of the example. This is
called overwriting the variable. Enter the following code into the interactive
shell to try overwriting a string:
"""
name = 'Nithin'
print(name)
name = 'Krishnan'
print(name)
"""
1. It can be only one word.
2. It can use only letters, numbers, and the underscore (_) character.
3. It can’t begin with a number.
"""
#My First Program
print('Hello World!')
print('What is your Name?')
myName = input()
# input() function waits for the user to type some text on the keyboard and press ENTER and the value is stored in myName variable.
print('Hallo ' + myName)
print('The lenght of your name is:')
print(len(myName))
# len() prints the length of the string
print('Whats your Age?')
myAge = input()
print('Oh so you will be ' + str(int(myAge) + 1) + ' in a year.')
# here myAge is converted into integer and then added with 1 and then converted into string and then concatenated with the string.