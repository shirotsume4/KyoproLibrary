# verification-helper: PROBLEM https://judge.yosupo.jp/problem/matrix_product
import sys
sys.path.append("..")
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())
inf = 2 ** 63 - 1
mod = 998244353
from Matrix import Matrix

n, m, k = map(int,input().split())
mod = 998244353
a = [list(map(int,input().split())) for _ in range(n)]
b = [list(map(int,input().split())) for _ in range(m)]

c = [[0] * k for _ in range(n)]

for x in range(n):
    for y in range(m):
        for z in range(k):
            c[x][z] += a[x][y] * b[y][z]
            c[x][z] %= mod

for i in range(n):
    print(*c[i])