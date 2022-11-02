---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/Matrixdet.test.py
    title: test/Matrixdet.test.py
  - icon: ':x:'
    path: test/Matrixinv.test.py
    title: test/Matrixinv.test.py
  - icon: ':x:'
    path: test/Matrixproduct.test.py
    title: test/Matrixproduct.test.py
  - icon: ':x:'
    path: test/systemoflinereq.test.py
    title: test/systemoflinereq.test.py
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':question:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class Matrix():\n    def __init__(self, r, c, mod = 998244353):\n       \
    \ self.r = r\n        self.c = c\n        self.A = [[0] * self.c for _ in range(self.r)]\n\
    \        self.mod = mod\n    \n    def makeone(self, r = 1):\n        A = Matrix(r,\
    \ r, self.mod)\n        for i in range(r):\n            A[i, i] = 1\n        return\
    \ A\n        \n    def __getitem__(self, key):\n        rnow, cnow = key\n   \
    \     return self.A[rnow][cnow]\n    \n    def __setitem__(self, key, value):\n\
    \        rnow, cnow = key\n        self.A[rnow][cnow] = value\n    \n    def __add__(self,\
    \ other):\n        assert self.r == other.r and self.c == other.c\n        ret\
    \ = Matrix(self.r, self.c)\n        for i in range(self.r):\n            for j\
    \ in range(self.c):\n                ret[i, j] = self[i, j] + other[i, j]\n  \
    \              ret[i, j] %= self.mod\n        return ret\n\n    def __sub__(self,\
    \ other):\n        assert self.r == other.r and self.c == other.c\n        ret\
    \ = Matrix(self.r, self.c)\n        for i in range(self.r):\n            for j\
    \ in range(self.c):\n                ret[i, j] = self[i, j] - other[i, j]\n  \
    \              ret[i, j] %= self.mod\n        return ret\n\n    def __mul__(self,\
    \ other):\n        if isinstance(other, int):\n            ret = Matrix(self.r,\
    \ self.c)\n            for i in range(self.r):\n                for j in range(self.c):\n\
    \                    ret[i, j] = self[i, j] * other\n                    ret[i,\
    \ j] %= self.mod\n                    \n\n        assert self.c == other.r\n \
    \       ret = Matrix(self.r, other.c)\n        for i in range(self.r):\n     \
    \       for j in range(self.c):\n                for k in range(other.c):\n  \
    \                  ret[i, k] += self[i, j] * other[j, k]\n                   \
    \ ret[i, k] %= self.mod\n        return ret\n\n    def pow(self, x):\n       \
    \ assert isinstance(x, int) and x >= 0\n        assert self.r == self.c\n    \
    \    if x == 0:\n            return self.makeone(self.c)\n        else:\n    \
    \        ret = self.makeone(self.c)\n            now = self\n            while\
    \ x > 0:\n                if x % 2:\n                    ret *= now\n        \
    \        now *= now\n                x //= 2\n            return ret\n       \
    \     \n                    \n\n    def augment(self, other):\n\n        assert\
    \ self.r == other.r\n\n        X = Matrix(self.r, self.c + other.c, mod = self.mod)\n\
    \n        for i in range(self.r):\n            for j in range(self.c):\n     \
    \           X[i, j] = self[i, j]\n            for j in range(other.c):\n     \
    \           X[i, j + self.c] = other[i, j]\n        \n        return X\n    \n\
    \    def diminish(self, c):\n\n        X = []\n\n        for i in range(self.r):\n\
    \            X.append((self.A[i][:c]))\n        \n        return Matrix(self.r,\
    \ c, mod = self.mod, A = X)\n        \n    def hakidashi(self):\n        for i\
    \ in range(self.c):\n            for j in range(i + 1, self.r):\n            \
    \    if self[j, i] != 0:\n                    for k in range(self.c):\n      \
    \                  self[j, k], self[i, k] = self[i, k], self[j, k]\n         \
    \           break\n\n        for i in range(self.r):\n            for j in range(self.c):\n\
    \                if self[i, j] != 0:\n                    break\n            else:\n\
    \                continue\n            K = pow(self[i, j], self.mod - 2, self.mod)\n\
    \n            for to in range(self.c):\n                self[i, to] *= K\n   \
    \             self[i, to] %= self.mod\n\n            for i2 in range(self.r):\n\
    \                if i == i2:\n                    continue\n                time\
    \ = self[i2, j]\n                for j2 in range(self.c):\n                  \
    \  self[i2, j2] -= time * self[i, j2]\n                    self[i2, j2] %= self.mod\n\
    \n        return self\n\n    def inv(self):\n        assert self.c == self.r\n\
    \n        one = Matrix.makeone(self.r)\n        new = self.augment(one)\n    \
    \    new.hakidashi()\n        for i in range(self.r):\n            for j in range(self.c):\n\
    \                if i == j:\n                    if new[i, j] != 1:\n        \
    \                return 0, new\n                else:\n                    if\
    \ new[i, j] != 0:\n                        return 0, new\n        \n        X\
    \ = Matrix(self.r, self.c)\n\n        for i in range(self.r):\n            for\
    \ j in range(self.c):\n                X[i, j] = new[i, j + self.c]\n\n      \
    \  return 1, X\n\n    def lineareq(self, b):\n        assert self.r == b.r\n \
    \       assert b.c == 1\n        Y = self.augment(b)\n        Y = Y.hakidashi()\n\
    \        B = [[0] * self.c for _ in range(self.c)]\n        ans = [0] * self.c\n\
    \n        flag = [0] * self.c\n        for i in range(self.r):\n            j\
    \ = 0\n            while j < self.c and Y[i, j] == 0:\n                j += 1\n\
    \            if j == self.c:\n                if Y[i, -1] != 0:\n            \
    \        return None, None\n                continue\n            flag[j] = 1\n\
    \            ans[j] = Y[i, -1]\n            for k in range(j + 1, self.c):\n \
    \               if Y[i, k] % self.mod != 0:\n                    B[k][j] = (-Y[i,\
    \ k])% self.mod\n                    flag[k] = -1\n        for i in range(self.c):\n\
    \            if  flag[i] != 1:\n                B[i][i] = 1\n        B=[B[i] for\
    \ i in range(self.c) if flag[i] != 1]\n        return ans,B\n\n    def rank(self):\n\
    \        new = self.hakidashi()\n        ret = 0\n        for i in range(self.r):\n\
    \            for j in range(self.c):\n                if new[i, j] != 0:\n   \
    \                 ret += 1\n                    break\n        return ret\n\n\
    \    def det(self):\n        ret = 1\n        a = self\n        for i in range(self.r):\n\
    \            if a[i, i] == 0:\n                for j in range(i + 1, self.r):\n\
    \                    if a[j, i]:\n                        break\n            \
    \    else:\n                    return 0\n                for k in range(self.r):\n\
    \                    a[j, k], a[i, k] = a[i, k], a[j, k]\n                ret\
    \ *= -1\n                ret %= self.mod\n\n            for j in range(self.r):\n\
    \                if i < j:\n                    buf = a[j, i] * (pow(a[i, i],\
    \ self.mod - 2, self.mod))\n                    buf %= self.mod\n            \
    \        for k in range(self.r):\n                        a[j, k] -= a[i, k] *\
    \ buf\n\n                        a[j, k] %= self.mod\n        for i in range(self.r):\n\
    \            ret *= a[i, i]\n            ret %= self.mod\n        return ret\n\
    \n    def print(self):\n        for v in self.A:\n            print(*v)\n\n  \
    \      "
  dependsOn: []
  isVerificationFile: false
  path: Matrix.py
  requiredBy: []
  timestamp: '2022-11-02 23:38:59+09:00'
  verificationStatus: LIBRARY_SOME_WA
  verifiedWith:
  - test/Matrixdet.test.py
  - test/systemoflinereq.test.py
  - test/Matrixinv.test.py
  - test/Matrixproduct.test.py
documentation_of: Matrix.py
layout: document
redirect_from:
- /library/Matrix.py
- /library/Matrix.py.html
title: Matrix.py
---
