def jumpingOnClouds(c):
    t = 0
    i = 0
    while i < len(c):
        cloud = c[i]
        a = i + 2
        if a < len(c) and c[a] == 0:
            i = a
            t += 1
        else:
            a = i + 1
            if a < len(c) and c[a] == 0:
                t += 1
            i = a
    return t
