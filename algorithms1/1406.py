import sys
from collections import deque
problem = sys.stdin.readline().strip()
#첫번째 문자열
N = int(sys.stdin.readline())
#명령어 개수
#명령어들의 리스트
#커서의 위치(처음에는 마지막원소 오른쪽에 있음)
# print(command)
left = [x for x in problem]
right = deque([])

for i in range(N):
    command = sys.stdin.readline().split()
    if command[0] == "P":
        left.append(command[1])
    elif command[0] == "D" and right:
        left.append(right.popleft())
    elif command[0] == "L" and left:
        right.appendleft(left.pop())
    elif command[0] == "B" and left:
        left.pop()

print(*(left+list(right)), sep="")
    

