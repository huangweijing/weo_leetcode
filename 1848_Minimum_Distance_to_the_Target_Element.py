from typing import List
import math


class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        idx = start
        cnt1, cnt2 = 0, 0
        while idx < len(nums) and nums[idx] != target:
            idx += 1
            cnt1 += 1
        if idx == len(nums):
            cnt1 = math.inf
        idx = start
        while idx >= 0 and nums[idx] != target:
            idx -= 1
            cnt2 += 1
        if idx == -1:
            cnt2 = math.inf
        return min(cnt1, cnt2)
