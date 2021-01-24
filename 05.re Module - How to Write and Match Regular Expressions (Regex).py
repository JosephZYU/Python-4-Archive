"""

NOTE:

    🧭 backward slash is the real-deal!

    \ -> "escape"


"""


import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

coreyms.com

321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''

sentence = 'Start a sentence and then bring it to an end'

# Backslash \t -> tab
# 🧠 '\t'

print('\tTab')

# r -> raw string
# 🧠 r'string'
print(r'\tTab')

# Create pattern: raw string mast to be EXACT match
pattern = re.compile(r'.')

# Match pattern
matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)

print(text_to_search[1:4])
print(text_to_search[28:31])
print(text_to_search[142:153])


"""
# 🎯 https://stackoverflow.com/a/1548720/15063197

import os, re

def purge(dir, pattern):
    for f in os.listdir(dir):
        if re.search(pattern, f):
            os.remove(os.path.join(dir, f))

"""
