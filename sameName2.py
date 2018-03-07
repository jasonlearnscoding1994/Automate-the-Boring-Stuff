# Example from Chapter 3, testing global statement in functions.
# Code tests global statement.
# End result: global variable eggs can be modified depending on order of code.

def spam():
    global eggs
    eggs = 'spam'

eggs = 'global'
spam()
print(eggs)
