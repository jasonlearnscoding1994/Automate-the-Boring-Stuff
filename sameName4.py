# Example from Chapter 3, testing global variables.
# Code tests the use of a local variable in a function before assigning a value to it.
# The end result is an error because there is an assignment statement for eggs in spam()
# and therefore considers eggs local to the function.


def spam():
    print(eggs)
    eggs = 'spam local'
    
    
eggs = 'global'
spam()
