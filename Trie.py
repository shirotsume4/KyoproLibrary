
class Trie:
    def __init__(self, wordsize = 64):
        self.wordsize = wordsize
        self.root = 0
        self.leftch = {}
        self.rightch = {}
        self.parent = {}

    def add(self, x):
        V = self.root
        for i in range(self.wordsize - 1, -1, -1):
            fr = 2 ** i
            if 1 & (x >> i):
                if V not in self.rightch:
                    self.rightch[V] = V + fr
                    self.parent[V + fr] = V
                V = V + fr
            else:
                if V not in self.leftch:
                    self.leftch[V] = V
                    self.parent[V] = V
                V = V.zero
    def search(self, x):
        V = self.root
        for i in range(self.wordsize - 1, -1, -1):
            if 1 & (x >> i):
                if V.one is None: return None
                V = V.one
            else:
                if V.zero is None: return None
                V = V.zero
        return V

    def contains(self, x) -> bool:
        if self.search(x) is None:
            return False
        else:
            return True

    
    def remove(self, x):
        V = self.search(x)
        if V is None: return False
        for i in range(self.wordsize):
            P = V.parent
            if P.zero == V:
                P.zero = None
            else:
                P.one = None
            if P.zero is not None or P.one is not None:
                return True
            V = P
        return True
    
    def xormin(self, x) -> int:
        V = self.root
        xor = 0
        for i in range(self.wordsize - 1, -1, -1):
            if 1 & (x >> i):
                if V.one is not None:
                    V = V.one
                else:
                    V = V.zero
                    xor += 2 ** i
            else:
                if V.zero is not None:
                    V = V.zero
                else:
                    V = V.one
                    xor += 2 ** i
        return xor
