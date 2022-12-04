from typing import List
from collections import deque

class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        avg_set = set()
        for i in range(len(nums) >> 1):
            avg_set.add((nums[i] + nums[len(nums) - 1 - i]) / 2)
        return len(avg_set)
