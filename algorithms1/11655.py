words = list(input())

for i in range(0, len(words)):
    if ord(words[i]) >= 65 and ord(words[i]) <= 90:
        new = ord(words[i]) + 13
        if new > 90:
            new -= 26
        words[i] = chr(new)
    elif ord(words[i]) >= 97 and ord(words[i]) <= 122:
        new = ord(words[i]) + 13
        if new > 122:
            new -= 26
        words[i] = chr(new)
print("".join(words))