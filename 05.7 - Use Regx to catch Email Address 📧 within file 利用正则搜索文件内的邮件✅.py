# https://youtu.be/K8L6KVGG-7o?t=1995

import os
import re

from email import emails

pattern = re.compile(r'[a-zA-Z0-9.-]+@[a-zA-Z0-9-_]+\.\w+')  # 200
# pattern = re.compile(r'[a-zA-Z0-9.-]+@[a-zA-Z0-9-_]+\.[a-z]{2}[a-z]?')  # 200

for match in pattern.findall(emails):
    print(match)
