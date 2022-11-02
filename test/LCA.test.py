# verification-helper: PROBLEM https://judge.yosupo.jp/problem/lca
import sys
sys.path.append("..")
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())
inf = 2 ** 63 - 1
mod = 998244353
from Eulertour_and_LCA import LCA

n, q = mi()
p = li()

graph = [[] for _ in range(n)]

for i in range(n - 1):
    graph[i + 1].append(p[i])
    graph[p[i]].append(i + 1)

L = LCA(graph)

for _ in range(q):
    u, v = mi()
    print(L.lca(u, v))