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
  code: "import heapq\nclass mcf_graph():\n    n=1\n    pos=[]\n    g=[[]]\n    def\
    \ __init__(self,N):\n        self.n=N\n        self.pos=[]\n        self.g=[[]\
    \ for i in range(N)]\n    def add_edge(self,From,To,cap,cost):\n        assert\
    \ 0<=From and From<self.n\n        assert 0<=To and To<self.n\n        m=len(self.pos)\n\
    \        self.pos.append((From,len(self.g[From])))\n        self.g[From].append({\"\
    to\":To,\"rev\":len(self.g[To]),\"cap\":cap,\"cost\":cost})\n        self.g[To].append({\"\
    to\":From,\"rev\":len(self.g[From])-1,\"cap\":0,\"cost\":-cost})\n    def get_edge(self,i):\n\
    \        m=len(self.pos)\n        assert 0<=i and i<m\n        _e=self.g[self.pos[i][0]][self.pos[i][1]]\n\
    \        _re=self.g[_e[\"to\"]][_e[\"rev\"]]\n        return {\"from\":self.pos[i][0],\"\
    to\":_e[\"to\"],\"cap\":_e[\"cap\"]+_re[\"cap\"],\n        \"flow\":_re[\"cap\"\
    ],\"cost\":_e[\"cost\"]}\n    def edges(self):\n        m=len(self.pos)\n    \
    \    result=[{} for i in range(m)]\n        for i in range(m):\n            tmp=self.get_edge(i)\n\
    \            result[i][\"from\"]=tmp[\"from\"]\n            result[i][\"to\"]=tmp[\"\
    to\"]\n            result[i][\"cap\"]=tmp[\"cap\"]\n            result[i][\"flow\"\
    ]=tmp[\"flow\"]\n            result[i][\"cost\"]=tmp[\"cost\"]\n        return\
    \ result\n    def flow(self,s,t,flow_limit=(1<<63)-1):\n        return self.slope(s,t,flow_limit)[-1]\n\
    \    def slope(self,s,t,flow_limit=(1<<63)-1):\n        assert 0<=s and s<self.n\n\
    \        assert 0<=t and t<self.n\n        assert s!=t\n        '''\n        \
    \ variants (C = maxcost):\n         -(n-1)C <= dual[s] <= dual[i] <= dual[t] =\
    \ 0\n         reduced cost (= e.cost + dual[e.from] - dual[e.to]) >= 0 for all\
    \ edge\n        '''\n        dual=[0 for i in range(self.n)]\n        dist=[0\
    \ for i in range(self.n)]\n        pv=[0 for i in range(self.n)]\n        pe=[0\
    \ for i in range(self.n)]\n        vis=[False for i in range(self.n)]\n      \
    \  def dual_ref():\n            for i in range(self.n):\n                dist[i]=(1<<63)-1\n\
    \                pv[i]=-1\n                pe[i]=-1\n                vis[i]=False\n\
    \            que=[]\n            heapq.heappush(que,(0,s))\n            dist[s]=0\n\
    \            while(que):\n                v=heapq.heappop(que)[1]\n          \
    \      if vis[v]:continue\n                vis[v]=True\n                if v==t:break\n\
    \                '''\n                 dist[v] = shortest(s, v) + dual[s] - dual[v]\n\
    \                 dist[v] >= 0 (all reduced cost are positive)\n             \
    \    dist[v] <= (n-1)C\n                '''\n                for i in range(len(self.g[v])):\n\
    \                    e=self.g[v][i]\n                    if vis[e[\"to\"]] or\
    \ (not(e[\"cap\"])):continue\n                    '''\n                     |-dual[e.to]+dual[v]|\
    \ <= (n-1)C\n                     cost <= C - -(n-1)C + 0 = nC\n             \
    \       '''\n                    cost=e[\"cost\"]-dual[e[\"to\"]]+dual[v]\n  \
    \                  if dist[e[\"to\"]]-dist[v]>cost:\n                        dist[e[\"\
    to\"]]=dist[v]+cost\n                        pv[e[\"to\"]]=v\n               \
    \         pe[e[\"to\"]]=i\n                        heapq.heappush(que,(dist[e[\"\
    to\"]],e[\"to\"]))\n            if not(vis[t]):\n                return False\n\
    \            for v in range(self.n):\n                if not(vis[v]):continue\n\
    \                dual[v]-=dist[t]-dist[v]\n            return True\n        flow=0\n\
    \        cost=0\n        prev_cost=-1\n        result=[(flow,cost)]\n        while(flow<flow_limit):\n\
    \            if not(dual_ref()):\n                break\n            c=flow_limit-flow\n\
    \            v=t\n            while(v!=s):\n                c=min(c,self.g[pv[v]][pe[v]][\"\
    cap\"])\n                v=pv[v]\n            v=t\n            while(v!=s):\n\
    \                self.g[pv[v]][pe[v]][\"cap\"]-=c\n                self.g[v][self.g[pv[v]][pe[v]][\"\
    rev\"]][\"cap\"]+=c\n                v=pv[v]\n            d=-dual[s]\n       \
    \     flow+=c\n            cost+=c*d\n            if(prev_cost==d):\n        \
    \        result.pop()\n            result.append((flow,cost))\n            prev_cost=cost\n\
    \        return result\n"
  dependsOn: []
  isVerificationFile: false
  path: bflow.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: bflow.py
layout: document
redirect_from:
- /library/bflow.py
- /library/bflow.py.html
title: bflow.py
---
