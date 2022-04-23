class Cumsum1d():
    def __init__(self, A = []):
        self.Suma = []
        self.n = len(A)
        self.Suma.append(0)
        for i in range(self.n):
            self.Suma.append(self.Suma[-1] + A[i])
    
    def append(self, x) -> None:
        self.Suma.append(self.Suma[-1] + x)
        self.n += 1
        
    def query(self, l, r) -> int:
        #0-indexed
        if l < 0:
            l = 0
        if r < 0:
            return 0
        if r > n - 1:
            r = n - 1
        if l > n - 1:
            return 0
        return self.Suma[r + 1] - self.Suma[l]

    def get(self, i) -> int:
        assert 0 <= i < self.n
        return self.query(i, i + 1)
