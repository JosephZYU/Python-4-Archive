# https://youtu.be/K8L6KVGG-7o?t=635

import os
import re

from text import text_to_search, sentence

# 🧭 🧠 list of re.compile(r'\')

pattern = re.compile(r'\bHa')  # \b - word boundary (leading space) 空格领头的第一个单次

pattern = re.compile(r'\BHa')  # \B - NOT starting with a word boundary

pattern = re.compile(r'\BHaHa')

pattern = re.compile(r'^Start')  # ^ - VERY beginning of a string

pattern = re.compile(r'end$')  # $ - VERY End of a string

# Create of list / set of matches (iterable)

li_matches = pattern.findall(sentence)

print(f'list of ALL matches: {li_matches}')
print(f'length of ALL matches: {len(li_matches)}')

set_matches = set(li_matches)

print(f'unique set of matches: {set_matches}')
print(f'length of unique matches: {len(set_matches)}')

# Show the exact position (location) of each string match
for match in pattern.finditer(sentence):
    print(match)
