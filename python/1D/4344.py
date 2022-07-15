C = int(input())
for i in range(0, C):
    l = list(map(int, input().split( )))
    med = sum(l[1:])/l[0]
    A = list()
    for k in l[1:]:
        if k > med:
            A.append(k)
    rate = len(A)/l[0]*100
    print(f'{rate:.3f}%')

