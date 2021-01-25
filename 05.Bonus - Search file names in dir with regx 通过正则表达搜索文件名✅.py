# pattern = re.compile(r'\d{2}.*py')
import re
import os

pattern = re.compile(r'\d{2}.*.py')

for f in os.listdir():
    if re.search(pattern, f):
        print(f)
