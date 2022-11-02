---
data:
  _extendedDependsOn:
  - icon: ':question:'
    path: Matrix.py
    title: Matrix.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/matrix_product
    links:
    - https://judge.yosupo.jp/problem/matrix_product
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/matrix_product\n\
    import sys\nsys.path.append(\"..\")\ninput = lambda: sys.stdin.readline().rstrip()\n\
    ii = lambda: int(input())\nmi = lambda: map(int, input().split())\nli = lambda:\
    \ list(mi())\ninf = 2 ** 63 - 1\nmod = 998244353\nfrom Matrix import Matrix\n\n\
    n, m, k = map(int,input().split())\nmod = 998244353\na = [list(map(int,input().split()))\
    \ for _ in range(n)]\nb = [list(map(int,input().split())) for _ in range(m)]\n\
    \nc = [[0] * k for _ in range(n)]\n\nfor x in range(n):\n    for y in range(m):\n\
    \        for z in range(k):\n            c[x][z] += a[x][y] * b[y][z]\n      \
    \      c[x][z] %= mod\n\nfor i in range(n):\n    print(*c[i])"
  dependsOn:
  - Matrix.py
  isVerificationFile: true
  path: test/Matrixproduct.test.py
  requiredBy: []
  timestamp: '2022-11-02 23:38:59+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: test/Matrixproduct.test.py
layout: document
redirect_from:
- /verify/test/Matrixproduct.test.py
- /verify/test/Matrixproduct.test.py.html
title: test/Matrixproduct.test.py
---
