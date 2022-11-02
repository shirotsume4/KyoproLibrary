---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/bitwise_xor_convolution
    links:
    - https://judge.yosupo.jp/problem/bitwise_xor_convolution
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: '# verification-helper: PROBLEM https://judge.yosupo.jp/problem/bitwise_xor_convolution

    import sys

    sys.path.append("..")

    input = lambda: sys.stdin.readline().rstrip()

    ii = lambda: int(input())

    mi = lambda: map(int, input().split())

    li = lambda: list(mi())

    inf = 2 ** 63 - 1

    mod = 998244353

    from xorconvolution import xorconvolution


    n = ii()

    a = li()

    b = li()

    F = xorconvolution()


    print(*F.XORconv(a, b))'
  dependsOn: []
  isVerificationFile: true
  path: test/xorconv.test.py
  requiredBy: []
  timestamp: '2022-11-03 01:49:51+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: test/xorconv.test.py
layout: document
redirect_from:
- /verify/test/xorconv.test.py
- /verify/test/xorconv.test.py.html
title: test/xorconv.test.py
---
