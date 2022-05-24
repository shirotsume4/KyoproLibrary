from math import gcd
def isprime(n):
    if n <= 2:
        return n == 2
    if n % 2 == 0:
        return False
    s = 0
    t = n - 1
    while t % 2 == 0:
        s += 1
        t //= 2
    
    for a in [2, 3, 5, 7, 11, 13, 17, 19, 23, 31, 37]:
        if a >= n:
            break
        x = pow(a, t, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s):
            x = (x * x) % n
            if x == n - 1:
                break
        if x == n - 1:
            continue

        return False
    return True

def Pollad(N):
    if N % 2 == 0:
        return 2
    if isprime(N):
        return N
    def f(x):
        return (x * x + 1) % N
    step = 0

    while True:
        step += 1
        x = step
        y = f(x)
        while True:
            p = gcd(y - x + N, N)
            if p == 0 or p == N:
                break
            if p != 1:
                return p
            x = f(x)
            y = f(f(y))


def Primefact(N):
    if N == 1:
        return []
    q = []
    q.append(N)
    ret = []
    while q:
        now = q.pop()
        if now == 1:
            continue
        p = Pollad(now)
        if p == now:
            ret.append(p)
        else:
            q.append(p)
            q.append(now // p)

    return ret

def EulerPhi(n):
    ret = n
    for i in range(2, n + 1):
        if i * i > n:
            break
        if n % i == 0:
            ret -= ret // i
            while n % i == 0:
                n //= i
    if n > 1:
        ret -= ret // n
    return ret

def Tetration(a, b, mod):
    if mod == 1:
        return 0
    if a == 0:
        return 1 - (b & 1)
    if b == 0:
        return 1
    if b == 1:
        return a % mod
    if b == 2:
        return pow(a, a, mod)
    phi = EulerPhi(mod)
    t = Tetration(a, b - 1, phi)
    if t == 0:
        t += phi
    return pow(a, t, mod)


    
