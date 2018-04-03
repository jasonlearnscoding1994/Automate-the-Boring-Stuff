#! python3
# https.py - Finds website URLs that begin with http:// or https:// from clipboard
# and list them out. Code was initially used to search for phone numbers and email
# addresses.

import pyperclip, re

# https regex.
urlRegex = re.compile(r'''(
    ([http(s)?]+://)                        # Find lines containing http(s)://
    ([a-zA-Z0-9.])+                         # and get domain name (i.e www.google.com)
    ([\w.,@?^=%&:/~+#-]*)?                  # and get everything after domain name
    )''', re.VERBOSE)

# Find matches in clipboard text.
text = str(pyperclip.paste())
matches = []
for groups in urlRegex.findall(text):
    matches.append(groups[0])
    
# Copy results to the clipboard.
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No URLs found.')

# Comments:
# - Had difficulties getting characters after domain name and to exclude unwanted
#   special characters at end of url.
# - Initially used (.*) to grab everthing after https://, which also included paragraphs
#   after url.
