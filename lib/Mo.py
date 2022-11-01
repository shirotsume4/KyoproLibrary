class Mo():
    def Pre(self, q, ls, rs, n):
        B = round(((3 ** 0.5) * n) / (2 * q) ** 0.5)
        mx = 0
        mxr = 0
        for i in range(len(ls)):
            l, r = ls[i], rs[i]
            mx, mxr = max(mx, l // B), max(mxr, r)
        bucket = [[] for _ in range(mx + 1)]
        for i in range(len(ls)):
            bucket[ls[i] // B].append(i)
        order = []
        for b in bucket:
            order.extend(sorted(b, key = lambda x: -rs[x]))
        return order
    
    def __init__(self, N, Q, A, LRs):
        self.n = N
        self.q = Q
        self.a = A
        self.table = [0] * (self.n + 1)
        self.ls = []
        self.rs = []
        for L, R in LRs:
            self.ls.append(L)
            self.rs.append(R + 1)
            
        self.order = self.Pre(self.q, self.ls, self.rs, self.n)
        self.ans = self.solve()
    
    def in_query(self, x, ans):
        #要素xが区間に入った時ansがどうなるか
        return ans

    def out_query(self, x, ans):
        #要素xが区間から出たときansがどうなるか
        return ans

    def solve(self):
        l = r = 0
        ans = 0
        ret = [0] * self.q
        for i in self.order:
            
            s, t = self.ls[i], self.rs[i]
            while l < s:
                ans = self.out_query(self.a[l], ans)
                l += 1
            while l > s:
                ans = self.in_query(self.a[l - 1], ans)
                l -= 1
            while r < t:
                ans = self.in_query(self.a[r], ans)
                r += 1
            while r > t:
                ans = self.out_query(self.a[r - 1], ans)
                r -= 1
            ret[i] = ans
        return ret
        