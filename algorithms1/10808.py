from collections import Counter

str = input().strip()

cnt = dict(Counter(str))
answer = dict()
alpa = "abcdefghijklmnopqrstuvwxyz"

for i in alpa:
    if i not in answer.keys():
        answer[i] = 0

answer = answer|cnt

print(*answer.values(), sep=" ")
    
