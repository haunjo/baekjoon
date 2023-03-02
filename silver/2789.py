from itertools import combinations

N, M = map(int, input().split(" "))
cards = list(map(int, input().split(" ")))

numbers = list(combinations(cards, 3))

print(N, M)
print(numbers)

max = 0 
for i in numbers:
    if M - max >  M - sum(i) and sum(i) <= M:
        max = sum(i)
print(max)