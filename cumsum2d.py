class Cumsum2d():
    def __init__(self, A):
        self.X = len(A[0])
        self.Y = len(A)
        self.Suma = [[0] * (self.X + 1) for _ in range(self.Y + 1)]
        for i in range(self.X):
            for j in range(self.Y):
                self.Suma[i + 1][j + 1] = self.Suma[i + 1][j] + self.Suma[i][j + 1] - self.Suma[i][j] + A[i][j]
    def query(self, x1, y1, x2, y2) -> int:
        #0-indexed
        assert 0 <= x1 <= x2 < self.X and 0 <= y1 <= y2 < self.Y
        return self.Suma[x2 + 1][y2 + 1] - self.Suma[x2 + 1][y1] - self.Suma[x1][y2 + 1] + self.Suma[x1][y1]
