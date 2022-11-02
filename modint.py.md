---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class mint(int):\n    def __init__(self, v = 0):\n        self.mod = 998244353\n\
    \    def __add__(self, other):\n        return mint(int.__add__(self,other) %\
    \ self.mod)\n    def __sub__(self, other):\n        return mint(int.__sub__(self,other)\
    \ % self.mod)\n    def __mul__(self, other):\n        return mint(int.__mul__(self,other)\
    \ % self.mod)\n    def __floordiv__(self, other):\n        return mint(int.__mul__(self,pow(other,\
    \ self.mod-2,self.mod)) %self.mod)\n\nimport sys\ninput = lambda: sys.stdin.readline().rstrip()\n\
    ii = lambda: int(input())\nmi = lambda: map(int, input().split())\nli = lambda:\
    \ list(mi())\ninf = 2 ** 63 - 1\nmod = 998244353\n \n \n \nn, m = mi()\na, b,\
    \ c, d, e, f = mi()\nXY = set()\n \nfor _ in range(m):\n    x, y = mi()\n    XY.add((x,\
    \ y))\n \ndp = [[[0] * 302 for _ in range(302)] for _ in range(302)] \ndp[0][0][0]\
    \ = mint(1)\nfor i in range(n + 1):\n    for j in range(n + 1 - i):\n        for\
    \ k in range(n + 1 - j):\n            if i + j + k > n:\n                continue\n\
    \            tox = i * a + j * c + k * e\n            toy = i * b + j * d + k\
    \ * f\n            if (tox + a, toy + b) not in XY:\n                dp[i + 1][j][k]\
    \ += dp[i][j][k]\n            if (tox + c, toy + d) not in XY:\n             \
    \   dp[i][j + 1][k] += dp[i][j][k]\n            if (tox + e, toy + f) not in XY:\n\
    \                dp[i][j][k + 1] += dp[i][j][k]\nans = mint()\nfor i in range(n\
    \ + 1):\n    for j in range(n + 1):\n        for k in range(n + 1):\n        \
    \    if i + j + k == n:\n                ans += dp[i][j][k]\nprint(ans)"
  dependsOn: []
  isVerificationFile: false
  path: modint.py
  requiredBy: []
  timestamp: '2022-11-02 01:48:20+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: modint.py
layout: document
redirect_from:
- /library/modint.py
- /library/modint.py.html
title: modint.py
---
