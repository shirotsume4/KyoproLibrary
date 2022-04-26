class andconvolution():
    def __init__(self, mod = 998244353):
        self.mod = mod

    def zetatransform(self, a):
        N = len(a)
        n = 0
        for i in range(0, 21):
            if 2 ** i >= N:
                a += [0] * (N - 2 ** i)
                n = i
                break
        g = []
        for i in range(2 ** n):
            g.append(a[i])
        for j in range(n):
            bit = 1 << j
            for i in range(1 << n):
                if i & bit == 0:
                    g[i] += g[i | bit]
   
        return g

    def mebioustransform(self, a):
        N = len(a)
        n = 0
        for i in range(0, 21):
            if 2 ** i >= N:
                a += [0] * (N - 2 ** i)
                n = i
                break
        g = []
        for i in range(2 ** n):
            g.append(a[i])
        for j in range(n):
            bit = 1 << j
            for i in range(1 << n):
                if i & bit == 0:
                    g[i] -= g[i | bit]
   
        return g

    def ANDconv(self, a, b):
        a = self.zetatransform(a)
        b = self.zetatransform(b)
        N = max(len(a), len(b))
        a += [0] * (N - len(a))
        b += [0] * (N - len(b))
        c = [0] * N

        for i in range(N):
            c[i] = (a[i] * b[i]) % self.mod
        c = self.mebioustransform(c)

        for i in range(N):
            c[i] %= self.mod
        return c
        
