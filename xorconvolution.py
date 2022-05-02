class Xorconvolution():
    def __init__(self, mod = 998244353):
        self.mod = mod

    def FHT(self, a):
        n = len(a)
        i = 1
        while i < n:
            for j in range(n):
                if (j & i) == 0:
                    x = a[j]
                    y = a[j | i]
                    a[j] = x + y
                    a[j | i] = x - y
            i *= 2

    def IFHT(self, a):
        inv2 = pow(2, self.mod - 2, self.mod)
        n = len(a)
        i = 1
        while i < n:
            for j in range(n):
                if (j & i) == 0:
                    x = a[j]
                    y = a[j | i]
                    a[j] = x + y
                    a[j | i] = x - y
                    a[j] *= inv2; a[j | i] *= inv2
                    a[j] %= self.mod
                    a[j | i] %= self.mod
            i *= 2
        
    def XORconv(self,a, b):
        n = len(a)
        self.FHT(a)
        self.FHT(b)
        c = [0] * n

        for i in range(n):
            c[i] = (a[i] * b[i]) % self.mod
        
        self.IFHT(c)

        for i in range(n):
            c[i] %= self.mod
        return c


