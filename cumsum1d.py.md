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
  code: "class Cumsum1d():\n    def __init__(self, A):\n        self.n = len(A)\n\
    \        self.Suma = [0] * (self.n + 1)\n        for i in range(self.n):\n   \
    \         self.Suma[i + 1] += self.Suma[i] + A[i]\n\n    def query(self, l, r):\n\
    \        #0-indexed\n        return self.Suma[r] - self.Suma[l]\n\n    def get(self,\
    \ i):\n        return self.Suma[i + 1] - self.Suma[i]\n\n    def __getitem__(self,\
    \ p):\n        if isinstance(p, int):\n            return self.get(p)\n      \
    \  else:\n            return self.query(p.start, p.stop)\n\n"
  dependsOn: []
  isVerificationFile: false
  path: cumsum1d.py
  requiredBy: []
  timestamp: '2022-05-25 04:33:23+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cumsum1d.py
layout: document
redirect_from:
- /library/cumsum1d.py
- /library/cumsum1d.py.html
title: cumsum1d.py
---
