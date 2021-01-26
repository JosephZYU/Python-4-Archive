# https://youtu.be/K8L6KVGG-7o?t=3040

import os
import re

from text import text_to_search, sentence

# search key-word as case-insensitive

pattern = re.compile(r'[\w]{4}', re.I)  # re.IGNORECASE

# Use pattern.match() to seach for simple (exact) result
# for match in pattern.finditer(text_to_search):
#     print(match.group(1))
#     print(type(match.group(1)))

matches = pattern.findall(text_to_search)

print(matches)

for match in matches:
    print(match)
