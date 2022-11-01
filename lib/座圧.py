def comp(a):
    import bisect
    n = len(a)
    b = sorted(list(set(a)))
    c = []
    for i in range(n):
        c.append(bisect.bisect(b, a[i]) - 1)
    return c
