# find out unique character (E.g. numbers, digis, signs) from a given text

import re


text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

coreyms.com

321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''

sentence = 'Start a sentence and then bring it to an end'

pattern = re.compile(r'.')

# Match pattern
matches = pattern.finditer(text_to_search)

li_items = []

for match in matches:

    item = str(match)[-3:-2]

    li_items.append(item)

print(li_items)
print(len(li_items))

print(set(li_items))
print(len(set(li_items)))
