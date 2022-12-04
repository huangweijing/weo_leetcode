class WeightedUnionFind:

    def __init__(self, size):
        self.node = [i for i in range(size)]
        self.size = [1] * size
        self.count = size
        pass

    def find(self, p: int):
        while self.node[p] != p:
            p = self.node[p]
        return p

    def union(self, p: int, q: int):
        p = self.find(p)
        q = self.find(q)
        if p == q:
            return
        if self.size[p] < self.size[q]:
            self.node[p] = q
            self.size[q] = self.size[q] + self.size[p]
        else:
            self.node[q] = p
            self.size[p] = self.size[q] + self.size[p]
        self.count -= 1

class LUPrefix:

    def __init__(self, n: int):
        self.wuf = WeightedUnionFind(n)
        self.piece_set = set[int]()

    def upload(self, video: int) -> None:
        self.piece_set.add(video - 1)
        if video in self.piece_set:
            self.wuf.union(video - 1, video)
        if video - 2 in self.piece_set:
            self.wuf.union(video - 1, video - 2)

    def longest(self) -> int:
        if 0 not in self.piece_set:
            return 0
        root = self.wuf.find(0)
        return self.wuf.size[root]

