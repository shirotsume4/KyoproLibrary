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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.8/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.8/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def Manacher(s):\n    t = []\n    for v in s:\n        t.append(v)\n    \
    \    t.append('$')\n    t.pop()\n    ret = [0] * len(t)\n    i = 0\n    j = 0\n\
    \n    while i < len(t):\n        while i - j >= 0 and i + j < len(t) and t[i -\
    \ j] == t[i + j]:\n            j += 1\n        ret[i] = j\n        k = 1\n   \
    \     while i  - k >= 0 and i + k < len(t) and k + ret[i - k] < j:\n         \
    \   ret[i + k] = ret[i - k]\n            k += 1\n        i += k\n        j -=\
    \ k\n    for i in range(len(t)):\n        if t[i] == '$' and ret[i] % 2:\n   \
    \         ret[i] -= 1\n        if t[i] != '$' and ret[i] % 2 == 0:\n         \
    \   ret[i] -= 1\n    return ret\n\n        \n\n\n"
  dependsOn: []
  isVerificationFile: false
  path: manacher.py
  requiredBy: []
  timestamp: '2022-05-03 00:13:15+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: manacher.py
layout: document
redirect_from:
- /library/manacher.py
- /library/manacher.py.html
title: manacher.py
---
