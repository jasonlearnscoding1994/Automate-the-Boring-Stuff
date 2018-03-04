# Example in Chapter 2, tweaked it to include two while loops to constantly ask users for
# correct inputs (name and age) and then password. Loops break when correct inputs are received.
    
# Set Loop and Loop2 as a boolean.
Lp = True 
Lp2 = True
i = 0
n = 4
j = 0
p = 4
k = 0
    
# Use while loop Lp to determine whether an input provided by the user is correct.
# If incorrect, ask for name and age again for three more times using "i" counter and "continue" before disabling system.
# If correct, break the while loop and display message "Hello, Jason".
while Lp:
    print ("Please enter your name: ")
    name = input()
    print ("Please enter your age: ")
    age = int(input())
       
    if name != 'Jason':
        if i == 3:
            print("Sytem disabled.")
            break
        else:
            print ("User denied. Make sure name and age is correct.")
            n = n - 1
            print ("You will be locked out of the system after %d more attempt(s)." % n)
            i = i + 1
            continue
        
    elif age <= 12:
        if i == 3:
            print("Sytem disabled.")
            break
        else:
            print ("Kid, go away.")
            n = n - 1
            print ("You will be locked out of the system after %d more attempt(s)." % n)
            i = i + 1
        continue
    
    elif age >= 50:
        if i == 3:
            print("Sytem disabled.")
            break
        else:
            print ("Grandma, this isn't the TV.")
            n = n - 1
            print ("You will be locked out of the system after %d more attempt(s)." % n)
            i = i + 1
        continue
    
    elif age != 24:
        if i == 3:
            print("Sytem disabled.")
            break
        else:
            print ("User denied. Make sure username and age is correct.")
            n = n - 1
            print ("You will be locked out of the system after %d more attempt(s)." % n)
            i = i + 1
        continue
    
    else:
        print ("Hello, Jason")
        k = k + 1
        break
        
# Use while loop Lp2 to determine whether an input provided by the user is correct.
# If incorrect, display "Wrong Password" and ask for password again.
# If correct, display message and break while loop.
# If more than three additional attempts are made, Lp2 will not initialise.
while Lp2:
    if i >= 3 and k != 1:
        break
    else:
        print ("Please enter your password, %s" % name)

    password = 'swordfish'
    password = input()
    if password == 'swordfish':
        print ("Access Granted.")
        break
    elif j == 3 and password != 'swordfish':
        print("Sytem disabled.")
        break
    else:
        print ("Wrong Password.")
        p = p - 1
        print ("You will be locked out of the system after %d more attempt(s)." % p)
        j = j + 1
        continue    
            
# Comments:
# - Variable age will output an error if a string is entered instead of an integer.
#   Unsure of a way to circumvent this problem and to output a string "Age only accepts numbers.:
# - Basic authentication system.

            


           
