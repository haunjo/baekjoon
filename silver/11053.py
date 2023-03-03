import sys
N = int(sys.stdin.readline())

numbers = list(map(int, sys.stdin.readline().split(" ")))

dp = [1]*N

for i in range(0,N):
    for j in range(0,i):
        if numbers[i]>numbers[j]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))


#10 20 10 30 20 50

#가장 긴 증가하는 부분 수열을 구하려면?

#1. 증가해야 한다(다음 것이 더 커야 한다)
#2. 길어야 한다(바로 다음에 너무 큰 값을 만나면, 길이가 짧아질 확률이 높음)

# 20
# 31 84 18 62 35 77 23 53 60 94 3 77 60 51 42 18 83 85 63 51
