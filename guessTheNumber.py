# This is a guess the number game from Chapter 3.
# The code uses the random module to generate a number between 1 to 20 and is stored in variable secretNumber.

import random
secretNumber = random.randint(1,20)
print('I am thinking of a number between 1 and 20.')

# Ask the player to guess 6 times.
for guessesTaken in range(1,7):
    print('Take a guess.')
    guess = int(input())

# Check to see if number input is less or greater than secretNumber.
    if guess < secretNumber: # If number is less, give hint it is low.
        print('Your guess is too low.')
    elif guess > secretNumber: # If number is more, give hint it is high.
        print('Your guess is too high.')
    else: 
        break # If number is guess correctly, then this condition is the correct guess

# 
if guess == secretNumber:
    print('Good job! You guessed my number in ' + str(guessesTaken) + ' guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber))
    
