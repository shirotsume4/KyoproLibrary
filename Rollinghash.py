class Rollinghash():
    def __init__(self, A):
        import random
        if isinstance(A[0], str):
            self.A = [0] * len(A)
            for i in range(len(A)):
                self.A[i] = ord(A[i])
        else:
            self.A = A[::]

        self.mod1 = 1999881227
        self.mod2 = 999051227
        self.r1 = random.randint(0, self.mod1 - 1)
        self.r2 = random.randint(0, self.mod2 - 1)
        self.S1 = self.hashing(self.r1, self.mod1)
        self.S2 = self.hashing(self.r2, self.mod2)
        self.pow1= [1] * (len(A) + 1)
        self.pow2= [1] * (len(A) + 1)
        for i in range(1, len(A) + 1):
            self.pow1[i] = pow(self.r1, i, self.mod1)
        for i in range(1, len(A) + 1):
            self.pow2[i] = pow(self.r2, i, self.mod2)
    def hashing(self, r, mod):
        S = [0, self.A[0]]
        for v in self.A[1:]:
            S.append((S[-1] * r + v) % mod)
        return S
    def query1(self, l, r):
        return (self.S1[r] - self.S1[l] * self.pow1[r - l]) % self.mod1
    def query2(self, l, r):
        return (self.S2[r] - self.S2[l] * self.pow2[r - l]) % self.mod2
    def same(self, l1, r1, l2, r2):
        return self.query1(l1, r1) == self.query1(l2, r2) and self.query2(l1, r1) == self.query2(l2, r2)