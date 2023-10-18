from typing import List
from functools import cache
import math


class Solution:
    def __init__(self):
        self.nums1 = []
        self.nums2 = []

    @cache
    def my_sol(self, s1: int, s2: int) -> int:
        if s1 >= len(self.nums1) or s2 >= len(self.nums2):
            return -math.inf
        if s1 == len(self.nums1) - 1 and s2 == len(self.nums2) - 1:
            return self.nums1[s1] * self.nums2[s2]
        sol1 = self.my_sol(s1, s2 + 1)
        sol2 = self.my_sol(s1 + 1, s2)
        sol3 = self.my_sol(s1 + 1, s2 + 1)
        if sol3 < 0:
            sol3 = 0
        sol3 += self.nums1[s1] * self.nums2[s2]
        # print(s1, s2, sol1, sol2, sol3)
        return max(sol1, sol2, sol3)

    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        self.nums1, self.nums2 = nums1, nums2
        return self.my_sol(0, 0)


data = [
[-5,-1,-2]
, [3,3,5,5]
]
r = Solution().maxDotProduct(*data)
print(r)
