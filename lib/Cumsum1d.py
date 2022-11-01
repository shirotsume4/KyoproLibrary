class Cumsum1d():
    def __init__(self, A):
        self.n = len(A)
        self.Suma = [0] * (self.n + 1)
        for i in range(self.n):
            self.Suma[i + 1] += self.Suma[i] + A[i]

    def query(self, l, r):
        #0-indexed
        return self.Suma[r] - self.Suma[l]

    def get(self, i):
        return self.Suma[i + 1] - self.Suma[i]

    def __getitem__(self, p):
        if isinstance(p, int):
            return self.get(p)
        else:
            return self.query(p.start, p.stop)

