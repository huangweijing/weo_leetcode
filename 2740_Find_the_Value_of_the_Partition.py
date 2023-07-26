from typing import List


class Solution:
    def findValueOfPartition(self, nums: List[int]) -> int:
        nums.sort()
        ans = nums[1] - nums[0]
        for i in range(1, len(nums)):
            diff = nums[i] - nums[i - 1]
            ans = min(ans, diff)
        return ans