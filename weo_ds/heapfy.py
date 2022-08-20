import heapq

class MyObject(object):
    def __init__(self, val):
        self.val = val

    def __cmp__(self, other):
        return cmp(self.val, other.val)
