A, B = input().split(" ")

A, B = int(A), int(B)
if A < B:
    temp = A
    A = B
    B = temp


if A >= B:
    max = 1
    min = B
    for i in range(1, B+1):
        if B%i == 0 and A%i == 0:
            max = i
    for i in range(1, A+1):
        if (B*i) % A == 0:
            min = B*i
            break
print(max)
print(min)
