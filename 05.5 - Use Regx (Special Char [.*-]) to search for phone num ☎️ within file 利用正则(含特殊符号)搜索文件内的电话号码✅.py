# https://youtu.be/K8L6KVGG-7o?t=1175

import os
import re
from text import text_to_search, sentence

pattern = re.compile(r'\d\d\d\d')

pattern = re.compile(r'\d{3}\*\d{3}\*\d{4}')

# Search for specific special character within Regx 精准搜索🔍特殊符号
# 🧠 r'\d{3}[.*-]\d{3}[.*-]\d{4}' -> [.*-] ⭐️

pattern = re.compile(r'\d{3}[.*-]\d{3}[.*-]\d{4}')  # 10
# pattern = re.compile(r'\d{3}[*-]\d{3}[*-]\d{4}')  # 8
# pattern = re.compile(r'\d{3}[-]\d{3}[-]\d{4}')  # 6
# pattern = re.compile(r'\d{3}[.*]\d{3}[.*]\d{4}')  # 4
# pattern = re.compile(r'\d{3}[*]\d{3}[*]\d{4}')  # 2
# pattern = re.compile(r'\d{3}[.]\d{3}[.]\d{4}')  # 2

# Create of list / set of matches (iterable)

li_matches = pattern.findall(text_to_search)

print(f'list of ALL matches: {li_matches}')
print(f'length of ALL matches: {len(li_matches)}')

set_matches = set(li_matches)

print(f'unique set of matches: {set_matches}')
print(f'length of unique matches: {len(set_matches)}')

# Show the exact position (location) of each string match
# for match in pattern.finditer(text_to_search):
#     print(match)


# Use context manager to open 🗄
# 🧠 with open('file.ext', 'r') as f:

with open('data.txt', 'r') as f:
    contents = f.read()
    matches = pattern.findall(contents)

    for match in matches:
        print(match)
