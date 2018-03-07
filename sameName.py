# Example from Chapter 3, testing local and global variables with the same name.
# Code tests whether global variable eggs will take precedence over local variable in functions when declared.
# End result: local variable in function will always be used instead of global variable when function is called upon.
def spam():
    eggs = 'spam local'
    print(eggs)
    
def bacon():
    eggs = 'bacon local'
    print(eggs)
    spam()
    print(eggs)


eggs = 'global'
bacon()
print(eggs)
