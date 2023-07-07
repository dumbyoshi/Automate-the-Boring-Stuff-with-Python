#Local and Global Variables
#Local Variables
def name():
   name = 'Nithin'#this is local variable
   print("Hello " + name)

name()
#here the variable name is a local variable and can be used only inside the function name()

#Global Variables
name = 'Krish'#this is global variable
def lname():
    print('Hello' + name)   
lname()


