class matrix():
    r = 1
    c = 1
    A = None
    mod = None
    def __init__(self, r, c, mod = 998244353, one = False, A = None):
        self.r = r
        self.c = c
        self.A = [[0] * self.c for _ in range(self.r)]
        if A is not None:
            for i in range(self.r):
                for j in range(self.c):
                    self.A[i][j] = A[i][j]
        if one:
            for i in range(min(self.r, self.c)):
                self.A[i][i] = 1
        if mod is not None:
            self.mod = mod
    
    def __getitem__(self, key):
        rnow, cnow = key
        return self.A[rnow][cnow]
    
    def __setitem__(self, key, value):
        rnow, cnow = key
        self.A[rnow][cnow] = value
    
    def __add__(self, other):
        assert self.r == other.r and self.c == other.c
        ret = matrix(self.r, self.c)
        for i in range(self.r):
            for j in range(self.c):
                ret[i, j] = self[i, j] + other[i, j]
                ret[i, j] %= self.mod
        return ret

    def __sub__(self, other):
        
        assert self.r == other.r and self.c == other.c
        ret = matrix(self.r, self.c)
        for i in range(self.r):
            for j in range(self.c):
                ret[i, j] = self[i, j] - other[i, j]
                ret[i, j] %= self.mod
        return ret

    def __mul__(self, other):

        assert self.c == other.r
        ret = matrix(self.r, other.c)
        for i in range(self.r):
            for j in range(self.c):
                for k in range(other.c):
                    ret[i, k] += self[i, j] * other[j, k]
                    ret[i, k] %= self.mod
        return ret

    def augment(self, other):

        assert self.r == other.r

        X = []

        for i in range(self.r):
            X.append((self.A[i] + other.A[i]))
        
        return matrix(self.r, self.c + other.c, mod = self.mod, A = X)
    
    def diminish(self, c):

        X = []

        for i in range(self.r):
            X.append((self.A[i][:c]))
        
        return matrix(self.r, c, mod = self.mod, A = X)
        
    def hakidashi(self):
        for i in range(self.c):
            for j in range(i, self.r):
                if self.A[j][i] != 0:
                    for k in range(self.c):
                        self.A[j][k], self.A[i][k] = self.A[i][k], self.A[j][k]
                    break
            if i >= self.r or self.A[i][i] == 0:
                continue
            K = pow(self.A[i][i], self.mod - 2, self.mod)
            for k in range(self.c):
                self.A[i][k] *= K
                self.A[i][k] %= self.mod
            assert self.A[i][i] == 1
            for j in range(self.r):
                if j == i: continue
                K = self.A[j][i]
                for k in range(self.c):
                    self.A[j][k] -= self.A[i][k] * K
                    self.A[j][k] %= self.mod
        return self
        

        



    def lineareq(self, b):
        assert self.r == b.r
        assert b.c == 1
        M = self.augment(b)
        M.hakidashi()
        ans = [0] * self.c
        ker = []

        for i in range(self.r):
            cnt = 0
            for j in range(self.c):
                cnt = max(cnt, M.A[i][j])
            if cnt == 0 and M.A[i][-1] > 0:
                return -1, -1

        for i in range(self.c):
            if i >= self.r:
                break
            if M.A[i][i] == 1:
                ans[i] = M.A[i][-1] % self.mod
            else:
                ans[i] = 0

        for i in range(self.r):
            if self.A[i][i] != 1:
                ret = []
                for x in range(self.c):
                    if x == i:
                        ret.append((-1) % self.mod)
                    else:
                        ret.append((M.A[i][x]) % self.mod)
                ker.append(ret)
        return ans, ker
                    


        




    def print(self):
        for v in self.A:
            print(*v)


import sys
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())
INF = 2 ** 63 - 1
mod = 998244353
n, m = mi()
a = matrix(n, m)

for i in range(n):
    al = li()
    for j in range(m):
        a[i, j] = al[j]

b = matrix(n, 1)
bl = li()

for i in range(n):
    b[i, 0] = bl[i]

ans, ker = a.lineareq(b)
if ans == -1:
    print(-1)
    exit()
print(len(ker))

print(*ans)

for v in ker:
    print(*v)