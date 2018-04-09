# Automate-the-Boring-Stuff
Examples and exercises from the book Automate the Boring Stuff. README is used for keeping random notes.

CollatzSequence.py:
- Wrote Collatz Sequence from Chapter 3 practical project to recalculate user input until the number one is returned.
- Implemented try and except clauses into a Collatz Sequence to check whether user input is an integer.

https.py:
- Wrote https.py to find URLs in sentences, paragraphs, webpages using REGEX re.compile.
- URL is split into three parts which are: https://, domain name (www.google.com), and the rest of the URL containing special characters.
- The PYPERCLIP package is used to collect information from clipboard via CTRL+C 

corrections.py:
- Wrote corrections.py to correct typos in a sentence; typos are limited to extra spacing, accidentally repeated words, and multiple punctuation marks.
- It uses REGEX and PYPERCLIP packages.
- Sentence is passed through a function that splits it into a list. For loops were used to check whether words and punctuation marks were repeated. Extra spacing were removed using ' '.join().
