#Funtions
def hello():
   print('Hallo')
   print('Wie gehts?')
   print('Hallo Hallo Hallo')
hello()
hello()
hello()

#def Statements with Parameters
def hello(name):
   print('Hallo ' + name)
   
hello('Nithin')
hello('Krishnan')
""" 
>>> Return Values and return Statements
When creating a function using the def statement, you can specify what
the return value should be with a return statement. A return statement consists
of the following:
• The return keyword
• The value or expression that the function should return
When an expression is used with a return statement, the return value
is what this expression evaluates to. For example, the following program
defines a function that returns a different string depending on what number
it is passed as an argument.
"""
def plusone(number):
   return number + 1
newno = plusone(7)
print(newno)

""" 
>>> Keyword Arguments and print()
Most arguments are identified by their position in the function call. For
example, random.randint(1, 10) is different from random.randint(10, 1). The
function call random.randint(1, 10) will return a random integer between 1
and 10, because the first argument is the low end of the range and the second
argument is the high end (while random.randint(10, 1) causes an error).However, keyword arguments are identified by the keyword put before
them in the function call. Keyword arguments are often used for optional
parameters. For example, the print() function has the optional parameters
end and sep to specify what should be printed at the end of its arguments
and between its arguments (separating them), respectively.

"""
print('Hello')
print('World')
#the above two print statements will print in two lines
print('Hello' , end = ' ')
print('World')
#the above two print statements will print in one line
print('cats', 'dogs', 'mice', sep=',')
