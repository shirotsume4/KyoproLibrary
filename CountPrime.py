def countprime(n):
    if n <= 1:
        return 0
    elif n <= 2:
        return 1
    elif n <= 3:
        return 2
    nsq = round(n ** 0.5)
    ndsq = n // nsq
    L = [0] * ndsq

    for i in range(1, ndsq):
        L[i] = n // i - 1
    LS = list(range(-1, nsq))
    count = 0
    for p in range(2, nsq + 1):
        if LS[p] == LS[p - 1]:
            continue
        q = p * p
        nowp = p
        indm = min(ndsq, n // q + 1)
        for to in range(1, indm):
            if nowp < ndsq:
                L[to] -= L[nowp]
            else:
                L[to] -= LS[n // nowp]
            L[to] += count
            nowp += p

        for to in range(nsq, q - 1, -1):
            LS[to] -= LS[to // p] - count 
        count += 1
    return L[1]