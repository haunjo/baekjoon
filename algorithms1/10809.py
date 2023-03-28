from collections import Counter

str = input().strip()

alpa = "abcdefghijklmnopqrstuvwxyz"

cnt = dict()

for i in alpa:
    cnt[i] = -1

for k in range(len(str)):
    if cnt[str[k]] == -1:
        cnt[str[k]] = k
    
print(*cnt.values(), sep=" ")