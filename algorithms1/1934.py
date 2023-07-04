import sys

n = int(sys.stdin.readline())

for i in range(n):
    A, B = sys.stdin.readline().split(" ")
    A, B = int(A), int(B)
    
    if A<B:
        temp = A
        A = B
        B = temp
    
    maxn = 1
    for k in range(1,B+1):
        if A%k == 0 and B%k == 0:
            maxn = k
    print((A*B)//maxn)