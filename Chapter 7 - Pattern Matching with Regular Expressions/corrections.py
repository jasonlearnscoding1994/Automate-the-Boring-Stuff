#python3
# corrections.py - Finds typos such as multiple spaces between words, consecutively repeated words, and multiple punctuations at the end of sentences.
import pyperclip, re    # import pyperclip and regex.

# correction regex.
correctionRegex = re.compile(r'''(
    (\(?[a-zA-Z0-9]\)?.*)                # Use greedy format to get everything in a sentence and to start with a letter or number. Open and close brackets are optional.
    )''', re.VERBOSE)

# Find matches in clipboard text.
text = str(pyperclip.paste())
matches = []
for groups in correctionRegex.findall(text):
    matches.append(groups[0])

def correction(sentence): # Function used to correct typos in a sentence.
    fragment = sentence.split() # Split sentence into a list with words.
    punctuations = [',','.','?','!','-','*','#']
    new = []    # Empty list to store words again after looping through.
    for words in range(len(fragment)):  # Loop through list of words.
        if (fragment[words] != fragment[words-1]):              # If the next word in sentence is not a repeat,
            new.append(fragment[words])                         # append to new list.
            complete = ' '.join(new)                            # Then join together to make a complete sentence.
    for words in new:                                           # Loop through new list of words from before.
        for symbols in range(len(punctuations)):                # And loop through list of punctuations.
            if punctuations[symbols] in words:                  # If punctuation(s) are found after a word,
                words2 = words.rstrip(punctuations[symbols])    # strip the punctuation and its repeating ones
                correct = words2 + punctuations[symbols]        # and add only one similar punctuation to the end of the words.
                complete2 = complete.replace(words, correct)    # Replace the words in the completed sentence with the words with new punctuations.
                return(complete2)                               # Return this complete sentence with correct punctuations and words.
            else:
                return(complete)                                # If not punctuations detected in sentence, return the initial completed sentence.
    
# Copy results to the clipboard.
if len(matches) > 0:
    pyperclip.copy(''.join(matches))
    sentence = ''.join(matches)
    print('Copied to clipboard:')
    print(correction(sentence)) # Print the corrected sentence after passing it through the correction function.
else:
    print('No sentences.')

## Comments:
## Typo example: Find common typos such as       multiple spaces between words, accidentally accidentally repeated words, or multiple multiple exclamation marks at the end of sentences. Those are annoying!!
## The code will have trouble correcting typos in dates (i.e. 04/    03/1999) and subsequent caps (i.e. Once Upon A Time) in a sentence.

