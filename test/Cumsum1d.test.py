# verification-helper: PROBLEM https://judge.yosupo.jp/problem/static_range_sum
import sys
sys.path.append("..")
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())
inf = 2 ** 63 - 1
mod = 998244353
from Cumsum1d import Cumsum1d


n, q = mi()

a = li()

A = Cumsum1d(a)

for _ in range(q):
    l, r = mi()
    print(A[l:r])