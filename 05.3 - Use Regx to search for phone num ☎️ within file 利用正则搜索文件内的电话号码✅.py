# https://youtu.be/K8L6KVGG-7o?t=850

import os
import re
from text import text_to_search, sentence

pattern = re.compile(r'\d\d\d\d')

# Quantifier - https://youtu.be/K8L6KVGG-7o?t=1620

pattern = re.compile(r'\d{3}.\d{3}.\d{4}')  # ⭐️

pattern = re.compile(r'\d{3,4}.\d{3,4}.\d{3,4}')  # ⭐️

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


# Use context manager
