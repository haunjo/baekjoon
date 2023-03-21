import sys

answer = list(map(str, sys.stdin.readline().strip()))
#print(answer)

i = 0

while i < len(answer):
    #print(i)
    if answer[i] == "<":
        while answer[i] != ">":
            i += 1
        i += 1
    else:
        start = i
        while i < len(answer) and answer[i] != "<":
            i += 1
        end = i
        temp = answer[start:end]
        temp = list(map(str, ''.join(temp).split(" ")))
        for k in range(0,len(temp)):
            temp[k] = temp[k][::-1]
        #print(temp)
        answer[start:end] = list(' '.join(temp).strip())
for i in answer:
    print(i, end="")
        