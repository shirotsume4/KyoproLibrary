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
  code: "def Dijkstra(s, graph):\n    INF = 2 ** 63 - 1\n    half = 10 ** 6\n    import\
    \ heapq\n    n = len(graph)\n    dist = [INF] * n\n    dist[s] = 0\n    bef =\
    \ [0] * n\n    bef[s] = s\n    hq = [0 * half + s]\n    heapq.heapify(hq)\n  \
    \  while hq:\n        x = heapq.heappop(hq)\n        c = x // half\n        now\
    \ = x % half\n        \n        if c > dist[now]:\n            continue\n    \
    \    for to, cost in graph[now]:\n            if dist[now] + cost < dist[to]:\n\
    \                dist[to] = cost + dist[now]\n                bef[to] = now\n\
    \                heapq.heappush(hq, dist[to] * half + to)\n    return dist, bef\n\
    \ndef DijkstraRest(bef, t):\n    now = t\n    ret = []\n    while bef[now] !=\
    \ now:\n        ret.append((bef[now], now))\n        now = bef[now]\n    ret.reverse()\n\
    \    return ret\n\n"
  dependsOn: []
  isVerificationFile: false
  path: Dijkstra.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Dijkstra.py
layout: document
redirect_from:
- /library/Dijkstra.py
- /library/Dijkstra.py.html
title: Dijkstra.py
---