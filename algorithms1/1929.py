M, N = map(int, input().split())

numbers = list(range(M,N+1))
if M == 1:
    del numbers[0]

for i in range(2,N):
    for k in numbers:
        if k%i == 0 and k != i:
            numbers.remove(k)

for i in numbers:
    print(i)