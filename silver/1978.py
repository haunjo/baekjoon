#주어진 수 N개 중에 소수가 몇개인지 찾아서 출력하는 프로그램

#첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.

n = int(input())

numbers = list(map(int, input().split(" ")))

#print(numbers)

prime = [x for x in range(2,1000)]

for i in prime:
    for j in prime:
        if i != j and j%i == 0:
            prime.remove(j)
#print(prime)

cnt = 0

for num in numbers:
    if num in prime:
        cnt += 1
print(cnt)