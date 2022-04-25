def manacher(s):
    t = []
    for v in s:
        t.append(v)
        t.append('$')
    t.pop()
    ret = [0] * len(t)
    i = 0
    j = 0

    while i < len(t):
        while i - j >= 0 and i + j < len(t) and t[i - j] == t[i + j]:
            j += 1
        ret[i] = j
        k = 1
        while i  - k >= 0 and i + k < len(t) and k + ret[i - k] < j:
            ret[i + k] = ret[i - k]
            k += 1
        i += k
        j -= k
    for i in range(len(t)):
        if t[i] == '$' and ret[i] % 2:
            ret[i] -= 1
        if t[i] != '$' and ret[i] % 2 == 0:
            ret[i] -= 1
    return ret

        


