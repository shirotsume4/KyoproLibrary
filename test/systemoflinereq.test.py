# verification-helper: PROBLEM https://judge.yosupo.jp/problem/system_of_linear_equations
import sys
sys.path.append("..")
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())
inf = 2 ** 63 - 1
mod = 998244353
from Matrix import Matrix

n, m = mi()
a = Matrix(n, m)

for i in range(n):
    al = li()
    for j in range(m):
        a[i, j] = al[j]

b = Matrix(n, 1)
bl = li()

for i in range(n):
    b[i, 0] = bl[i]

ans, ker = a.lineareq(b)
if ans is None:
    print(-1)
    exit()
print(len(ker))

print(*ans)

for v in ker:
    print(*v)
