N = int(input())

paper = []

for i in range(N):
    paper.append(list(map(int, input().split(" "))))

white = 0
blue = 0

def recursive(paper):
    global white
    global blue
    #print(paper)
    if all([len(set(a))==1 and a[0] == 1 for a in paper]):
        blue += 1
        return 0
    elif all([len(set(a))==1 and a[0] == 0 for a in paper]):
        white +=1
        return 0
    else:
        recursive([row[0:len(paper)//2] for row in paper[0:len(paper)//2]])
        recursive([row[0:len(paper)//2] for row in paper[len(paper)//2:]])
        recursive([row[len(paper)//2:] for row in paper[0:len(paper)//2]])
        recursive([row[len(paper)//2:] for row in paper[len(paper)//2:]])

recursive(paper)
print(white, blue, sep="\n")