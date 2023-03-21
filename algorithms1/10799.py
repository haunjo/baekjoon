import sys

answer = list(map(str, sys.stdin.readline().strip()))
#print(answer)
open = 0
close = 0

pipes = 0

for i,v in enumerate(answer):
    if v == '(':
        if answer[i+1] == ')':
            continue
        else:
            open += 1
    elif v == ')':
        if answer[i-1] == '(':
            pipes += open-close
        else:
            close += 1

pipes += close
print(pipes)


        