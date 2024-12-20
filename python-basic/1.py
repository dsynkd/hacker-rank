def avg(*args):
    t = 0
    for v in iter(args):
        t += v
    return t / len(args)
