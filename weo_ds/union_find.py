
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


# Test Code
data = [[1, 9], [2, 3], [3, 7], [7, 4], [5, 7], [8, 6]]
uf = WeightedUnionFind(10)
print(uf.node)
for pair in data:
    uf.union(*pair)
print(uf.node)
print(uf.count)

# uf.union(9, 0)
#
# print(uf.count)
# print(uf.find(3) == uf.find(8))
# uf.union(3, 8)
# print(uf.find(3) == uf.find(8))
# print(uf.count)
