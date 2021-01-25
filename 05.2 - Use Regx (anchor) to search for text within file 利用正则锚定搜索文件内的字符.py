# https://youtu.be/K8L6KVGG-7o?t=635

import os
import re

from text import text_to_search

# 🧭 🧠 list of re.compile(r'')

pattern = re.compile(r'.')  # Any character except a new line

pattern = re.compile(r'\d')  # Any (single) digit within 0 to 9

pattern = re.compile(r'\D')  # NOT a digit - the opposite of lower case

pattern = re.compile(r'\w')  # MOST-COMMON search ⭐️ (a-z, A-Z, 0-9, _)

pattern = re.compile(r'\W')  # NOT a word (Exclude: a-z, A-Z, 0-9, _)

pattern = re.compile(r'\s')  # Whitespace (space, tab, new line)

pattern = re.compile(r'\S')  # Not Whitespace

pattern = re.compile(r'\d{3}.\d{3}.\d{4}')

# Create of list of matches (iterable)

set_matches = set(pattern.findall(text_to_search))


print(f'unique set of matches: {set_matches}')

print(f'length of unique matches: {len(set_matches)}')


for match in pattern.finditer(text_to_search):
    print(match)
