import sys
from collections import deque
N = int(input())

notation = deque(sys.stdin.readline().strip())
nums = dict()
for i in range(N):
    nums[chr(65+i)] = sys.stdin.readline().strip()


stack = []

while notation:
    if ord(notation[0]) > 64:
        stack.append(notation.popleft())
    elif ord(notation[0]) <= 64:
        a = stack.pop()
        b = stack.pop()
        c = notation.popleft()
        stack.append(f'({b}{c}{a})')

answer = list(stack[0])

for i in range(len(answer)):
    if answer[i] in nums.keys():
        answer[i] = nums[answer[i]]

answer = ''.join(answer)
print("{:.2f}".format(eval(answer)))