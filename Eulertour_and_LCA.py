class segtree():
    def __init__(self,V,OP,E):
        self.n=len(V)
        self.op=OP
        self.e=E
        self.log=(self.n-1).bit_length()
        self.size=1<<self.log
        self.d=[E for i in range(2*self.size)]
        for i in range(self.n):
            self.d[self.size+i]=V[i]
        for i in range(self.size-1,0,-1):
            self.update(i)

    def prod(self,l,r):
        assert 0<=l and l<=r and r<=self.n
        sml=self.e
        smr=self.e
        l+=self.size
        r+=self.size
        while(l<r):
            if (l&1):
                sml=self.op(sml,self.d[l])
                l+=1
            if (r&1):
                smr=self.op(self.d[r-1],smr)
                r-=1
            l>>=1
            r>>=1
        return self.op(sml,smr)
  
    def update(self,k):
        self.d[k]=self.op(self.d[2*k],self.d[2*k+1])

def EulerTour(s, graph):
    n = len(graph)
    visit = [False] * n
    visit[s] = True
    q = [s]
    ret = []
    while q:
        now = q.pop()
        if now >= 0:
            ret.append(now)
            for to in graph[now][::-1]:
                if not visit[to]:
                    visit[to] = True
                    q.append(~now)
                    q.append(to)
        else:
            ret.append(~now)
    
    return ret

def CalcDepth(s, graph):
    INF = 2 ** 63 - 1
    from collections import deque
    n = len(graph)
    depth = [INF] * n
    depth[s] = 0
    q = deque()
    q.append(s)
    while q:
        now = q.popleft()
        for to in graph[now]:
            if depth[to] == INF:
                depth[to] = depth[now] + 1
                q.append(to)
    return depth


class LCA():
    def __init__(self, graph):
        self.INF = 2 ** 63 - 1
        self.graph = graph
        self.N = len(self.graph)
        self.ET = EulerTour(0, self.graph)
        self.depth = CalcDepth(0, graph)
        self.disc = [-1] * (self.N)
        self.fin = [-1] * (self.N)
        for i, v in enumerate(self.ET):
            if self.disc[v] == -1:
                self.disc[v] = i
            self.fin[v] = i
        self.S = segtree([(self.ET[i], self.depth[self.ET[i]]) for i in range(len(self.ET))], lambda x, y: x if x[1] <= y[1] else y, (-1, self.INF))
    
    def lca(self, u, v):
        st = min(self.disc[u], self.disc[v])
        en = max(self.fin[u], self.fin[v]) + 1
        ver, _ = self.S.prod(st, en)
        return ver
    
    def dist(self, u, v):
        a = self.lca(u, v)
        return self.depth[u] + self.depth[v] - 2 * self.depth[a]
    
