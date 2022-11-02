# verification-helper: PROBLEM https://judge.yosupo.jp/problem/inverse_matrix
import sys
sys.path.append("..")
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())
inf = 2 ** 63 - 1
mod = 998244353
from Matrix import Matrix
n = ii()
a = Matrix(n, n, mod)

for i in range(n):
    al = li()
    for j in range(n):
        a[i, j] = al[j]

f, a = a.inv()

if not f:
    print(-1)
else:
    a.print()