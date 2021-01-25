# https://youtu.be/K8L6KVGG-7o?t=1420

import os
import re
from text import text_to_search, sentence

# Create pattern
# 🧭 [] 是一种对与\w的精细化控制

# pattern = re.compile(r'.')  # 320

# pattern = re.compile(r'\w')  # 256

# pattern = re.compile(r'[a-zA-Z0-9_]')  # 256 = 104 + 42 + 110

# pattern = re.compile(r'[a-z]')  # 104
# pattern = re.compile(r'[A-Z]')  # 42
# pattern = re.compile(r'[0-9]')  # 110
# pattern = re.compile(r'[_]')  # 0

# ^ to exclude something ⛔️ (match any single character that is NOT a b)
pattern = re.compile(r'[^b]at')

# -> ['cat', 'mat', 'pat']


# Working with text *Advanced
# https://youtu.be/K8L6KVGG-7o?t=1705


# 🧠 (r'M[rs]s?\.? [A-Z]\w*') -> \w* (catch ALL the rest of words)

pattern = re.compile(r'M[rs]s?\.?\s[A-Z]\w*')  # ⭐️

# Use group for better solution *Advanced
# https://youtu.be/K8L6KVGG-7o?t=1910 ⏭⏭⏭

# pattern = re.compile(r'(Mr|Ms|Mrs)\.?')

# Create of list / set of matches (iterable)

li_matches = pattern.findall(text_to_search)

print(f'list of ALL matches: {li_matches}')
print(f'length of ALL matches: {len(li_matches)}')

set_matches = set(li_matches)

print(f'unique set of matches: {set_matches}')
print(f'length of unique matches: {len(set_matches)}')


# Use context manager to open 🗄
# 🧠 with open('file.ext', 'r') as f:

with open('data.txt', 'r') as f:
    contents = f.read()
    matches = pattern.findall(contents)

    for match in matches:
        print(match)
