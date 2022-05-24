class Matrix():
    def __init__(self, r, c, mod = 998244353):
        self.r = r
        self.c = c
        self.A = [[0] * self.c for _ in range(self.r)]
        self.mod = mod
    
    def makeone(self, r = 1):
        A = Matrix(r, r, self.mod)
        for i in range(r):
            A[i, i] = 1
        return A
        
    def __getitem__(self, key):
        rnow, cnow = key
        return self.A[rnow][cnow]
    
    def __setitem__(self, key, value):
        rnow, cnow = key
        self.A[rnow][cnow] = value
    
    def __add__(self, other):
        assert self.r == other.r and self.c == other.c
        ret = Matrix(self.r, self.c)
        for i in range(self.r):
            for j in range(self.c):
                ret[i, j] = self[i, j] + other[i, j]
                ret[i, j] %= self.mod
        return ret

    def __sub__(self, other):
        assert self.r == other.r and self.c == other.c
        ret = Matrix(self.r, self.c)
        for i in range(self.r):
            for j in range(self.c):
                ret[i, j] = self[i, j] - other[i, j]
                ret[i, j] %= self.mod
        return ret

    def __mul__(self, other):
        if isinstance(other, int):
            ret = Matrix(self.r, self.c)
            for i in range(self.r):
                for j in range(self.c):
                    ret[i, j] = self[i, j] * other
                    ret[i, j] %= self.mod
                    

        assert self.c == other.r
        ret = Matrix(self.r, other.c)
        for i in range(self.r):
            for j in range(self.c):
                for k in range(other.c):
                    ret[i, k] += self[i, j] * other[j, k]
                    ret[i, k] %= self.mod
        return ret

    def augment(self, other):

        assert self.r == other.r

        X = Matrix(self.r, self.c + other.c, mod = self.mod)

        for i in range(self.r):
            for j in range(self.c):
                X[i, j] = self[i, j]
            for j in range(other.c):
                X[i, j + self.c] = other[i, j]
        
        return X
    
    def diminish(self, c):

        X = []

        for i in range(self.r):
            X.append((self.A[i][:c]))
        
        return Matrix(self.r, c, mod = self.mod, A = X)
        
    def hakidashi(self):
        for i in range(self.c):
            for j in range(i + 1, self.r):
                if self[j, i] != 0:
                    for k in range(self.c):
                        self[j, k], self[i, k] = self[i, k], self[j, k]
                    break

        for i in range(self.r):
            for j in range(self.c):
                if self[i, j] != 0:
                    break
            else:
                continue
            K = pow(self[i, j], self.mod - 2, self.mod)

            for to in range(self.c):
                self[i, to] *= K
                self[i, to] %= self.mod

            for i2 in range(self.r):
                if i == i2:
                    continue
                time = self[i2, j]
                for j2 in range(self.c):
                    self[i2, j2] -= time * self[i, j2]
                    self[i2, j2] %= self.mod

        return self

    def inv(self):
        assert self.c == self.r

        one = Matrix.makeone(r = self.r)
        new = self.augment(one)
        new.hakidashi()
        for i in range(self.r):
            for j in range(self.c):
                if i == j:
                    if new[i, j] != 1:
                        return 0, new
                else:
                    if new[i, j] != 0:
                        return 0, new
        
        X = Matrix(self.r, self.c)

        for i in range(self.r):
            for j in range(self.c):
                X[i, j] = new[i, j + self.c]

        return 1, X

    def lineareq(self, b):
        assert self.r == b.r
        assert b.c == 1
        Y = self.augment(b)
        Y = Y.hakidashi()
        B = [[0] * self.c for _ in range(self.c)]
        ans = [0] * self.c

        flag = [0] * self.c
        for i in range(self.r):
            j = 0
            while j < self.c and Y[i, j] == 0:
                j += 1
            if j == self.c:
                if Y[i, -1] != 0:
                    return None, None
                continue
            flag[j] = 1
            ans[j] = Y[i, -1]
            for k in range(j + 1, self.c):
                if Y[i, k] % self.mod != 0:
                    B[k][j] = (-Y[i, k])% self.mod
                    flag[k] = -1
        for i in range(self.c):
            if  flag[i] != 1:
                B[i][i] = 1
        B=[B[i] for i in range(self.c) if flag[i] != 1]
        return ans,B

    def rank(self):
        new = self.hakidashi()
        ret = 0
        for i in range(self.r):
            for j in range(self.c):
                if new[i, j] != 0:
                    ret += 1
                    break
        return ret

    def det(self):
        ret = 1
        a = self
        for i in range(self.r):
            if a[i, i] == 0:
                for j in range(i + 1, self.r):
                    if a[j, i]:
                        break
                else:
                    return 0
                for k in range(self.r):
                    a[j, k], a[i, k] = a[i, k], a[j, k]
                ret *= -1
                ret %= self.mod

            for j in range(self.r):
                if i < j:
                    buf = a[j, i] * (pow(a[i, i], self.mod - 2, self.mod))
                    buf %= self.mod
                    for k in range(self.r):
                        a[j, k] -= a[i, k] * buf

                        a[j, k] %= self.mod
        for i in range(self.r):
            ret *= a[i, i]
            ret %= self.mod
        return ret

    def print(self):
        for v in self.A:
            print(*v)

        