import os
import re

from text import text_to_search, sentence

pattern = re.compile(r'(Mr|Ms|Mrs)[\.]? ([A-Z][a-z]*)')

# NOTE: findall() -> tuple
for match in pattern.findall(text_to_search):
    print(match[0])
    print(match[1])
    print()

pattern = re.compile(r'(\d{3}).(\d{3}).(\d{4})')

# 🧠 finditer()
# +
# 🧠 match.group(0)
# -> finditer()  group()

for match in pattern.finditer(text_to_search):
    print(match.group(0))
    print()
