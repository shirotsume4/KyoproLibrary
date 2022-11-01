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
  code: "import heapq\nclass Heap():\n    def __init__(self, maxi = False):\n    \
    \    self.sum = 0\n        self.al = []\n        self.maxi = maxi\n        self.len\
    \ = 0\n\n    def __len__(self):\n        return len(self.al)\n\n    def add(self,\
    \ x):\n        if self.maxi:\n            heapq.heappush(self.al, -x)\n      \
    \  else:\n            heapq.heappush(self.al, x)\n        self.sum += x\n    \n\
    \    def pop(self):\n        if self.maxi:\n            now = heapq.heappop(self.al)\n\
    \            self.sum += now\n            return -now\n        else:\n       \
    \     now = heapq.heappop(self.al)\n            self.sum -= now\n            return\
    \ now\n\n    def top(self):\n        now = self.pop()\n        self.add(now)\n\
    \        return now"
  dependsOn: []
  isVerificationFile: false
  path: Heap.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Heap.py
layout: document
redirect_from:
- /library/Heap.py
- /library/Heap.py.html
title: Heap.py
---
