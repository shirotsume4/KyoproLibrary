# verification-helper: PROBLEM https://judge.yosupo.jp/problem/tetration_mod
import sys
sys.path.append("..")
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())
inf = 2 ** 63 - 1
from Tetration import Tetration

for _ in range(int(input())):
    a, b, m = map(int,input().split())
    print(Tetration(a, b, m))