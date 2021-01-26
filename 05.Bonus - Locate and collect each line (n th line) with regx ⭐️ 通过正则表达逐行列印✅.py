# Ref - How can I get python to read every nth line of a .txt file? [duplicate]
# https://stackoverflow.com/a/47062516/15063197

import os
import re
from text import text_to_search, sentence


# ✅ how to print out by every 1st line
# 如何对于有规律的文档，列印每组的第一行


with open('data.txt', 'r') as f:

    lines = f.readlines()

names = []


for line in lines[3::5]:
    names.append(line[:-1])

print(names)


# source: lines (read from the context manager)
# start:0, 1, 2, 3 -> range(4)
# width:5

def collect_line(source, start_index, width):
    contents = []

    for line in source[start_index::width]:
        contents.append(line[:-2])

    print(contents)


collect_line(lines, 0, 5)  # Email Address - ONLY
collect_line(lines, 1, 5)  # Phone Number - ONLY
collect_line(lines, 2, 5)  # Address  - ONLY
