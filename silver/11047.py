import sys

N, K = map(int, sys.stdin.readline().split(" "))

coins = []

for i in range(N):
    coins.append(int(sys.stdin.readline()))

cnt = 0
i = N-1



for j in range(N):
        if K < coins[j]:
            i = j-1
            break
            
while True:
    if K < coins[i]:  
        i -= 1
    else:
        cnt += K//coins[i]
        K = K%coins[i]
        i -= 1
    if K == 0:
        break
print(cnt)