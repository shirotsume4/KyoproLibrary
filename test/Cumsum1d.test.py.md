---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: Cumsum1d.py
    title: Cumsum1d.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/static_range_sum
    links:
    - https://judge.yosupo.jp/problem/static_range_sum
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/static_range_sum\n\
    import sys\nsys.path.append(\"..\")\ninput = lambda: sys.stdin.readline().rstrip()\n\
    ii = lambda: int(input())\nmi = lambda: map(int, input().split())\nli = lambda:\
    \ list(mi())\ninf = 2 ** 63 - 1\nmod = 998244353\nfrom Cumsum1d import Cumsum1d\n\
    \n\nn, q = mi()\n\na = li()\n\nA = Cumsum1d(a)\n\nfor _ in range(q):\n    l, r\
    \ = mi()\n    print(A[l:r])"
  dependsOn:
  - Cumsum1d.py
  isVerificationFile: true
  path: test/Cumsum1d.test.py
  requiredBy: []
  timestamp: '2022-11-02 13:56:10+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/Cumsum1d.test.py
layout: document
redirect_from:
- /verify/test/Cumsum1d.test.py
- /verify/test/Cumsum1d.test.py.html
title: test/Cumsum1d.test.py
---
