# https://youtu.be/K8L6KVGG-7o?t=2360

import os
import re

from url import urls


pattern = re.compile(r'http[s]?://(www.)?([a-z]+).([a-z]{3})')

for match in pattern.finditer(urls):
    print(match.group(1))
    print(match.group(2))
    print(match.group(3))
    print()
