class matrix():
    r = 1
    c = 1
    A = None
    mod = None
    def __init__(self, r, c, mod = None, one = False, A = None):
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
                if self.mod is not None:
                    ret[i, j] %= self.mod
        return ret

    def __sub__(self, other):
        
        assert self.r == other.r and self.c == other.c
        ret = matrix(self.r, self.c)
        for i in range(self.r):
            for j in range(self.c):
                ret[i, j] = self[i, j] - other[i, j]
                if self.mod is not None:
                    ret[i, j] %= self.mod
        return ret

    def __mul__(self, other):

        assert self.c == other.r
        ret = matrix(self.r, other.c)
        for i in range(self.r):
            for j in range(self.c):
                for k in range(other.c):
                    ret[i, k] += self[i, j] * other[j, k]
                    if self.mod is not None:
                        ret[i, k] %= self.mod
        return ret

    def augment(self, other):

        assert self.r == other.r

        X = []

        for i in range(self.r):
            X.append((self.A[i] + other.A[i]))
        
        return matrix(self.r, 2 * self.c, mod = self.mod, A = X)




    def print(self):
        for v in self.A:
            print(*v)

