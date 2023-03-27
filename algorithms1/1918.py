import sys


prefix = list(sys.stdin.readline().strip())

stack = []
answer = []


for i in prefix:
    if i.isalpha():
        print(f"{i} is alpha")
        answer.append(i)
    elif i == "(":
        stack.append(i)
    elif i == "*" or i == "/":
        while stack and (stack[-1] == "*" or stack[-1] =="/"):
            answer.append(stack.pop())
        stack.append(i)
    elif i == "+" or i == "-":
        while stack and stack[-1] != "(":
            answer.append(stack.pop())
        stack.append(i)
    elif i == ")":
        while stack and stack[-1] != "(":
            answer.append(stack.pop())
        stack.pop()
    print(answer, stack)
while stack:
    answer.append(stack.pop())


print(*answer, sep="")
        
    
    
    
#print(prefix)

#우선순위
# ( )
# * /
# + -

