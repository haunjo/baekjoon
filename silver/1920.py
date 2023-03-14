import sys

N = int(input())

A = set(map(int, sys.stdin.readline().split(" ")))
L = len(A)

M = int(input())

B = list(map(int, sys.stdin.readline().split(" ")))

answer = dict()

A = sorted(list(A))
#print(A)

def binary_search(num, data):
    start = 0
    end = L-1
    
    while start <= end:
        mid = (start + end)//2
        #print(start, end, mid)
        if num == data[mid]:
            answer[num] = 1
            return 1
        elif num < data[mid]:
            end = mid-1
        else:
            start = mid+1
    answer[num] = 0
    return 0

for i in B:
    if i in answer.keys():
        print(answer[i])
    else:
        print(binary_search(i, A))