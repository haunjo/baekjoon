import sys
from collections import deque
N = int(input())
answer = deque([])

for i in range(N):
    command = sys.stdin.readline().strip().split(" ")
    #print(command)
    if command[0] == "push":
        answer.append(command[1])
    elif command[0] == "front":
        if len(answer)>0:
            print(answer[0])
        else:
            print(-1)
    elif command[0] == "back":
        if len(answer)>0:
            print(answer[-1])
        else:
            print(-1)
    elif command[0] =="pop":
        if len(answer) > 0:
            print(answer.popleft())
        else:
            print(-1)
    elif command[0] == "empty":
        if answer:
            print(0)
        else:
            print(1)
    elif command[0] == "size":
        print(len(answer))