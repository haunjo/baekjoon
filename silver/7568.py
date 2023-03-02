
N = int(input())

ls = []
queue = []

for i in range(0, N):
    ls.append(list(map(int, input().split(" "))))
#print(ls)

for a in ls:
    level = 1
    for b in ls:
        if a[0] < b[0] and a[1] < b[1]:
            level += 1
    queue.append(level)
for num in queue:
    print(num, end=" ")