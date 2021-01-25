# https://youtu.be/K8L6KVGG-7o?t=1995

import os
import re

from email import emails

# pattern = re.compile(r'[a-zA-Z.-]+@[a-zA-Z]+\.(com|edu|net)')

pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')

matches = pattern.finditer(emails)

for match in matches:
    print(match)
