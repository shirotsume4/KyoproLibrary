---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: CountPrime.py
    title: CountPrime.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/counting_primes
    links:
    - https://judge.yosupo.jp/problem/counting_primes
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: '# verification-helper: PROBLEM https://judge.yosupo.jp/problem/counting_primes

    import sys

    sys.path.append("..")

    input = lambda: sys.stdin.readline().rstrip()

    ii = lambda: int(input())

    mi = lambda: map(int, input().split())

    li = lambda: list(mi())

    inf = 2 ** 63 - 1

    mod = 998244353

    from CountPrime import countprime

    print(countprime(int(input())))'
  dependsOn:
  - CountPrime.py
  isVerificationFile: true
  path: test/CountPrime.test.py
  requiredBy: []
  timestamp: '2022-11-02 13:20:43+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/CountPrime.test.py
layout: document
redirect_from:
- /verify/test/CountPrime.test.py
- /verify/test/CountPrime.test.py.html
title: test/CountPrime.test.py
---
