class Trie_Vertex:
    def __init__(self):
        self.parent = None
        self.one = None
        self.zero = None

class Trie:
    def __init__(self, wordsize = 64):
        self.wordsize = wordsize
        self.root = Trie_Vertex()

    def add(self, x):
        V = self.root
        for i in range(self.wordsize - 1, -1, -1):
            if 1 & (x >> i):
                if V.one is None:
                    V.one = Trie_Vertex()
                    V.one.parent = V
                V = V.one
            else:
                if V.zero is None:
                    V.zero = Trie_Vertex()
                    V.zero.parent = V
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
