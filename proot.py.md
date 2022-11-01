---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "import random\nfrom math import gcd\ndef isprime(n):\n    if n <= 2:\n  \
    \      return n == 2\n    if n % 2 == 0:\n        return False\n    s = 0\n  \
    \  t = n - 1\n    while t % 2 == 0:\n        s += 1\n        t //= 2\n    \n \
    \   for a in [2, 3, 5, 7, 11, 13, 17, 19, 23, 31, 37]:\n        if a >= n:\n \
    \           break\n        x = pow(a, t, n)\n        if x == 1 or x == n - 1:\n\
    \            continue\n        for _ in range(s):\n            x = (x * x) % n\n\
    \            if x == n - 1:\n                break\n        if x == n - 1:\n \
    \           continue\n\n        return False\n    return True\n\ndef Pollad(N):\n\
    \    if N % 2 == 0:\n        return 2\n    if isprime(N):\n        return N\n\
    \    def f(x):\n        return (x * x + 1) % N\n    step = 0\n\n    while True:\n\
    \        step += 1\n        x = step\n        y = f(x)\n        while True:\n\
    \            p = gcd(y - x + N, N)\n            if p == 0 or p == N:\n       \
    \         break\n            if p != 1:\n                return p\n          \
    \  x = f(x)\n            y = f(f(y))\n\n\ndef Primefact(N):\n    if N == 1:\n\
    \        return []\n    q = []\n    q.append(N)\n    ret = []\n    while q:\n\
    \        now = q.pop()\n        if now == 1:\n            continue\n        p\
    \ = Pollad(now)\n        if p == now:\n            ret.append(p)\n        else:\n\
    \            q.append(p)\n            q.append(now // p)\n\n    return ret\n\n\
    def proot(p):\n    P = Primefact(p - 1)\n    while True:\n        a = random.randint(0,\
    \ p - 1)\n        for v in P:\n            if pow(a, (p - 1) // v, p) == 1:\n\
    \                break\n        else:\n            return a\n        \n"
  dependsOn: []
  isVerificationFile: false
  path: proot.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: proot.py
layout: document
redirect_from:
- /library/proot.py
- /library/proot.py.html
title: proot.py
---
