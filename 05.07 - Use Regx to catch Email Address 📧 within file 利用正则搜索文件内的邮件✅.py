# https://youtu.be/K8L6KVGG-7o?t=1995

import os
import re

from text import text_to_search, sentence
from email import emails
from url import urls

pattern = re.compile(r'[a-zA-Z0-9.-]+@[a-z-_]+\.[a-z]{2}[a-z]?')

pattern = re.compile(r'[a-zA-Z0-9.-]+@[a-zA-Z0-9-_]+\.\w+')  # 200


# ✅ how to locate ONLY the final extension of a string
# Ref - Python-0-Automation - Trifecat Template IRIS

pattern = re.compile(r'@[a-zA-Z-_]+\.\w+')


for match in pattern.findall(emails):
    match = match[match.find('.'):]
    print(match)
