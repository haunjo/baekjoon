A = list()

for i in range(0, 10):
    a = int(input())
    A.append((a%42))


print(len(set(A)))


