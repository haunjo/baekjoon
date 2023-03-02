import sys

N = int(sys.stdin.readline())

numbers = list(map(int, sys.stdin.readline().split(" ")))

count = list(set(numbers))

dict = {}

for idx, val in enumerate(sorted(count)):
    dict[val] = idx
for i in numbers:
    print(dict[i], end = " ")
#print(dict)