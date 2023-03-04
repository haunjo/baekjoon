from collections import deque

N = int(input())

cards = deque(range(1,N+1))

print(cards)

while len(cards)>1:
    cards.popleft()
    if len(cards)==1:
        print(cards[0])
        exit(0)
    cards.append(cards.popleft())
print(cards[0])
