from typing import List


class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        arr = nums[1:]
        arr.sort()
        return sum(arr[:2]) + nums[0]
