from collections import deque

N = int(input())
M = int(input())
computers = dict()

for i in range(1,N+1):
    computers[i] = []

for i in range(0,M):
    a, b = map(int, input().split(" "))
    computers[a].append(b)
    computers[b].append(a)

def BFS(start, networks):
    global N
    visited = [False]*N
    queue = deque([start])
    while queue:
        curr = queue.popleft()
        if visited[curr-1] == False:
            visited[curr-1] = True
            queue = queue + deque(networks[curr])
        else:
            continue
    return visited.count(True)

print(BFS(1, computers)-1)

