n = int(input())


def fibonacci(num):
    if num == 0:
        print("0")
        return 0
    
    answer = [0]*(num+1)
    answer[1] = 1
    
    for i in range(2,num+1):
        answer[i] = answer[i-1] + answer[i-2]
    print(answer[-1])

fibonacci(n)
    
        
    