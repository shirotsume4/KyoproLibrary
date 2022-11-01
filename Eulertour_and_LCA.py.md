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
  code: "class segtree():\n    def __init__(self,V,OP,E):\n        self.n=len(V)\n\
    \        self.op=OP\n        self.e=E\n        self.log=(self.n-1).bit_length()\n\
    \        self.size=1<<self.log\n        self.d=[E for i in range(2*self.size)]\n\
    \        for i in range(self.n):\n            self.d[self.size+i]=V[i]\n     \
    \   for i in range(self.size-1,0,-1):\n            self.update(i)\n\n    def prod(self,l,r):\n\
    \        assert 0<=l and l<=r and r<=self.n\n        sml=self.e\n        smr=self.e\n\
    \        l+=self.size\n        r+=self.size\n        while(l<r):\n           \
    \ if (l&1):\n                sml=self.op(sml,self.d[l])\n                l+=1\n\
    \            if (r&1):\n                smr=self.op(self.d[r-1],smr)\n       \
    \         r-=1\n            l>>=1\n            r>>=1\n        return self.op(sml,smr)\n\
    \  \n    def update(self,k):\n        self.d[k]=self.op(self.d[2*k],self.d[2*k+1])\n\
    \ndef EulerTour(s, graph):\n    n = len(graph)\n    visit = [False] * n\n    visit[s]\
    \ = True\n    q = [s]\n    ret = []\n    while q:\n        now = q.pop()\n   \
    \     if now >= 0:\n            ret.append(now)\n            for to in graph[now][::-1]:\n\
    \                if not visit[to]:\n                    visit[to] = True\n   \
    \                 q.append(~now)\n                    q.append(to)\n        else:\n\
    \            ret.append(~now)\n    \n    return ret\n\ndef CalcDepth(s, graph):\n\
    \    INF = 2 ** 63 - 1\n    from collections import deque\n    n = len(graph)\n\
    \    depth = [INF] * n\n    depth[s] = 0\n    q = deque()\n    q.append(s)\n \
    \   while q:\n        now = q.popleft()\n        for to in graph[now]:\n     \
    \       if depth[to] == INF:\n                depth[to] = depth[now] + 1\n   \
    \             q.append(to)\n    return depth\n\n\nclass LCA():\n    def __init__(self,\
    \ graph):\n        self.INF = 2 ** 63 - 1\n        self.graph = graph\n      \
    \  self.N = len(self.graph)\n        self.ET = EulerTour(0, self.graph)\n    \
    \    self.depth = CalcDepth(0, graph)\n        self.disc = [-1] * (self.N)\n \
    \       self.fin = [-1] * (self.N)\n        for i, v in enumerate(self.ET):\n\
    \            if self.disc[v] == -1:\n                self.disc[v] = i\n      \
    \      self.fin[v] = i\n        self.S = segtree([(self.ET[i], self.depth[self.ET[i]])\
    \ for i in range(len(self.ET))], lambda x, y: x if x[1] <= y[1] else y, (-1, self.INF))\n\
    \    \n    def lca(self, u, v):\n        st = min(self.disc[u], self.disc[v])\n\
    \        en = max(self.fin[u], self.fin[v]) + 1\n        ver, _ = self.S.prod(st,\
    \ en)\n        return ver\n    \n    def dist(self, u, v):\n        a = self.lca(u,\
    \ v)\n        return self.depth[u] + self.depth[v] - 2 * self.depth[a]\n    \n"
  dependsOn: []
  isVerificationFile: false
  path: Eulertour_and_LCA.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Eulertour_and_LCA.py
layout: document
redirect_from:
- /library/Eulertour_and_LCA.py
- /library/Eulertour_and_LCA.py.html
title: Eulertour_and_LCA.py
---
