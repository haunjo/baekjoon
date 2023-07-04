numbers = input().split(" ")

A,B,C = int(numbers[0]), int(numbers[1]), int(numbers[2])


print((A+B)%C)
print(((A%C) + (B%C))%C)
print((A*B)%C)
print(((A%C) * (B%C))%C)