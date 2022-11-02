# verification-helper: PROBLEM https://judge.yosupo.jp/problem/counting_primes
import sys
sys.path.append("..")
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())
inf = 2 ** 63 - 1
mod = 998244353
from CountPrime import countprime
print(countprime(int(input())))