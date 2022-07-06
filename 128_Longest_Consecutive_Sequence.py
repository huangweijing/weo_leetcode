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

    def union(self, p: int, q: int) -> int:
        p = self.find(p)
        q = self.find(q)
        if p == q:
            return self.size[p]
        if self.size[p] < self.size[q]:
            self.node[p] = q
            self.size[q] = self.size[q] + self.size[p]
            self.count -= 1
            return self.size[q]
        else:
            self.node[q] = p
            self.size[p] = self.size[q] + self.size[p]
            self.count -= 1
            return self.size[p]


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #union find
        wuf = WeightedUnionFind(len(nums))
        # hashmap num -> idx
        max_size = 0
        num_dic = dict[int, int]()
        for idx, num in enumerate(nums):
            if num in num_dic:
                continue
            num_dic[num] = idx
            size = 1

            if num + 1 in num_dic.keys():
                p1_idx = num_dic[num + 1]
                size = wuf.union(idx, p1_idx)
            if num - 1 in num_dic.keys():
                p1_idx = num_dic[num - 1]
                size = wuf.union(idx, p1_idx)
            if size > max_size:
                max_size = size
        return max_size

sol = Solution()
data = [0,3,7,2,5,8,4,6,0,1]
r = sol.longestConsecutive(data)
print(r)