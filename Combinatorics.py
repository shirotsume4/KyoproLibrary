class Combinatorics():
    def __init__(self, mod, maxi):
        self.mod = mod
        self.maxi = maxi
        self.facs = [1] * (maxi + 1)
        self.factinvs = [1] * (maxi + 1)
        self.invs = [1] * (maxi + 1)
        for i in range(2, self.maxi + 1):
            self.facs[i] = ((self.facs[i-1] * i) % self.mod)
            self.invs[i] = (-self.invs[self.mod % i] * (self.mod // i)) % self.mod
            self.factinvs[i] = (self.factinvs[i-1] * self.invs[i]) % self.mod
            
    def choose(self, n, k) -> int:
        if k < 0 or k > n: return 0
        if k == 0 or k == n: return 1
        k = min(k, n - k)
        return (((self.facs[n] * self.factinvs[k]) % self.mod) * self.factinvs[n-k]) % self.mod
    
    def perm(self, n, k) -> int:
        return (self.choose(n, k) * self.facs[k]) % self.mod

    def homop(self, n, k) -> int:
        if n == k == 0:
            return 1
        return self.choose(n + k - 1, k)




