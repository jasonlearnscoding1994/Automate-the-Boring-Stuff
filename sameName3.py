# Example from Chapter 3, testing global variables.

def spam():
    global eggs
    eggs = 'spam'

def bacon():
    eggs = 'bacon'

def ham():
    print(eggs)


eggs = 42
spam()
bacon()
print(eggs)
