# verification-helper: PROBLEM https://judge.yosupo.jp/problem/shortest_path
import sys
sys.path.append("..")
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())
inf = 2 ** 63 - 1
mod = 998244353

from Dijkstra import Dijkstra, DijkstraRest


n, m, s, t = mi()
graph = [[] for _ in range(n)]
for _ in range(m):
    u, v, w = mi()
    graph[u].append((v, w))

d, r = Dijkstra(s, graph)
if d[t] >= inf:
    print(-1)
    exit()
ret = DijkstraRest(r, t)
print(d[t], len(ret))
for u, v in ret:
    print(u, v)