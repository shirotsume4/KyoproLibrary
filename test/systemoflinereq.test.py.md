---
data:
  _extendedDependsOn:
  - icon: ':x:'
    path: Matrix.py
    title: Matrix.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/system_of_linear_equations
    links:
    - https://judge.yosupo.jp/problem/system_of_linear_equations
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.8/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.8/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/system_of_linear_equations\n\
    import sys\nsys.path.append(\"..\")\ninput = lambda: sys.stdin.readline().rstrip()\n\
    ii = lambda: int(input())\nmi = lambda: map(int, input().split())\nli = lambda:\
    \ list(mi())\ninf = 2 ** 63 - 1\nmod = 998244353\nfrom Matrix import Matrix\n\n\
    n, m = mi()\na = Matrix(n, m)\n\nfor i in range(n):\n    al = li()\n    for j\
    \ in range(m):\n        a[i, j] = al[j]\n\nb = Matrix(n, 1)\nbl = li()\n\nfor\
    \ i in range(n):\n    b[i, 0] = bl[i]\n\nans, ker = a.lineareq(b)\nif ans is None:\n\
    \    print(-1)\n    exit()\nprint(len(ker))\n\nprint(*ans)\n\nfor v in ker:\n\
    \    print(*v)\n"
  dependsOn:
  - Matrix.py
  isVerificationFile: true
  path: test/systemoflinereq.test.py
  requiredBy: []
  timestamp: '2022-11-02 14:25:52+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: test/systemoflinereq.test.py
layout: document
redirect_from:
- /verify/test/systemoflinereq.test.py
- /verify/test/systemoflinereq.test.py.html
title: test/systemoflinereq.test.py
---
