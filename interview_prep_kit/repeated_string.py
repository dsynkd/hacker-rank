def repeatedString(s, n):
    r = 0
    for i in range(0, len(s)):
        if s[i] == 'a':
            r += 1
    r *= n//len(s)
    for i in range(0, n % len(s)):
        if s[i] == 'a':
            r += 1
    return r
