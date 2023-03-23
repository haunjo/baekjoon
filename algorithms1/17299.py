import sys
from collections import Counter

N = int(input())
nums = list(map(int, sys.stdin.readline().split(" ")))

cnt = Counter(nums)

stack = []

for i in range(0,N-1):
    n = nums[i+1]
    if cnt[nums[i]] >= cnt[n]:
        stack.append(i)
    elif cnt[nums[i]] < cnt[n]:
        nums[i] = n
        while stack and True:
            if cnt[nums[stack[-1]]] < cnt[n]:
                nums[stack.pop()] = n
            else:
                break
for k in stack:
    nums[k] = -1
nums[-1] = -1
    
print(*nums, sep=" ")