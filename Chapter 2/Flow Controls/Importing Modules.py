""" 
>>> Importing Modules
All Python programs can call a basic set of functions called built-in functions,
including the print(), input(), and len() functions you’ve seen before. Python
also comes with a set of modules called the standard library. Each module
is a Python program that contains a related group of functions that can be
embedded in your programs. For example, the math module has mathematicsrelated
functions, the random module has random number–related functions,
and so on.
Before you can use the functions in a module, you must import the
module with an import statement. In code, an import statement consists of
the following:
• The import keyword
• The name of the module
• Optionally, more module names, as long as they are separated by
commas
Once you import a module, you can use all the cool functions of that
module. Let’s give it a try with the random module, which will give us access
to the random.ranint() function.

"""
import random
for i in range(5):
   print(random.randint(1,20))
   #this will print 5 random numbers between 1 - 20.
   