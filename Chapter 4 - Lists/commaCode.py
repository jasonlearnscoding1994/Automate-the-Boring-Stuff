# Comma Code is a practical project from Chapter 4 - Lists.
# It takes a user defined list and returns it as a structured sentence with commas and conjunction "and".
# The function splits the list into two to insert conjunction "and".

spam = ['apples', 'bananas', 'tofu', 'cats', 'guitar', 'cigarette', 'cake']

# Function for splitting list.
def sentence(words):
    line = '' # Store beginning list into a string
    line2 = '' # Store end of list into a string
    for i in range((len(words)-1)): # For each word in beginning of list until before last word in list.
        line += words[i] + ', ' # Store in line and add comma.
    for i in range((len(words)-1),(len(words))): # For word before last until end of list.
        line2 += 'and ' + words[i] # Store in line2 and add conjunction "and".
    print(line + line2) 


sentence(spam)
