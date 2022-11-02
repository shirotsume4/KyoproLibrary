---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/associative_array
    links:
    - https://judge.yosupo.jp/problem/associative_array
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.8/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.8/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/associative_array\n\
    import sys\ninput = lambda: sys.stdin.readline().rstrip()\nii = lambda: int(input())\n\
    mi = lambda: map(int, input().split())\nli = lambda: list(mi())\ninf = 2 ** 63\
    \ - 1\nmod = 998244353\nfrom .. import safedict\nq = ii()\nd = sdict()\nfor _\
    \ in range(q):\n    query = li()\n    if query[0] == 0:\n        k, v = query[1:]\n\
    \        d[k] = v\n    else:\n        k = query[1]\n        if k in d:\n     \
    \       print(d[k])\n        else:\n            print(0)\n"
  dependsOn: []
  isVerificationFile: true
  path: test/safedict.test.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: test/safedict.test.py
layout: document
redirect_from:
- /verify/test/safedict.test.py
- /verify/test/safedict.test.py.html
title: test/safedict.test.py
---
