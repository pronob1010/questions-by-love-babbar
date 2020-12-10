def reverseWord(s):
    s = list(s)

    l = len(s)

    i = 0
    j = l - 1

    while (i < j):
        s[i], s[j] = s[j], s[i]
        i+=1
        j-=1
    return s

s = input()
print(reverseWord(s))