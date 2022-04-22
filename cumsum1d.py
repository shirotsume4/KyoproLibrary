class Cumsum1d():
    def __init__(self, A):
        self.Suma = []
        self.n = len(A)
        self.Suma.append(0)
        for i in range(self.n):
            self.Suma.append(self.Suma[-1] + A[i])
    
    def query(self, l, r) -> int:
        #0-indexed
        assert 0 <= l <= r < self.n
        return self.Suma[r + 1] - self.Suma[l]

    def get(self, i) -> int:
        assert 0 <= i < self.n
        return self.query(i, i + 1)