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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.8/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.8/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class Cumsum2d():\n    def __init__(self, A):\n        self.X = len(A[0])\n\
    \        self.Y = len(A)\n        self.Suma = [[0] * (self.X + 1) for _ in range(self.Y\
    \ + 1)]\n        for i in range(self.X):\n            for j in range(self.Y):\n\
    \                self.Suma[i + 1][j + 1] = self.Suma[i + 1][j] + self.Suma[i][j\
    \ + 1] - self.Suma[i][j] + A[i][j]\n    def query(self, x1, y1, x2, y2):\n   \
    \     #0-indexed\n        return self.Suma[x2][y2] - self.Suma[x2][y1] - self.Suma[x1][y2]\
    \ + self.Suma[x1][y1]\n\n\n\n"
  dependsOn: []
  isVerificationFile: false
  path: Cumsum2d.py
  requiredBy: []
  timestamp: '2022-11-02 01:48:20+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Cumsum2d.py
layout: document
redirect_from:
- /library/Cumsum2d.py
- /library/Cumsum2d.py.html
title: Cumsum2d.py
---
