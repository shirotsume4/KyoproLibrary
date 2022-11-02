# verification-helper: PROBLEM https://judge.yosupo.jp/problem/bitwise_and_convolution
import sys
sys.path.append("..")
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())
inf = 2 ** 63 - 1
mod = 998244353
from andconvolution import andconvolution

n = ii()
a = li()
b = li()
F = andconvolution()

print(*F.ANDconv(a, b))