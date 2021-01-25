"""

🎯 how to link pattern from regx (re) with re.search(pattern, file)

    实现正则表达式pattern和re.search(pattern, file)之间的交互连接

"""


import os
import re
from text import text_to_search, sentence

# Concept of Raw String
# print('tab')    # regular print func
# print('\ttab')  # \t -> as if we're using tab on our keyboard
# print(r'\tab')  # raw string -> always interpret string literaly 解析文字需要表的含义

# 🧭 whenever needs Regx -> r'\' 需要用正则表达的时候必须使用r' ⭐️
pattern = re.compile(r'\d{2}.*py')

# 🧭 findall 🆚 finditer
# finditer() -> complete info with precise location 提供完整定位信息
# findall() -> better for count of frequency 更适合后期统计 len(matches)

# 🧠 pattern.finditer()
# 🧠 pattern.findall()

matches = pattern.findall(text_to_search)

for match in matches:
    print(match)  # 'str'


"""
def purge(dir, pattern):
    for f in os.listdir(dir):
        if re.search(pattern, f):
            os.remove(os.path.join(dir, f))
"""


"""
def pre_scan(dir, pattern):
    for f in os.listdir(dir):
        if re.search(pattern, f):
            print(f)


dir_1 = '/Users/josephyu/Documents/GitHub/Python-4-Archive/TBD-test/'

pattern_1 = re.compile('*.txt')

pre_scan(dir_1, pattern_1)
"""
