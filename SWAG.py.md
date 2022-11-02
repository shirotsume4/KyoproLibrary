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
  code: "class SWAG():\n    def __init__(self, op, e):\n        self.op = op\n   \
    \     self.e = e\n        self.top = []\n        self.bottom = []\n        self.topfold\
    \ = [e]\n        self.bottomfold = [e]\n    def _pushbottom(self, x):\n      \
    \  self.bottom.append(x)\n        self.bottomfold.append(self.op(self.bottomfold[-1],\
    \ x))\n    def _popbottom(self):\n        self.bottomfold.pop()\n        return\
    \ self.bottom.pop()\n    def _pushtop(self, x):\n        self.top.append(x)\n\
    \        self.topfold.append(self.op(x, self.topfold[-1]))\n    def _poptop(self):\n\
    \        self.topfold.pop()\n        return self.top.pop()\n    def push(self,\
    \ x):\n        self._pushbottom(x)\n    def fold(self):\n        return self.op(self.topfold[-1],\
    \ self.bottomfold[-1])\n    def pop(self):\n        if not self.top:\n       \
    \     while self.bottom:\n                x = self._popbottom()\n            \
    \    self._pushtop(x)\n        if not self.top:\n            return self.e\n \
    \       else:\n            return self._poptop()\n    def front(self):\n     \
    \   if not self.top:\n            while self.bottom:\n                x = self._popbottom()\n\
    \                self._pushtop(x)\n        return self.top[-1]\n"
  dependsOn: []
  isVerificationFile: false
  path: SWAG.py
  requiredBy: []
  timestamp: '2022-11-02 01:48:20+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: SWAG.py
layout: document
redirect_from:
- /library/SWAG.py
- /library/SWAG.py.html
title: SWAG.py
---
