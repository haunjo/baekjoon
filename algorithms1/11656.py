# 접미사 배열, S4

words = input()
ls = []
for i in range(0, len(words)):
    ls.append(words[i:])

for i in sorted(ls):
    print(i)