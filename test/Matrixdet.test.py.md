---
data:
  _extendedDependsOn:
  - icon: ':question:'
    path: Matrix.py
    title: Matrix.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/matrix_det
    links:
    - https://judge.yosupo.jp/problem/matrix_det
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/matrix_det\n\
    import sys\nsys.path.append(\"..\")\ninput = lambda: sys.stdin.readline().rstrip()\n\
    ii = lambda: int(input())\nmi = lambda: map(int, input().split())\nli = lambda:\
    \ list(mi())\ninf = 2 ** 63 - 1\nmod = 998244353\nfrom Matrix import Matrix\n\n\
    n = ii()\na = Matrix(n, n, mod)\n\nfor i in range(n):\n    al = li()\n    for\
    \ j in range(n):\n        a[i, j] = al[j]\n\nprint(a.det())"
  dependsOn:
  - Matrix.py
  isVerificationFile: true
  path: test/Matrixdet.test.py
  requiredBy: []
  timestamp: '2022-11-03 01:23:41+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/Matrixdet.test.py
layout: document
redirect_from:
- /verify/test/Matrixdet.test.py
- /verify/test/Matrixdet.test.py.html
title: test/Matrixdet.test.py
---
