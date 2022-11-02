# verification-helper: PROBLEM https://judge.yosupo.jp/problem/queue_operate_all_composite
import sys
sys.path.append("..")
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())
inf = 2 ** 63 - 1
mod = 998244353
from SWAG import SWAG
def op(x, y):
    xa, xb = y
    ya, yb = x
    za = xa * ya % mod
    zb = xa * yb + xb
    zb %= mod
    return (za, zb)


q = ii()

S = SWAG(op, (1, 0))

for _ in range(q):
    t = li()
    if t[0] == 0:
        a, b = t[1:]
        S.push((a, b))
    elif t[0] == 1:
        S.pop()
    else:
        x = t[1]
        a, b = S.fold()
        print((a * x + b) % mod)