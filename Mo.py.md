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
  code: "class Mo():\n    def Pre(self, q, ls, rs, n):\n        B = round(((3 ** 0.5)\
    \ * n) / (2 * q) ** 0.5)\n        mx = 0\n        mxr = 0\n        for i in range(len(ls)):\n\
    \            l, r = ls[i], rs[i]\n            mx, mxr = max(mx, l // B), max(mxr,\
    \ r)\n        bucket = [[] for _ in range(mx + 1)]\n        for i in range(len(ls)):\n\
    \            bucket[ls[i] // B].append(i)\n        order = []\n        for b in\
    \ bucket:\n            order.extend(sorted(b, key = lambda x: -rs[x]))\n     \
    \   return order\n    \n    def __init__(self, N, Q, A, LRs):\n        self.n\
    \ = N\n        self.q = Q\n        self.a = A\n        self.table = [0] * (self.n\
    \ + 1)\n        self.ls = []\n        self.rs = []\n        for L, R in LRs:\n\
    \            self.ls.append(L)\n            self.rs.append(R + 1)\n          \
    \  \n        self.order = self.Pre(self.q, self.ls, self.rs, self.n)\n       \
    \ self.ans = self.solve()\n    \n    def in_query(self, x, ans):\n        #\u8981\
    \u7D20x\u304C\u533A\u9593\u306B\u5165\u3063\u305F\u6642ans\u304C\u3069\u3046\u306A\
    \u308B\u304B\n        return ans\n\n    def out_query(self, x, ans):\n       \
    \ #\u8981\u7D20x\u304C\u533A\u9593\u304B\u3089\u51FA\u305F\u3068\u304Dans\u304C\
    \u3069\u3046\u306A\u308B\u304B\n        return ans\n\n    def solve(self):\n \
    \       l = r = 0\n        ans = 0\n        ret = [0] * self.q\n        for i\
    \ in self.order:\n            \n            s, t = self.ls[i], self.rs[i]\n  \
    \          while l < s:\n                ans = self.out_query(self.a[l], ans)\n\
    \                l += 1\n            while l > s:\n                ans = self.in_query(self.a[l\
    \ - 1], ans)\n                l -= 1\n            while r < t:\n             \
    \   ans = self.in_query(self.a[r], ans)\n                r += 1\n            while\
    \ r > t:\n                ans = self.out_query(self.a[r - 1], ans)\n         \
    \       r -= 1\n            ret[i] = ans\n        return ret\n        "
  dependsOn: []
  isVerificationFile: false
  path: Mo.py
  requiredBy: []
  timestamp: '2022-04-25 22:03:25+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Mo.py
layout: document
redirect_from:
- /library/Mo.py
- /library/Mo.py.html
title: Mo.py
---
