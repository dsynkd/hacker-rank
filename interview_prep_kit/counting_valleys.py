def countingValleys(steps, path):
    v = 0
    l = 0 # level
    for i in range(0, steps):
        p = path[i]
        if p == 'D' and l == 0:
            v += 1
        if p == 'D':
            l -= 1
        else:
            l += 1
    return v
