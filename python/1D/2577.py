
L = list()
B = 1

for i in range(0,3):
    A = int(input())
    B = B*A

B = str(B)

for i in B:
    L.append(int(i))

for i in range(0,10):
    print(L.count(i))