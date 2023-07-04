# 소수 구하기, S3

M, N = map(int, input().split())

numbers = [True] * (N+1)
numbers[0] = False
numbers[1] = False

for i in range(2, int(N**0.5 +1)):
    k = 2
    while i*k <= N:
        numbers[i*k] = False
        k = k + 1

for j in range(M,N+1):
    if numbers[j]:
        print(j)
            



