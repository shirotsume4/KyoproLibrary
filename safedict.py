class sdict(dict):
    def __init__(self):
        import random
        self.r = random.randint(1, 2 ** 63 - 1)
    def __contains__(self, __o: object) -> bool:
        return super().__contains__(__o^self.r)
    def __getitem__(self, __key):
        return super().__getitem__(__key^self.r)
    def __setitem__(self, __key, __value):
        return super().__setitem__(__key^self.r, __value)