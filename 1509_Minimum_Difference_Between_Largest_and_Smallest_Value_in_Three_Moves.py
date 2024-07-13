from typing import List


class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums.sort()
        ans = math.inf
        if len(nums) <= 4:
            return 0
        for i in range(0, 4):
            ans = min(ans, nums[len(nums) - 1 - (3 - i)] - nums[i])
        return ans
