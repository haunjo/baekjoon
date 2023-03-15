from collections import deque
import sys

N = int(input())

tree = dict()

for i in range(1,N+1):
    tree[i] = []

for k in range(0,N-1):
    a, b = map(int, sys.stdin.readline().split(" "))
    tree[b].append(a)
    tree[a].append(b)

#print(tree)

# 1-6-3-5
#  -4-2
#    -7
answer = dict()
   
def BFS(tree, start):
    global N
    global answer
    queue = deque([start])
    visited = [False]*N
    while queue:
        a = queue.popleft()
        if not visited[a-1]:
            visited[a-1] = True
            for i in tree[a]:
                if not visited[i-1]:
                    answer[i] = a
                    queue.append(i)                    

BFS(tree, 1)
for i in range(2,N+1):
    print(answer[i])