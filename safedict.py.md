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
  code: "class sdict(dict):\n    def __init__(self):\n        import random\n    \
    \    self.r = random.randint(1, 2 ** 63 - 1)\n    def __contains__(self, __o:\
    \ object) -> bool:\n        return super().__contains__(__o^self.r)\n    def __getitem__(self,\
    \ __key):\n        return super().__getitem__(__key^self.r)\n    def __setitem__(self,\
    \ __key, __value):\n        return super().__setitem__(__key^self.r, __value)"
  dependsOn: []
  isVerificationFile: false
  path: safedict.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: safedict.py
layout: document
title: safedict
---