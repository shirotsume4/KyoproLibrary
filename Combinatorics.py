class Combinatorics():
    def __init__(self, mod, maxi = 3 * 10 ** 6):
        self.mod = mod
        self.maxi = maxi
        self.facs = [1, 1]
        self.factinvs = [1, 1]
        self.invs = [0, 1]
        for i in range(2, self.maxi + 1):
            self.facs.append((self.facs[-1] * i) % self.mod)
            self.invs.append((-self.invs[self.mod % i] * (self.mod // i)) % self.mod)
            self.factinvs.append((self.factinvs[-1] * self.invs[-1]) % self.mod)
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

class BinomialCoefficient():
    def __init__(self, mod, maxi = 3 * 10 ** 6):
        self.mod = mod
        self.maxi = maxi
        self.facs = [1, 1]
        self.factinvs = [1, 1]
        self.invs = [0, 1]
        for i in range(2, self.maxi + 1):
            self.facs.append((self.facs[-1] * i) % self.mod)
            self.invs.append((-self.invs[self.mod % i] * (self.mod // i)) % self.mod)
            self.factinvs.append((self.factinvs[-1] * self.invs[-1]) % self.mod)
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
mod = 10 ** 9 + 7
C = BinomialCoefficient(mod)

for _ in range(int(input())):
    s = input()
    n, k = map(int,s[2:-1].split(","))
    if s[0] == 'C':
        print(C.choose(n, k))
    if s[0] == 'P':
        print(C.perm(n, k))
    if s[0] == 'H':
        print(C.homop(n, k))