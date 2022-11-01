# verification-helper: PROBLEM https://judge.yosupo.jp/problem/associative_array
import sys
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())
inf = 2 ** 63 - 1
mod = 998244353
class sdict(dict):
    def __init__(self):
        import random
        self.r = random.randint(1, 2 ** 63 - 1)
    def __contains__(self, __o: object) -> bool:
        return super().__contains__(__o^self.r)
    def __getitem__(self, __key):
        return super().__getitem__(__key^self.r)
    def __setitem__(self, __key, __value):
        return super().__setitem__(__key^self.r, __value)

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
