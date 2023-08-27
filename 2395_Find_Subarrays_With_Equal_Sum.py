from typing import List


class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        equal_set = set[int]()
        for i in range(1, len(nums)):
            val = nums[i] + nums[i - 1]
            if val in equal_set:
                return True
            equal_set.add(val)
        return False
