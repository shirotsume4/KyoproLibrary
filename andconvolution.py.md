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
  code: "class andconvolution():\n    def __init__(self, mod = 998244353):\n     \
    \   self.mod = mod\n\n    def zetatransform(self, a):\n        N = len(a)\n  \
    \      n = 0\n        for i in range(0, 21):\n            if 2 ** i >= N:\n  \
    \              a += [0] * (N - 2 ** i)\n                n = i\n              \
    \  break\n        g = []\n        for i in range(2 ** n):\n            g.append(a[i])\n\
    \        for j in range(n):\n            bit = 1 << j\n            for i in range(1\
    \ << n):\n                if i & bit == 0:\n                    g[i] += g[i |\
    \ bit]\n   \n        return g\n\n    def mebioustransform(self, a):\n        N\
    \ = len(a)\n        n = 0\n        for i in range(0, 21):\n            if 2 **\
    \ i >= N:\n                a += [0] * (N - 2 ** i)\n                n = i\n  \
    \              break\n        g = []\n        for i in range(2 ** n):\n      \
    \      g.append(a[i])\n        for j in range(n):\n            bit = 1 << j\n\
    \            for i in range(1 << n):\n                if i & bit == 0:\n     \
    \               g[i] -= g[i | bit]\n   \n        return g\n\n    def ANDconv(self,\
    \ a, b):\n        a = self.zetatransform(a)\n        b = self.zetatransform(b)\n\
    \        N = max(len(a), len(b))\n        a += [0] * (N - len(a))\n        b +=\
    \ [0] * (N - len(b))\n        c = [0] * N\n\n        for i in range(N):\n    \
    \        c[i] = (a[i] * b[i]) % self.mod\n        c = self.mebioustransform(c)\n\
    \n        for i in range(N):\n            c[i] %= self.mod\n        return c\n\
    \        \n"
  dependsOn: []
  isVerificationFile: false
  path: andconvolution.py
  requiredBy: []
  timestamp: '2022-11-02 01:48:20+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: andconvolution.py
layout: document
redirect_from:
- /library/andconvolution.py
- /library/andconvolution.py.html
title: andconvolution.py
---
