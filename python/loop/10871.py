N, X = map(int, input().split(' '))

A = list((map(int, input().split(' '))))
B = list()

for i in A:
    if( i < X ):
        B.append(i)

for j in B:
    print(j, end=' ')



