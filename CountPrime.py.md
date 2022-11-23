---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/CountPrime.test.py
    title: test/CountPrime.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def countprime(n):\n    if n <= 1:\n        return 0\n    elif n <= 2:\n\
    \        return 1\n    elif n <= 3:\n        return 2\n    nsq = round(n ** 0.5)\n\
    \    ndsq = n // nsq\n    L = [0] * ndsq\n\n    for i in range(1, ndsq):\n   \
    \     L[i] = n // i - 1\n    LS = list(range(-1, nsq))\n    count = 0\n    for\
    \ p in range(2, nsq + 1):\n        if LS[p] == LS[p - 1]:\n            continue\n\
    \        q = p * p\n        nowp = p\n        indm = min(ndsq, n // q + 1)\n \
    \       for to in range(1, indm):\n            if nowp < ndsq:\n             \
    \   L[to] -= L[nowp]\n            else:\n                L[to] -= LS[n // nowp]\n\
    \            L[to] += count\n            nowp += p\n\n        for to in range(nsq,\
    \ q - 1, -1):\n            LS[to] -= LS[to // p] - count \n        count += 1\n\
    \    return L[1]"
  dependsOn: []
  isVerificationFile: false
  path: CountPrime.py
  requiredBy: []
  timestamp: '2022-11-02 13:20:43+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/CountPrime.test.py
documentation_of: CountPrime.py
layout: document
redirect_from:
- /library/CountPrime.py
- /library/CountPrime.py.html
title: CountPrime.py
---