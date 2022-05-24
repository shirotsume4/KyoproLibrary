class Cumsum2d():
    def __init__(self, A):
        self.X = len(A[0])
        self.Y = len(A)
        self.Suma = [[0] * (self.X + 1) for _ in range(self.Y + 1)]
        for i in range(self.X):
            for j in range(self.Y):
                self.Suma[i + 1][j + 1] = self.Suma[i + 1][j] + self.Suma[i][j + 1] - self.Suma[i][j] + A[i][j]
    def query(self, x1, y1, x2, y2):
        #0-indexed
        return self.Suma[x2][y2] - self.Suma[x2 + 1][y1] - self.Suma[x1][y2] + self.Suma[x1][y1]



