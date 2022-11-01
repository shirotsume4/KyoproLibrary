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
  code: "class Trie_Vertex:\n    def __init__(self):\n        self.parent = None\n\
    \        self.one = None\n        self.zero = None\n\nclass Trie:\n    def __init__(self,\
    \ wordsize = 64):\n        self.wordsize = wordsize\n        self.root = Trie_Vertex()\n\
    \n    def add(self, x):\n        V = self.root\n        for i in range(self.wordsize\
    \ - 1, -1, -1):\n            if 1 & (x >> i):\n                if V.one is None:\n\
    \                    V.one = Trie_Vertex()\n                    V.one.parent =\
    \ V\n                V = V.one\n            else:\n                if V.zero is\
    \ None:\n                    V.zero = Trie_Vertex()\n                    V.zero.parent\
    \ = V\n                V = V.zero\n    def search(self, x):\n        V = self.root\n\
    \        for i in range(self.wordsize - 1, -1, -1):\n            if 1 & (x >>\
    \ i):\n                if V.one is None: return None\n                V = V.one\n\
    \            else:\n                if V.zero is None: return None\n         \
    \       V = V.zero\n        return V\n\n    def contains(self, x) -> bool:\n \
    \       if self.search(x) is None:\n            return False\n        else:\n\
    \            return True\n\n    \n    def remove(self, x):\n        V = self.search(x)\n\
    \        if V is None: return False\n        for i in range(self.wordsize):\n\
    \            P = V.parent\n            if P.zero == V:\n                P.zero\
    \ = None\n            else:\n                P.one = None\n            if P.zero\
    \ is not None or P.one is not None:\n                return True\n           \
    \ V = P\n        return True\n    \n    def xormin(self, x) -> int:\n        V\
    \ = self.root\n        xor = 0\n        for i in range(self.wordsize - 1, -1,\
    \ -1):\n            if 1 & (x >> i):\n                if V.one is not None:\n\
    \                    V = V.one\n                else:\n                    V =\
    \ V.zero\n                    xor += 2 ** i\n            else:\n             \
    \   if V.zero is not None:\n                    V = V.zero\n                else:\n\
    \                    V = V.one\n                    xor += 2 ** i\n        return\
    \ xor\n"
  dependsOn: []
  isVerificationFile: false
  path: Trie.py
  requiredBy: []
  timestamp: '2022-04-26 01:18:12+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Trie.py
layout: document
redirect_from:
- /library/Trie.py
- /library/Trie.py.html
title: Trie.py
---
