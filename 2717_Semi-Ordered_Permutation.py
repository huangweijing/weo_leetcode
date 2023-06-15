from typing import List

class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        n = len(nums)
        one_idx, n_idx = -1, -1
        for i, num in enumerate(nums):
            if num == 1:
                one_idx = i
            if num == n:
                n_idx = i
        if one_idx < n_idx:
            return one_idx + (n - 1) - n_idx
        else:
            return one_idx + (n - 1) - n_idx - 1
