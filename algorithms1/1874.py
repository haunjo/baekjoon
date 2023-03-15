import sys

N = int(input())
answer = []
for i in range(0,N):
    answer.append(int(sys.stdin.readline()))

numbers = [x for x in range(N,0,-1)]
print(numbers)
ls1 = []
pushpop = []
ls2 = []



for i in answer:
    if not ls1 and not numbers:
        break
    if not ls1:
        ls1.append(numbers.pop())
        pushpop.append("+")
    while ls1[-1] != i:
        if not numbers:
            break
        ls1.append(numbers.pop())
        pushpop.append("+")
    if ls1[-1] == i:
        ls2.append(ls1.pop())
        pushpop.append("-")

if ls2 == answer:
    for i in pushpop:
        print(i)
else:
    print("NO")