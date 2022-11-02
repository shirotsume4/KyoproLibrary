# verification-helper: PROBLEM https://judge.yosupo.jp/problem/associative_array
import sys
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())
inf = 2 ** 63 - 1
mod = 998244353
from .. import safedict
q = ii()
d = sdict()
for _ in range(q):
    query = li()
    if query[0] == 0:
        k, v = query[1:]
        d[k] = v
    else:
        k = query[1]
        if k in d:
            print(d[k])
        else:
            print(0)
