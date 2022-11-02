---
data:
  _extendedDependsOn:
  - icon: ':x:'
    path: andconvolution.py
    title: andconvolution.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/bitwise_and_convolution
    links:
    - https://judge.yosupo.jp/problem/bitwise_and_convolution
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: '# verification-helper: PROBLEM https://judge.yosupo.jp/problem/bitwise_and_convolution

    import sys

    sys.path.append("..")

    input = lambda: sys.stdin.readline().rstrip()

    ii = lambda: int(input())

    mi = lambda: map(int, input().split())

    li = lambda: list(mi())

    inf = 2 ** 63 - 1

    mod = 998244353

    from andconvolution import andconvolution


    n = ii()

    a = li()

    b = li()

    F = andconvolution()


    print(*F.ANDconv(a, b))'
  dependsOn:
  - andconvolution.py
  isVerificationFile: true
  path: test/andconv.test.py
  requiredBy: []
  timestamp: '2022-11-03 01:49:51+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: test/andconv.test.py
layout: document
redirect_from:
- /verify/test/andconv.test.py
- /verify/test/andconv.test.py.html
title: test/andconv.test.py
---
