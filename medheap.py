import heapq
class MedianHeap():
    def __init__(self):
        self.top = []
        self.bottom = []
    def __len__(self):
        return len(self.top) + len(self.bottom)
    def add(self, x):
        heapq.heappush(self.top, x)
        while len(self.top) - 2 >= len(self.bottom):
            heapq.heappush(self.bottom, -heapq.heappop(self.top))
        while self.top and self.bottom and self.top[0] < -self.bottom[0]:
            x = heapq.heappop(self.top)
            y = heapq.heappop(self.bottom)
            heapq.heappush(self.top, -y)
            heapq.heappush(self.bottom, -x)
    def med(self):
        if len(self) % 2:
            return self.top[0], self.top[0]
        else:
            return -self.bottom[0], self.top[0]
M = MedianHeap()
for v in [2, 5, 3, 4]:
    M.add(v)
print(M.med())
