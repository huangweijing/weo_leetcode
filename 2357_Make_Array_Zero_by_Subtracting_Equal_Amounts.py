from typing import List

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        num_set = set(nums)
        if 0 in num_set:
            return len(num_set) - 1
        else:
            return len(num_set)