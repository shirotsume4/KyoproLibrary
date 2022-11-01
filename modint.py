class mint(int):
    def __init__(self, v = 0):
        self.mod = 998244353
    def __add__(self, other):
        return mint(int.__add__(self,other) % self.mod)
    def __sub__(self, other):
        return mint(int.__sub__(self,other) % self.mod)
    def __mul__(self, other):
        return mint(int.__mul__(self,other) % self.mod)
    def __floordiv__(self, other):
        return mint(int.__mul__(self,pow(other, self.mod-2,self.mod)) %self.mod)

import sys
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())
inf = 2 ** 63 - 1
mod = 998244353
 
 
 
n, m = mi()
a, b, c, d, e, f = mi()
XY = set()
 
for _ in range(m):
    x, y = mi()
    XY.add((x, y))
 
dp = [[[0] * 302 for _ in range(302)] for _ in range(302)] 
dp[0][0][0] = mint(1)
for i in range(n + 1):
    for j in range(n + 1 - i):
        for k in range(n + 1 - j):
            if i + j + k > n:
                continue
            tox = i * a + j * c + k * e
            toy = i * b + j * d + k * f
            if (tox + a, toy + b) not in XY:
                dp[i + 1][j][k] += dp[i][j][k]
            if (tox + c, toy + d) not in XY:
                dp[i][j + 1][k] += dp[i][j][k]
            if (tox + e, toy + f) not in XY:
                dp[i][j][k + 1] += dp[i][j][k]
ans = mint()
for i in range(n + 1):
    for j in range(n + 1):
        for k in range(n + 1):
            if i + j + k == n:
                ans += dp[i][j][k]
print(ans)