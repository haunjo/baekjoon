import sys
N = int(input())

for i in range(0,N):
    answer = sys.stdin.readline()
    answer = answer.strip()
    stack = []
    for k in answer:
        if k == ')':
            if not stack:
                stack.append(k)
                break
            else:
                stack.pop()
        else:
            stack.append(k)
    if not stack:
        print("YES")
    else:
        print("NO")