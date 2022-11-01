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
  code: "class Xorconvolution():\n    def __init__(self, mod = 998244353):\n     \
    \   self.mod = mod\n\n    def FHT(self, a):\n        n = len(a)\n        i = 1\n\
    \        while i < n:\n            for j in range(n):\n                if (j &\
    \ i) == 0:\n                    x = a[j]\n                    y = a[j | i]\n \
    \                   a[j] = x + y\n                    a[j | i] = x - y\n     \
    \       i *= 2\n\n    def IFHT(self, a):\n        inv2 = pow(2, self.mod - 2,\
    \ self.mod)\n        n = len(a)\n        i = 1\n        while i < n:\n       \
    \     for j in range(n):\n                if (j & i) == 0:\n                 \
    \   x = a[j]\n                    y = a[j | i]\n                    a[j] = x +\
    \ y\n                    a[j | i] = x - y\n                    a[j] *= inv2; a[j\
    \ | i] *= inv2\n                    a[j] %= self.mod\n                    a[j\
    \ | i] %= self.mod\n            i *= 2\n        \n    def XORconv(self,a, b):\n\
    \        n = len(a)\n        self.FHT(a)\n        self.FHT(b)\n        c = [0]\
    \ * n\n\n        for i in range(n):\n            c[i] = (a[i] * b[i]) % self.mod\n\
    \        \n        self.IFHT(c)\n\n        for i in range(n):\n            c[i]\
    \ %= self.mod\n        return c\n\n\n"
  dependsOn: []
  isVerificationFile: false
  path: Xorconvolution.py
  requiredBy: []
  timestamp: '2022-11-02 01:48:20+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Xorconvolution.py
layout: document
redirect_from:
- /library/Xorconvolution.py
- /library/Xorconvolution.py.html
title: Xorconvolution.py
---
