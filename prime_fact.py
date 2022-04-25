from math import gcd
def is_prime(n):
    if n <= 2:
        return n == 2
    if n % 2 == 0:
        return False
    s = 0
    t = n - 1
    while t % 2 == 0:
        s += 1
        t //= 2
    
    for a in [2, 3, 5, 7, 11, 13, 17, 19, 23]:
        if a >= n:
            break
        x = pow(a, t, n)
        if x == 1 or x == n - 1:
            continue
        for i in range(s):
            x = (x * x) % n
            if x == n - 1:
                break
        if x == n - 1:
            continue

        return False
    return True

def pollad(N):
    if N % 2 == 0:
        return 2
    if is_prime(N):
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


def prime_fact(N):
    if N == 1:
        return []
    q = []
    q.append(N)
    ret = []
    while q:
        now = q.pop()
        if now == 1:
            continue
        p = pollad(now)
        if p == now:
            ret.append(p)
        else:
            q.append(p)
            q.append(now // p)

    return ret


q = int(input())

for _ in range(q):
    a = int(input())
    L = prime_fact(a)
    L.sort()
    print(len(L), *L)