def reverseWord(s):
    s = list(s)
    l = len(s)

    i = 0
    j = l - 1
    p = ''
    while (i < j):
        s[i], s[j] = s[j], s[i]
        i += 1
        j -= 1
    p=''.join([i for i in s])
    return p