---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/Cumsum1d.test.py
    title: test/Cumsum1d.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
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
  path: Cumsum1d.py
  requiredBy: []
  timestamp: '2022-11-02 01:48:20+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/Cumsum1d.test.py
documentation_of: Cumsum1d.py
layout: document
redirect_from:
- /library/Cumsum1d.py
- /library/Cumsum1d.py.html
title: Cumsum1d.py
---
