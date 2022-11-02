---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':x:'
    path: test/tetration.test.py
    title: test/tetration.test.py
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from math import gcd\ndef isprime(n):\n    if n <= 2:\n        return n ==\
    \ 2\n    if n % 2 == 0:\n        return False\n    s = 0\n    t = n - 1\n    while\
    \ t % 2 == 0:\n        s += 1\n        t //= 2\n    \n    for a in [2, 3, 5, 7,\
    \ 11, 13, 17, 19, 23, 31, 37]:\n        if a >= n:\n            break\n      \
    \  x = pow(a, t, n)\n        if x == 1 or x == n - 1:\n            continue\n\
    \        for _ in range(s):\n            x = (x * x) % n\n            if x ==\
    \ n - 1:\n                break\n        if x == n - 1:\n            continue\n\
    \n        return False\n    return True\n\ndef Pollad(N):\n    if N % 2 == 0:\n\
    \        return 2\n    if isprime(N):\n        return N\n    def f(x):\n     \
    \   return (x * x + 1) % N\n    step = 0\n\n    while True:\n        step += 1\n\
    \        x = step\n        y = f(x)\n        while True:\n            p = gcd(y\
    \ - x + N, N)\n            if p == 0 or p == N:\n                break\n     \
    \       if p != 1:\n                return p\n            x = f(x)\n         \
    \   y = f(f(y))\n\n\ndef Primefact(N):\n    if N == 1:\n        return []\n  \
    \  q = []\n    q.append(N)\n    ret = []\n    while q:\n        now = q.pop()\n\
    \        if now == 1:\n            continue\n        p = Pollad(now)\n       \
    \ if p == now:\n            ret.append(p)\n        else:\n            q.append(p)\n\
    \            q.append(now // p)\n\n    return ret\n\ndef EulerPhi(n):\n    ret\
    \ = n\n    for i in range(2, n + 1):\n        if i * i > n:\n            break\n\
    \        if n % i == 0:\n            ret -= ret // i\n            while n % i\
    \ == 0:\n                n //= i\n    if n > 1:\n        ret -= ret // n\n   \
    \ return ret\n\ndef Tetration(a, b, mod):\n    if mod == 1:\n        return 0\n\
    \    if a == 0:\n        return 1 - (b & 1)\n    if b == 0:\n        return 1\n\
    \    if b == 1:\n        return a % mod\n    if b == 2:\n        return pow(a,\
    \ a, mod)\n    phi = EulerPhi(mod)\n    t = Tetration(a, b - 1, phi)\n    if t\
    \ == 0:\n        t += phi\n    return pow(a, t, mod)\n"
  dependsOn: []
  isVerificationFile: false
  path: Tetration.py
  requiredBy: []
  timestamp: '2022-11-02 01:48:20+09:00'
  verificationStatus: LIBRARY_ALL_WA
  verifiedWith:
  - test/tetration.test.py
documentation_of: Tetration.py
layout: document
redirect_from:
- /library/Tetration.py
- /library/Tetration.py.html
title: Tetration.py
---
