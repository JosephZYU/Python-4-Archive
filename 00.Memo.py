"""

🧭 Always use r'\d.' -> use dot . to grab all possible characters first!

🧭 [a-zA-Z0-9_] 是一种对与\w的精细化控制

# MOST-COMMON search ⭐️ (a-z, A-Z, 0-9, _)

pattern = re.compile(r'\w')  # 256

pattern = re.compile(r'[a-zA-Z0-9_]')  # 256 = 104 + 42 + 110

# pattern = re.compile(r'[a-z]')  # 104
# pattern = re.compile(r'[A-Z]')  # 42
# pattern = re.compile(r'[0-9]')  # 110
# pattern = re.compile(r'[_]')  # 0



🧭 pattern.findall() 🆚 pattern.finditer()
😎 perfer: pattern.finditer() 尽可能多使用finditer获得更丰富的信息

    NOTE: 两者都可以提取
    https://youtu.be/K8L6KVGG-7o?t=2780



🎯 Optional - 05

Given the set:
[' ', '$', '(', ')', '*', '+', '-', '.', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', '?', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', '\\', ']', '^', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}']
Try to count the frequency of each character from the given text

统计各个字符在一段文本中出现的评率 - 优化NLP后序处理

########################################
pattern = re.compile('.')

matches = pattern.findall(text_to_search)

li_mat = []

for match in matches:
    print(match)  # 'str'
    li_mat.append(match)

print(sorted(set(li_mat)))
########################################





🎯 Optional - 05

Use os.listdir (or os.scandir in >= 3.5) to list items in a single directory, 
use os.walk (which uses os.listdir or os.scandir in >= 3.5) to list items in a directory tree.

Ref - Listdir vs os.walk?
https://www.reddit.com/r/Python/comments/6wdxn5/listdir_vs_oswalk/


"""
