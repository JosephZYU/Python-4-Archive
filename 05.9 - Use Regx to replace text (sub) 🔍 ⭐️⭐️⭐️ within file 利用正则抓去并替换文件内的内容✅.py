# https://youtu.be/K8L6KVGG-7o?t=2660

import os
import re

from url import urls

pattern = re.compile(r'http[s]?://(www\.)?([a-z]+)(\.[a-z]+)')

for match in pattern.finditer(urls):
    print(match.group(0))
    print(match.group(1))
    print(match.group(2))
    print(match.group(3))
    print()

# ⭐️⭐️⭐️ Create subbed urls to mass replace existing contents
# 🧠 pattern.sub(r'\2\3', urls) -> sub(r'\group_1\group_2')

sub_urls = pattern.sub(r'\2\3', urls)

print(sub_urls)
