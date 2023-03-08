from collections import deque

N = int(input())

tree = dict()

for i in range(1,N+1):
    tree[i] = []

for k in range(0,N-1):
    a, b = map(int, input().split(" "))
    tree[b].append(a)
    tree[a].append(b)

print(tree)

def BFS(tree_):
    global N
    visited = [[0,0]]*N
    print(visited)
    stack = deque([1])
    parent = 1
    while stack:
        curr = stack.popleft()
        if visited[curr-1][0] == 0:
            for i in tree_[curr]:
                if visited[i-1][1] == 0:
                    visited[i-1][1] = curr
                    print(visited)
            visited[curr-1][0] = 1
            stack = stack + deque(tree_[curr])
    return visited

print(*BFS(tree))
