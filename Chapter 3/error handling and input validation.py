#Exception Handling

def spam(divdeby):
    try:
       return 50 / divdeby
    except ZeroDivisionError:
        print('Error: Invalid argument.')
        
print(int(spam(2)))
print(int(spam(5)))
print((spam(0)))
print(int(spam(1)))
