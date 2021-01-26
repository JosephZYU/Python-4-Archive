# 🧭🧭🧭

# needs a list directly -> pattern.findall()
# findall() -> 直接生成list，便于OOP [0|1|2]

# needs more granular control -> pattern.finditer()
# finditer() -> 更丰富的信息和位置 group(0|1|2)

import os
import re

from text import text_to_search, sentence

pattern = re.compile(r'(Mr|Ms|Mrs)[\.]? ([A-Z][a-z]*)')

# NOTE: findall() -> tuple
# Tuple还是可以读取的，和list原则一样

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
