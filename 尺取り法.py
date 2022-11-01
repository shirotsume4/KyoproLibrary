ans = 0
right = 0
#n -> 数列の長さ
for left in range(n):
    while right < n:
        ここにrightが区間に入った時の処理を書く
        if ここに満たすべき条件を書く:
            right += 1
        else:
            ここにrightが区間から出たときの処理を書く
            break

    ここにansの更新式を書く

    if right == left:
        right += 1
    else:
        ここにleftが区間から出たときの処理を書く
import string
import sys
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())
inf = 2 ** 63 - 1
mod = 998244353


def sq(x):
    ok = 0
    ng = x + 1
    while abs(ok - ng) > 1:
        mid = (ok + ng)//2
        if mid * mid <= x:
            ok = mid
        else:
            ng = mid
    return ok

