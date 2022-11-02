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
  code: "class Rollinghash():\n    def __init__(self, A):\n        import random\n\
    \        if isinstance(A[0], str):\n            self.A = [0] * len(A)\n      \
    \      for i in range(len(A)):\n                self.A[i] = ord(A[i])\n      \
    \  else:\n            self.A = A[::]\n\n        self.mod1 = 1999881227\n     \
    \   self.mod2 = 999051227\n        self.r1 = random.randint(0, self.mod1 - 1)\n\
    \        self.r2 = random.randint(0, self.mod2 - 1)\n        self.S1 = self.hashing(self.r1,\
    \ self.mod1)\n        self.S2 = self.hashing(self.r2, self.mod2)\n        self.pow1=\
    \ [1] * (len(A) + 1)\n        self.pow2= [1] * (len(A) + 1)\n        for i in\
    \ range(1, len(A) + 1):\n            self.pow1[i] = pow(self.r1, i, self.mod1)\n\
    \        for i in range(1, len(A) + 1):\n            self.pow2[i] = pow(self.r2,\
    \ i, self.mod2)\n    def hashing(self, r, mod):\n        S = [0, self.A[0]]\n\
    \        for v in self.A[1:]:\n            S.append((S[-1] * r + v) % mod)\n \
    \       return S\n    def query1(self, l, r):\n        return (self.S1[r] - self.S1[l]\
    \ * self.pow1[r - l]) % self.mod1\n    def query2(self, l, r):\n        return\
    \ (self.S2[r] - self.S2[l] * self.pow2[r - l]) % self.mod2\n    def same(self,\
    \ l1, r1, l2, r2):\n        return self.query1(l1, r1) == self.query1(l2, r2)\
    \ and self.query2(l1, r1) == self.query2(l2, r2)"
  dependsOn: []
  isVerificationFile: false
  path: Rollinghash.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Rollinghash.py
layout: document
redirect_from:
- /library/Rollinghash.py
- /library/Rollinghash.py.html
title: Rollinghash.py
---
