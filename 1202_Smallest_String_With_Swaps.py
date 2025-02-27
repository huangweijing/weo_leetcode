from typing import List
from collections import defaultdict


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
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        wuf = WeightedUnionFind(len(s))
        for p in pairs:
            wuf.union(p[0], p[1])
        idx_list = defaultdict(lambda: list())
        idx_s = defaultdict(lambda: list())
        for i, ch in enumerate(s):
            idx = wuf.find(i)
            idx_list[idx].append(i)
            idx_s[idx].append(ch)
        new_arr = [""] * len(s)
        # print(idx_list)
        for key, val in idx_list.items():
            idx_s[key].sort()
            i = 0
            while i < len(idx_s[key]):
                new_arr[val[i]] = idx_s[key][i]
                i += 1
        return "".join(new_arr)
    

data = [
    "dcab"
    , [[0,3],[1,2],[0,2]]
]
r = Solution().smallestStringWithSwaps(*data)
print(r)