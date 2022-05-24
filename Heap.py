import heapq
class Heap():
    def __init__(self, maxi = False):
        self.sum = 0
        self.al = []
        self.maxi = maxi
        self.len = 0

    def __len__(self):
        return len(self.al)

    def add(self, x):
        if self.maxi:
            heapq.heappush(self.al, -x)
        else:
            heapq.heappush(self.al, x)
        self.sum += x
    
    def pop(self):
        if self.maxi:
            now = heapq.heappop(self.al)
            self.sum += now
            return -now
        else:
            now = heapq.heappop(self.al)
            self.sum -= now
            return now

    def top(self):
        now = self.pop()
        self.add(now)
        return now