"""

string: +=

list: .append()

"""

# How to print a to z? (A to Z)
# https://stackoverflow.com/a/3190207/15063197

# 🧠 import string
# 🧠 string.ascii_lower[:] -> ascii_lower[]
# 🧠 string.ascii_upper[:] -> ascii_upper[]

import string

str_lower = string.ascii_lowercase[:]
str_upper = string.ascii_uppercase[:]

str_nums = ''

for num in list(range(1, 10)):
    str_nums += str(num)

str_nums += '0'

"""
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters(Need to be escaped):
.[{()\^$|?*+

coreyms.com

321-555-4321
123.555.1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
"""
