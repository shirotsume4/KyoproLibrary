class DSWAG():
    def __init__(self, op, e):
        self.op = op
        self.e = e
        self.top = []
        self.bottom = []
        self.topfold = [e]
        self.bottomfold = [e]
    def _pushbottom(self, x):
        self.bottom.append(x)
        self.bottomfold.append(self.op(self.bottomfold[-1], x))
    def _popbottom(self):
        self.bottomfold.pop()
        return self.bottom.pop()
    def _pushtop(self, x):
        self.top.append(x)
        self.topfold.append(self.op(x, self.topfold[-1]))
    def _poptop(self):
        self.topfold.pop()
        return self.top.pop()
    def push(self, x):
        self._pushbottom(x)
    def pushleft(self, x):
        self._pushtop(x)
    def fold(self):
        return self.op(self.topfold[-1], self.bottomfold[-1])
    def popleft(self):
        if not self.top:
            stack = []
            while self.bottom:
                x = self._popbottom()
                stack.append(x)
            n = len(stack)
            for _ in range((n + 1) // 2):
                self._pushtop(stack.pop())
            for _ in range(n // 2):
                self._pushbottom(stack.pop())
        if not self.top:
            return self.e
        else:
            return self._poptop()
    def pop(self):
        if not self.bottom:
            stack = []
            while self.top:
                x = self._poptop()
                stack.append(x)
            n = len(stack)
            stack.reverse()
            for _ in range((n + 1) // 2):
                self._pushtop(stack.pop())
            for _ in range(n // 2):
                self._pushbottom(stack.pop())
        if not self.top:
            return self.e
        else:
            return self._popbottom()
        
import sys
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())
inf = 2 ** 63 - 1
mod = 998244353

def op(x, y):
    xa, xb = y
    ya, yb = x
    za = xa * ya % mod
    zb = xa * yb + xb
    zb %= mod
    return (za, zb)


q = ii()

S = DSWAG(op, (1, 0))

for _ in range(q):
    t = li()
    if t[0] == 0:
        a, b = t[1:]
        S.pushleft((a, b))
    elif t[0] == 1:
        a, b = t[1:]
        S.push((a, b))
    elif t[0] == 2:
        S.popleft()
    elif t[0] == 3:
        S.pop()
    else:
        x = t[1]
        a, b = S.fold()
        print((a * x + b) % mod)

