from collections import deque

N, M, V = map(int, input().split(" "))

graph = dict()
for k in range(1,N+1):
    graph[k] = []

for i in range(0,M):
    k, v = map(int, input().split(" "))
    graph[k].append(v)
    graph[v].append(k)


def DFS(start, map):
    answer = []
    for key in map.keys():
        map[key] = sorted(map[key],reverse=True)
    visited = [False]*N
    stack = [start]
    while stack:
        #print(stack)
        curr = stack.pop()
        if not visited[curr-1]:
            visited[curr-1] = True
            answer.append(curr)
            if map[curr]:
                stack = stack + map[curr]
    return answer

def BFS(start, map):
    answer = []
    for key in map.keys():
        map[key] = sorted(map[key])
    visited = [False]*N
    queue = deque([start])
    while queue:
        #print(queue)
        curr = queue.popleft()
        if not visited[curr-1]:
            visited[curr-1] = True
            answer.append(curr)
            if map[curr]:
                queue = queue + deque(map[curr])
    return answer
print(*DFS(V, graph), sep=" ")
print(*BFS(V, graph), sep=" ")