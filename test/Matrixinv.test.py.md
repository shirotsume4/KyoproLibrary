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
    PROBLEM: https://judge.yosupo.jp/problem/inverse_matrix
    links:
    - https://judge.yosupo.jp/problem/inverse_matrix
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/inverse_matrix\n\
    import sys\nsys.path.append(\"..\")\ninput = lambda: sys.stdin.readline().rstrip()\n\
    ii = lambda: int(input())\nmi = lambda: map(int, input().split())\nli = lambda:\
    \ list(mi())\ninf = 2 ** 63 - 1\nmod = 998244353\nfrom Matrix import Matrix\n\
    n = ii()\na = Matrix(n, n, mod)\n\n\nfor i in range(n):\n    al = li()\n    for\
    \ j in range(n):\n        a[i, j] = al[j]\n\nf, a = a.inv()\n\nif not f:\n   \
    \ print(-1)\nelse:\n    a.print()"
  dependsOn:
  - Matrix.py
  isVerificationFile: true
  path: test/Matrixinv.test.py
  requiredBy: []
  timestamp: '2022-11-03 00:49:18+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: test/Matrixinv.test.py
layout: document
redirect_from:
- /verify/test/Matrixinv.test.py
- /verify/test/Matrixinv.test.py.html
title: test/Matrixinv.test.py
---
