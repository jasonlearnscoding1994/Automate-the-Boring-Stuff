# Example from Chapter 3, testing exception handling.
# Code runs a user defined error using the try and except statements.
# This neglects the error output from P

def spam(divideBy):
    try:
        return 42/divideBy
    except ZeroDivisionError:
        print('Error: Invalid argument.')
        

print(spam(2))
print(spam(12))
print(spam(0))
print(spam (1))
