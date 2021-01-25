"""


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
