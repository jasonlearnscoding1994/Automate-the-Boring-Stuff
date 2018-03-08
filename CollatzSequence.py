# This code is written to run the collatz sequence from Chapter 3.
# The program will keep calling the user integer input until the function collatz returns the value 1.

print('Please enter a number: ')
while True:
    try:
        integer = int(input())
        break
    except ValueError:
        print('Invalid input. Please enter an integer.')

# Function for calculating whether a number is even or odd.
def collatz(number):
    if number % 2 == 0: # If remainder is zero
        return(number // 2)
    elif number % 2 == 1: # If remainder is not zero.
        return(3 * number + 1)

# Loop for storing the new number every calculation.
while True:
    store = collatz(integer)
    integer = store
    print(integer)
    if integer == 1:
        print('You have reached 1.')
        break
    else:
        continue

          
