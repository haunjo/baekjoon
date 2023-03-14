N = int(input())

for i in range(0,N):
    answer = map(str, input().split(" "))
    for k in answer:
        print(k[::-1], end=" ")