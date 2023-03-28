import sys


while True:
    try:
        cnt = [0]*4
        stri = input()
        for i in stri:
            if i == " ":
                cnt[3] += 1
            elif ord(i) <= 57:
                cnt[2] += 1
            elif ord(i) <= 90:
                cnt[1] += 1
            elif ord(i) <= 122:
                cnt[0] += 1
        print(' '.join(map(str, cnt)))
    except EOFError:
        break
         