---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: DSWAG.py
    title: DSWAG.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/deque_operate_all_composite
    links:
    - https://judge.yosupo.jp/problem/deque_operate_all_composite
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/deque_operate_all_composite\n\
    import sys\nsys.path.append(\"..\")\ninput = lambda: sys.stdin.readline().rstrip()\n\
    ii = lambda: int(input())\nmi = lambda: map(int, input().split())\nli = lambda:\
    \ list(mi())\ninf = 2 ** 63 - 1\nmod = 998244353\nfrom DSWAG import DSWAG\ndef\
    \ op(x, y):\n    xa, xb = y\n    ya, yb = x\n    za = xa * ya % mod\n    zb =\
    \ xa * yb + xb\n    zb %= mod\n    return (za, zb)\n\n\nq = ii()\n\nS = DSWAG(op,\
    \ (1, 0))\n\nfor _ in range(q):\n    t = li()\n    if t[0] == 0:\n        a, b\
    \ = t[1:]\n        S.pushleft((a, b))\n    elif t[0] == 1:\n        a, b = t[1:]\n\
    \        S.push((a, b))\n    elif t[0] == 2:\n        S.popleft()\n    elif t[0]\
    \ == 3:\n        S.pop()\n    else:\n        x = t[1]\n        a, b = S.fold()\n\
    \        print((a * x + b) % mod)"
  dependsOn:
  - DSWAG.py
  isVerificationFile: true
  path: test/DSWAG.test.py
  requiredBy: []
  timestamp: '2022-11-02 13:56:10+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/DSWAG.test.py
layout: document
redirect_from:
- /verify/test/DSWAG.test.py
- /verify/test/DSWAG.test.py.html
title: test/DSWAG.test.py
---
