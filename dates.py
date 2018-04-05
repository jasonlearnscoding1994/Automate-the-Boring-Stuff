#! python3
# dates.py - Finds dates in different formats (such as 14/3/2015, 14-03-2015, and 2015/3/14)
# and replace them with dates in a single, standard format dd/mm/yyyy.

import pyperclip, re

# url regex.
urlRegex = re.compile(r'''(
    (\d+){1,4}                       
    (\/|\-|.)
    (\d+){1,2}                         
    (\/|\-|.)
    (\d+){1,4}                  
    )''', re.VERBOSE)

# Find matches in clipboard text.
text = str(pyperclip.paste())
matches = []
# Check length of groups to determine whether it is year or month/date.
# First and last group are checked because dates are either writen yyyy/mm/dd or dd/mm/yyyy
for groups in urlRegex.findall(text):
    if len(groups[1]) >= 4: 
        year = groups[1]
        month = groups[3]
        day = groups[5]
    elif len(groups[5]) >= 4: 
        year = groups[5]
        month = groups[3]
        day = groups[1]
        if int(groups[3]) > 12: # Check whether format on clipboard is month-day-year 
            day = groups[3]
            month = groups[1]
    dates = '/'.join([day, month, year])
    dates2 = '/'.join([day, month, year[2:]]) # Shorten year from 20XX to XX.
    matches.append(dates)
    matches.append(dates2)
    
# Copy results to the clipboard.
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No dates.')

# Comments:
# - # The code does not always work for month-day-year format for example:
#   3/12/2015 will not print 12/3/2015 but 3/14/2015 will print 14/3/2015.
