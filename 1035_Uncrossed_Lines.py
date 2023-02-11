from typing import List
from functools import cache

class Solution:
    def __init__(self):
        self.nums1, self.nums2 = [], []

    @cache
    def my_sol(self, max_idx1: int, max_idx2: int) -> int:
        # print(max_idx1, max_idx2)
        if max_idx1 < 0 or max_idx2 < 0:
            return 0

        ans = 0
        i = max_idx1
        while i >= 0:
            if self.nums1[i] == self.nums2[max_idx2]:
                ans = max(ans, self.my_sol(i - 1, max_idx2 - 1) + 1)
            i -= 1
        i = max_idx2
        while i >= 0:
            if self.nums1[max_idx1] == self.nums2[i]:
                ans = max(ans, self.my_sol(max_idx1 - 1, i - 1) + 1)
            i -= 1
        ans = max(ans, self.my_sol(max_idx1 - 1, max_idx2 - 1))
        return ans

    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        self.nums1, self.nums2 = nums1, nums2
        return self.my_sol(len(nums1) - 1, len(nums2) - 1)

data = [
    [1,3,7,1,7,5]
    , [1,9,2,5,1]
]
r = Solution().maxUncrossedLines(* data)
print(r)