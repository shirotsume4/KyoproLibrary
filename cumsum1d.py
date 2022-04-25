class cumsum1d():
    n = None
    Suma = []
    def __init__(self, A):
        self.n = len(A)
        self.Suma = [0] * (self.n + 1)
        for i in range(self.n):
            self.Suma[i + 1] += self.Suma[i] + A[i]

    def query(self, l, r):
        #0-indexed
        return self.Suma[r + 1] - self.Suma[l]

    def get(self, i):
        return self.Suma[i + 1] - self.Suma[i]

