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

cat
mat
pat
bat

'''

sentence = 'Start a sentence and then bring it to an end'

# Backslash \t -> tab
# 🧠 '\t'

# print('\tTab')

# r -> raw string
# 🧠 r'string'
# print(r'\tTab')

# Create pattern: raw string mast to be EXACT match
# pattern = re.compile(r'd')

# Create pattern: use backward slash "\" to escape from raw string ⭐️
# pattern = re.compile(r'\d')
# pattern = re.compile(r'\D')
# pattern = re.compile(r'\w')
# pattern = re.compile(r'\W')
# pattern = re.compile(r'\s')
# pattern = re.compile(r'\S')

# pattern = re.compile(r'\bHa')
# pattern = re.compile(r'\BHa')

# pattern = re.compile(r'^Start')
# pattern = re.compile(r'end$')

pattern = re.compile(r'[89][0]\d[-*]\d\d\d[-*]\d\d\d\d')  # ⭐️
pattern = re.compile(r'[4-9]00.\d{3}.\d{4}')  # ⭐️

pattern = re.compile(r'[1-5]')

pattern = re.compile(r'[a-z]')
pattern = re.compile(r'[A-Z]')
pattern = re.compile(r'[a-zA-Z]')  # ⭐️
pattern = re.compile(r'[^a-zA-Z]')  # NOT in the character set

pattern = re.compile(r'[^b]at')  # NOT in the character set

pattern = re.compile(r'Mr\.?\s[A-Z]\w*')
pattern = re.compile(r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*')  # ⭐️


# Match pattern
matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)

# print(text_to_search[1:4])
# print(text_to_search[28:31])
# print(text_to_search[142:153])


# Search with context manager

# with open('data.txt', 'r', encoding='utf-8') as f:
#     contents = f.read()

#     matches = pattern.finditer(contents)

#     for match in matches:
#         print(match)

"""
# 🎯 https://stackoverflow.com/a/1548720/15063197

import os, re

def purge(dir, pattern):
    for f in os.listdir(dir):
        if re.search(pattern, f):
            os.remove(os.path.join(dir, f))

"""
