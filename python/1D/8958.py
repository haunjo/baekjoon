N = int(input())

for i in range(0, N):
    l = list(input())
    sum = 0
    count = 0
    for j in l:
        if(j == 'O'):
            count += 1
            """print(count)"""
        elif(j == 'X'):
            for k in range(1, count+1):
                sum += k
            count = 0
            """print(count)"""
    for r in range(1, count+1):
        sum += r

    print(sum)
