---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/associative_array
    links:
    - https://judge.yosupo.jp/problem/associative_array
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/associative_array\n\
    import sys\ninput = lambda: sys.stdin.readline().rstrip()\nii = lambda: int(input())\n\
    mi = lambda: map(int, input().split())\nli = lambda: list(mi())\ninf = 2 ** 63\
    \ - 1\nmod = 998244353\nclass sdict(dict):\n    def __init__(self):\n        import\
    \ random\n        self.r = random.randint(1, 2 ** 63 - 1)\n    def __contains__(self,\
    \ __o: object) -> bool:\n        return super().__contains__(__o^self.r)\n   \
    \ def __getitem__(self, __key):\n        return super().__getitem__(__key^self.r)\n\
    \    def __setitem__(self, __key, __value):\n        return super().__setitem__(__key^self.r,\
    \ __value)\n\nq = ii()\nd = sdict()\nfor _ in range(q):\n    query = li()\n  \
    \  if query[0] == 0:\n        k, v = query[1:]\n        d[k] = v\n    else:\n\
    \        k = query[1]\n        if k in d:\n            print(d[k])\n        else:\n\
    \            print(0)\n"
  dependsOn: []
  isVerificationFile: true
  path: test/safedict.test.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/safedict.test.py
layout: document
redirect_from:
- /verify/test/safedict.test.py
- /verify/test/safedict.test.py.html
title: test/safedict.test.py
---
