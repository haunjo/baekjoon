A = int(input())
count = 0
if(A < 10):
        A = A*10
C = A

while(1):
    a = C//10
    b = C%10
    B = a + b
    C = b*10 + B%10
    count = count + 1
    if(C == A):
        print(count)
        break
