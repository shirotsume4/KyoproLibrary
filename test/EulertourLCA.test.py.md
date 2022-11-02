---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/lca
    links:
    - https://judge.yosupo.jp/problem/lca
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/lca\nimport\
    \ sys\nsys.path.append(\"..\")\ninput = lambda: sys.stdin.readline().rstrip()\n\
    ii = lambda: int(input())\nmi = lambda: map(int, input().split())\nli = lambda:\
    \ list(mi())\ninf = 2 ** 63 - 1\nmod = 998244353\nfrom Eulertour_and_LCA import\
    \ LCA\n\nn, q = mi()\np = li()\ngraph = [[] for _ in range(n)]\n\nfor i in range(n\
    \ - 1):\n    graph[i + 1].append(p[i])\n    graph[p[i]].append(i + 1)\n\nL = LCA(graph)\n\
    \nfor _ in range(q):\n    u, v = mi()\n    print(L.lca(u, v))"
  dependsOn: []
  isVerificationFile: true
  path: test/EulertourLCA.test.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/EulertourLCA.test.py
layout: document
redirect_from:
- /verify/test/EulertourLCA.test.py
- /verify/test/EulertourLCA.test.py.html
title: test/EulertourLCA.test.py
---
