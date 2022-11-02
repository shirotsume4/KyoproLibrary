---
data:
  _extendedDependsOn:
  - icon: ':x:'
    path: Tetration.py
    title: Tetration.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/tetration_mod
    links:
    - https://judge.yosupo.jp/problem/tetration_mod
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/tetration_mod\n\
    import sys\nsys.path.append(\"..\")\ninput = lambda: sys.stdin.readline().rstrip()\n\
    ii = lambda: int(input())\nmi = lambda: map(int, input().split())\nli = lambda:\
    \ list(mi())\ninf = 2 ** 63 - 1\nfrom Tetration import Tetration\n\nfor _ in range(int(input())):\n\
    \    a, b, m = map(int,input().split())\n    print(Tetration(a, b, m))"
  dependsOn:
  - Tetration.py
  isVerificationFile: true
  path: test/tetration.test.py
  requiredBy: []
  timestamp: '2022-11-03 01:49:51+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: test/tetration.test.py
layout: document
redirect_from:
- /verify/test/tetration.test.py
- /verify/test/tetration.test.py.html
title: test/tetration.test.py
---
