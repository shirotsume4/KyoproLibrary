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
  code: "class Combinatorics():\n    def __init__(self, mod = 998244353, maxi = 5\
    \ * 10 ** 5):\n        self.mod = mod\n        self.maxi = maxi\n        self.facs\
    \ = [1, 1]\n        self.factinvs = [1, 1]\n        self.invs = [0, 1]\n     \
    \   for i in range(2, self.maxi + 1):\n            self.facs.append((self.facs[-1]\
    \ * i) % self.mod)\n            self.invs.append((-self.invs[self.mod % i] * (self.mod\
    \ // i)) % self.mod)\n            self.factinvs.append((self.factinvs[-1] * self.invs[-1])\
    \ % self.mod)\n            \n    def choose(self, n, k) -> int:\n        if k\
    \ < 0 or k > n: return 0\n        if k == 0 or k == n: return 1\n        k = min(k,\
    \ n - k)\n        return (((self.facs[n] * self.factinvs[k]) % self.mod) * self.factinvs[n-k])\
    \ % self.mod\n    \n    def perm(self, n, k) -> int:\n        return (self.choose(n,\
    \ k) * self.facs[k]) % self.mod\n\n    def homop(self, n, k) -> int:\n       \
    \ if n == k == 0:\n            return 1\n        return self.choose(n + k - 1,\
    \ k)\n\n    def factorial(self, n):\n        return self.facs[n]\n\n\n\n\n"
  dependsOn: []
  isVerificationFile: false
  path: Combinatorics.py
  requiredBy: []
  timestamp: '2022-11-02 01:48:20+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Combinatorics.py
layout: document
redirect_from:
- /library/Combinatorics.py
- /library/Combinatorics.py.html
title: Combinatorics.py
---
