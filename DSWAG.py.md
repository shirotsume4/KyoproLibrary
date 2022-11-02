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
  code: "class DSWAG():\n    def __init__(self, op, e):\n        self.op = op\n  \
    \      self.e = e\n        self.top = []\n        self.bottom = []\n        self.topfold\
    \ = [e]\n        self.bottomfold = [e]\n    def _pushbottom(self, x):\n      \
    \  self.bottom.append(x)\n        self.bottomfold.append(self.op(self.bottomfold[-1],\
    \ x))\n    def _popbottom(self):\n        self.bottomfold.pop()\n        return\
    \ self.bottom.pop()\n    def _pushtop(self, x):\n        self.top.append(x)\n\
    \        self.topfold.append(self.op(x, self.topfold[-1]))\n    def _poptop(self):\n\
    \        self.topfold.pop()\n        return self.top.pop()\n    def push(self,\
    \ x):\n        self._pushbottom(x)\n    def pushleft(self, x):\n        self._pushtop(x)\n\
    \    def fold(self):\n        return self.op(self.topfold[-1], self.bottomfold[-1])\n\
    \    def popleft(self):\n        if not self.top:\n            stack = []\n  \
    \          while self.bottom:\n                x = self._popbottom()\n       \
    \         stack.append(x)\n            n = len(stack)\n            stack = stack[::-1]\n\
    \            stack1 = stack[:(n+1)//2]\n            stack2 = stack[(n+1)//2:][::-1]\n\
    \            for _ in range((n + 1) // 2):\n                self._pushtop(stack1.pop())\n\
    \            for _ in range(n // 2):\n                self._pushbottom(stack2.pop())\n\
    \        if not self.top:\n            return self.e\n        else:\n        \
    \    return self._poptop()\n    def pop(self):\n        if not self.bottom:\n\
    \            stack = []\n            while self.top:\n                x = self._poptop()\n\
    \                stack.append(x)\n            n = len(stack)\n            stack1\
    \ = stack[:n//2]\n            stack2 = stack[n//2:][::-1]\n            for _ in\
    \ range((n+1) // 2):\n                self._pushbottom(stack2.pop())\n       \
    \     for _ in range(n // 2):\n                self._pushtop(stack1.pop())\n \
    \       if not self.bottom:\n            return self.e\n        else:\n      \
    \      return self._popbottom()\n"
  dependsOn: []
  isVerificationFile: false
  path: DSWAG.py
  requiredBy: []
  timestamp: '2022-11-02 01:48:20+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: DSWAG.py
layout: document
redirect_from:
- /library/DSWAG.py
- /library/DSWAG.py.html
title: DSWAG.py
---
