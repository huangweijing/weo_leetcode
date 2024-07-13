from typing import List


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


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        wuf_alice = WeightedUnionFind(n)
        wuf_bob = WeightedUnionFind(n)
        edge_needed = 0
        for edge in edges:
            edge[1] -= 1
            edge[2] -= 1
            if edge[0] == 3:
                if wuf_alice.find(edge[1]) != wuf_alice.find(edge[2]):
                    wuf_alice.union(edge[1], edge[2])
                    wuf_bob.union(edge[1], edge[2])
                    edge_needed += 1
        # print(wuf_alice.count)
        # print(wuf_bob.count)
        for edge in edges:
            if edge[0] == 1:
                if wuf_alice.find(edge[1]) != wuf_alice.find(edge[2]):
                    wuf_alice.union(edge[1], edge[2])
                    edge_needed += 1
            if edge[0] == 2:
                if wuf_bob.find(edge[1]) != wuf_bob.find(edge[2]):
                    wuf_bob.union(edge[1], edge[2])
                    edge_needed += 1
        # print(wuf_alice.count)
        # print(wuf_bob.count)
        if wuf_alice.count == wuf_bob.count == 1:
            return len(edges) - edge_needed
        else:
            return -1


data = [
    4
    , [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]]
]
r = Solution().maxNumEdgesToRemove(* data)
print(r)