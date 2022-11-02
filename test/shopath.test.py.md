---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/shortest_path
    links:
    - https://judge.yosupo.jp/problem/shortest_path
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/shortest_path\n\
    import sys\nsys.path.append(\"..\")\ninput = lambda: sys.stdin.readline().rstrip()\n\
    ii = lambda: int(input())\nmi = lambda: map(int, input().split())\nli = lambda:\
    \ list(mi())\ninf = 2 ** 63 - 1\nmod = 998244353\n\nfrom Dijkstra import Dijkstra,\
    \ DijkstraRest\n\nn, m, s, t = mi()\ngraph = [[] for _ in range(n)]\nfor _ in\
    \ range(m):\n    u, v, w = mi()\n    graph[u].append((v, w))\n\nd, r = Dijkstra(s,\
    \ graph)\nif d[t] >= inf:\n    print(-1)\n    exit()\nret = DijkstraRest(r, t)\n\
    print(d[t], len(ret))\nfor u, v in ret:\n    print(u, v)"
  dependsOn: []
  isVerificationFile: true
  path: test/shopath.test.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: test/shopath.test.py
layout: document
redirect_from:
- /verify/test/shopath.test.py
- /verify/test/shopath.test.py.html
title: test/shopath.test.py
---
